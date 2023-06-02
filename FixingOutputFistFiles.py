import os
import subprocess
import sys
import numpy as np
import matplotlib.pyplot as plt
import argparse
import time
import shutil
import ROOT
parser = argparse.ArgumentParser()
parser.add_argument("inputFile",help="Input config file")
args = parser.parse_args()
fistFile = open(args.inputFile) 
content = fistFile.readlines()

#print (content[10])
wrongVolumeSplit = content[10].split() 
#print (wrongVolumeSplit)
radiusInfo = wrongVolumeSplit[0:5]
#print (radiusInfo)
volumeInfo = wrongVolumeSplit[5:]
#print (volumeInfo)
radiusString = " ".join(wrongVolumeSplit[0:5])
volumeString = " ".join(wrongVolumeSplit[5:])
#print (volumeString)
content[10]=radiusString+"\n"
content.insert(11, volumeString+"\n")
print (content[10])
print (content[11])

#now I want to try everything all at once 
print(" ".join(content[4].split()))
newFile = "test.txt"

#the next step i want to try to get the name of the output file from the input file!  
with open(newFile, 'w') as file:
    for index in range(0,len(content)):
        #get only the lines that we are interested in but try to keep the same format on all of them
        
        if index == 4: 
            file.writelines((" ".join(content[index].split()))+"\n")
        elif index>= 9 and index<17:
            file.writelines((" ".join(content[index].split()))+"\n")
        elif index >= 20:
            file.writelines((" ".join(content[index].split()))+"\n")

    ### if i kept these lines they would keep the original formatting which meant everything would look weird. 
    #file.writelines((" ".join(content[4].split()))+"\n")
    #file.writelines(" ".join(content[9:17].split()))
    #file.writelines((" ".join(content[i].split()+'\n' for i in range(7,19))))
    #file.writelines((" ".join(content[j].split()) for j in range(20,len(content)))+'\n')

file.close()
#Now I only care about line 5, 10-16 and 20-32. Remember to subract one to match the indices properly


