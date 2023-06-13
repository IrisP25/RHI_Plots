import os 
import sys
import numpy as np
import argparse
import shutil 

parser = argparse.ArgumentParser()
parser.add_argument("inputDirectory",help="Input config file")
parser.add_argument("energyForYield",help='Give an energy to analyze')

args = parser.parse_args()
fileName="STAR_AuAu_"+args.energyForYield

#fistFiles=[]
#Search for files in which 
for file in os.listdir(args.inputDirectory):
  if file.startswith(fileName) and file.endswith("FixedFormat.txt"):
  	#fistFiles.append(file)
  	if "strange" in file:
  	  print ("Reading strange %s file",file)
  	  strangeFile = open(args.inputDirectory+"/"+file)
  	  strangeFileContent=strangeFile.readlines()
  	  #print (strangeFileContent[0])
  	  
  	elif "piKp" in file:
  	  print ("Reading piKp %s file",file)
  	  lightFile = open(args.inputDirectory+"/"+file)
  	  lightFileContent=lightFile.readlines()
  	else:
  	  print ("Reading all %s file",file)
  	  allFile = open(args.inputDirectory+"/"+file)
  	  allFileContent=allFile.readlines()
  	  
#Now we get the info from each file that we need! From each fist file we need the temperature, chi^2 and 
#we need all the experimental yields and errors 
#let's start with the temperatures

temp_strange = (strangeFileContent[1].split(","))[2].strip()
chi_strange = (strangeFileContent[0].split(","))[-1].strip()

temp_light =  (lightFileContent[1].split(","))[2].strip()
chi_light = (lightFileContent[0].split(","))[-1].strip()

temp_all = (allFileContent[1].split(","))[2].strip()
chi_all = (allFileContent[0].split(","))[-1].strip()
print (temp_strange,temp_light,temp_all)
print (chi_strange,chi_light,chi_all)

#Now I want to get the particle yields for each files and start formatting them as they will be outputted
#on the code that will be ran
##format enum{lpip, lpim, lkp, lkm, lk0s, lproton, lpbar, llambda, llamdabar, lphi, lxi, lxibar, lomega, lomegabar};
experimentalYields = "double yield_exp[npart] ={" 
experimentalYieldErr = "double yield_experr[npart]={"
twoTempYield = "double modelYield_twocfo[npart] = {" 
oneTempYield = "double modelYield_onecfo[npart] = {"
oneTempDev="double dev_1fo[npart] = {"
twoTempDev="double dev_2fo[npart] = {"
for index in range(9,len(allFileContent)-1):
  print (index,len(allFileContent))
  
  if index ==13:
    experimentalYields += (allFileContent[-1].split(","))[2].strip()
    experimentalYields +=","    
    experimentalYields += (allFileContent[index].split(","))[2].strip()
    experimentalYields +=","
    
    #now fill up the experimental error side! 
    experimentalYieldErr += (allFileContent[-1].split(","))[4].strip()
    experimentalYieldErr += ","
    experimentalYieldErr += (allFileContent[index].split(","))[4].strip()
    experimentalYieldErr += ","
    
    
    #now we want to get the model yields for both temperatures :D 
    oneTempYield += (allFileContent[-1].split(","))[6].strip()
    oneTempYield += ","
    oneTempYield += (allFileContent[index].split(","))[6].strip()
    oneTempYield += ","
    
    oneTempDev += (allFileContent[-1].split(","))[8].strip()
    oneTempDev += ","
    oneTempDev += (allFileContent[index].split(","))[8].strip()
    oneTempDev += ","
    allFileContent.pop()
    
    twoTempYield += (strangeFileContent[-1].split(","))[6].strip()
    twoTempYield += ","
    twoTempYield += (lightFileContent[index].split(","))[6].strip()
    twoTempYield += ","
    
    twoTempDev += (strangeFileContent[-1].split(","))[6].strip()
    twoTempDev += ","
    twoTempDev += (lightFileContent[index].split(","))[6].strip()
    twoTempDev += ","
    
    strangeFileContent.pop()
    lightFileContent.pop()
    #Now the most complicated is the 2 temperature since piKp are from ome 
    continue
  if index == len(allFileContent)-1:
    experimentalYields += (allFileContent[-1].split(","))[2].strip()
    experimentalYields += "};"
    experimentalYieldErr += (allFileContent[-1].split(","))[4].strip()
    experimentalYieldErr += "};"
    oneTempYield += (allFileContent[index].split(","))[6].strip()
    oneTempYield += "};"
    oneTempDev += (allFileContent[index].split(","))[8].strip()
    oneTempDev += "};"
    twoTempYield += (strangeFileContent[index].split(","))[6].strip()
    twoTempYield += "};"
    twoTempDev += (strangeFileContent[index].split(","))[8].strip()
    twoTempDev += "};"
    
    print (" LAST ENTRY IN FILE DONE")
    continue
  experimentalYields += (allFileContent[index].split(","))[2].strip()
  experimentalYields +=","
  experimentalYieldErr += (allFileContent[index].split(","))[4].strip()
  experimentalYieldErr += ","
  oneTempYield += (allFileContent[index].split(","))[6].strip()
  oneTempYield += ","
  oneTempDev += (allFileContent[index].split(","))[8].strip()
  oneTempDev += ","
  
  ###
  if index< 13 or index ==14:
      twoTempYield += (lightFileContent[index].split(","))[6].strip()
      twoTempYield += ","
      twoTempDev += (lightFileContent[index].split(","))[8].strip()
      twoTempDev += ","
  
  if index >14:
      twoTempYield += (strangeFileContent[index].split(","))[6].strip()
      twoTempYield += ","
      twoTempDev += (strangeFileContent[index].split(","))[8].strip()
      twoTempDev += ","

