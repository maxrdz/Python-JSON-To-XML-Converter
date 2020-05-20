import xml.etree.cElementTree as ElementTree
import json
import time

inputFileName = input("JSON File you want to convert: ")

jsonInput = inputFileName

# Open and Parse JSON

print(f"Opening '{jsonInput}' JSON File...")
try:
	with open(jsonInput, "r") as inputJson:
		try:
			jsonDict = json.load(inputJson)
		except:
			print(f"ERROR: '{jsonInput}' could not be parsed. JSON file might be invalid.")
except:
	print("Something went wrong with opening the file. Try again.")
finally:
	print(f"Successfully Parsed '{jsonInput}': {jsonDict}")


def parse_element(root, json_dict):
	for key in json_dict:
		if type(json_dict[key]) is (dict or list or tuple):

			sub_dict = json_dict[key]
			sub_element = ElementTree.SubElement(root, str(key))
			parse_element(sub_element, sub_dict)

		else:
			ElementTree.SubElement(root, str(key)).text = str(json_dict[key])


# Creating XML Elements

xml = ElementTree.Element("XML")  # Create base element that will hold json data

parse_element(xml, jsonDict)

# Write XML File

outputXML = ElementTree.ElementTree(xml)
print("Creating output XML file...")

try:
	outputXML.write("Output_XML.xml")

except:
	print("Could not create file due to an exception.")

finally:
	print("XML File Successfully Created!")
	time.sleep(1)
	for _ in range(2):
		print("...")
		time.sleep(1)
	print("Closing in 3 seconds...")
	time.sleep(3)
