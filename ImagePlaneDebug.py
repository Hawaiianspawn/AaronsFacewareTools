'''
Script by Aaron Low 
Date: 08/01/2022
Quick script to swap the impagePlane between clean and tracked images.
Todo: Add the original tracking frames as those are higher resolution  
-Increase the rsplit to go deeper into the directory
-Swap while playing. 
'''
from maya import OpenMaya
import maya.cmds as cmds
import os.path


#Pull and concatenate directory to easily organized string.
selection = cmds.ls(type="imagePlane")
if selection == []:
    OpenMaya.MGlobal.displayError("No imagePlane in scene, please import a Faceware scene with imagePlane")

filePath = cmds.getAttr(selection[0]+".imageName").rsplit("/", 2)
fileName = filePath[2].rsplit(".",1)[0]
fileExt = filePath[2].rsplit(".",1)[1]
folderName = filePath[1]
dirPath = filePath[0]


#Swap between folder locations
#Change folder, add or strip suffix from file name. newName created after if statement.  
if "results" in fileName:
    fullName = fileName.rsplit(".",1)
    fileName = fullName[0][:-8]
    suffix = "" 
    frameNum = fullName[1]
    folderName = fileName + "_frames"
else:
    folderName = "results"
    fullName = fileName.rsplit(".",1)
    fileName = fullName[0]
    suffix = "_results"
    frameNum = fullName[1]

newName = dirPath + "/" + folderName + "/" + fileName + suffix + "." + frameNum + "." + fileExt 
if os.path.exists(newName):
    cmds.setAttr(selection[0]+".imageName", newName, type='string')
else:
    OpenMaya.MGlobal.displayError("Unable to find file: " + newName)