print (experimentalYieldErr)
print (oneTempYield)
print (oneTempDev)
print (twoTempYield)
print (twoTempDev)

#Now we need to read in the Yield code Fernando gave me. We will modify the lines with the yield inputs as
#but also the temperature and Chi info from the legends!
yieldPlot = open(args.inputDirectory+"/Yieldsndevs_39.C")
yieldPlotContent = yieldPlot.readlines()

newFile = "YieldPlot"+args.energyForYield+".C"
with open(newFile,'w') as outputFile:
    outputFile.writelines("void YieldPlot"+args.energyForYield+"() \n")
    for index_out in range(2,len(yieldPlotContent)):
        ##first replace the yield info!!
        if index_out <10:
            outputFile.writelines(yieldPlotContent[index_out])
        elif index_out ==10:
            outputFile.writelines(oneTempYield+"\n")
        elif index_out ==11:
            outputFile.writelines(twoTempYield+"\n")
        elif index_out == 13:
            outputFile.writelines(experimentalYields+"\n")
        elif index_out == 14:
            outputFile.writelines(experimentalYieldErr+"\n")
        elif index_out == 16:
            outputFile.writelines(oneTempDev+"\n")
        elif index_out == 17:
            outputFile.writelines(twoTempDev+"\n")
        elif index_out == 147:
            oneTempLegend = yieldPlotContent[147].split()
            oneTempLegend[(oneTempLegend.index("MeV,")-1)] = temp_all
            oneTempLegend[(oneTempLegend.index("dof")+2)] = chi_all+'","L");'
            outputFile.writelines((" ".join(oneTempLegend))+"\n")
        elif index_out == 148:
            lightTempLegend = yieldPlotContent[148].split()
            lightTempLegend[(lightTempLegend.index("MeV,")-1)] = temp_light
            lightTempLegend[(lightTempLegend.index("dof)_{")+3)] = chi_light+'","L");'
            outputFile.writelines((" ".join(lightTempLegend))+"\n")
        elif index_out == 149:
            strangeTempLegend = yieldPlotContent[149].split()
            strangeTempLegend[(strangeTempLegend.index("MeV,")-1)] = temp_strange
            strangeTempLegend[(strangeTempLegend.index("dof)_{")+3)] = chi_strange+'","L");'
            outputFile.writelines((" ".join(strangeTempLegend))+"\n")
        else:
            outputFile.writelines(yieldPlotContent[index_out])
        
outputFile.close()



