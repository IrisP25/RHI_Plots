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

temp_all = (allFileContent[0].split(","))[-1].strip()
chi_all = (allFileContent[1].split(","))[2].strip()
print (temp_strange,temp_light)
print (chi_strange,chi_light)

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
 
print (experimentalYields)
print (experimentalYieldErr)
print (oneTempYield)
print (oneTempDev)





