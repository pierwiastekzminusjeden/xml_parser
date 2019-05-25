#!/usr/bin/env python3
###########################
#@author Krystian Molenda
#@version 1.0.0
###########################

from source.XmlReader import XmlReader
from source.JsonWriter import JsonWriter

#Reading XML file and pre-validating data by XmlReader object
xmlReader = XmlReader('input.xml')
objectList = xmlReader.read()

#Validating data (checking if the object has one or more fields) and printing json file
jsonWriter = JsonWriter('output.json')
jsonWriter.writeFromString(objectList)