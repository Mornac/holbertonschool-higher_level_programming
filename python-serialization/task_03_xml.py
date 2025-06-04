#!/usr/bin/env python3
"""
Serialization and Deserialization of Python Objects to XML
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename): 
    """
    Serialize a dictionary to an XML file.
    Parameters:
        dictionary: python dictionary to serialize.
        filename: Name of the XML file to write to.
    """
    root = ET.Element("root")
    
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    
    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)

def deserialize_from_xml(filename):
    """
    Deserialize an XML file to a dictionary.
    Parameters:
        filename: Name of the XML file to read from.
    Returns:
        A dictionary containing the data from the XML file.
    """
    tree = ET.parse(filename)
    root = tree.getroot()
    dictionary = {}
    for child in root:
        dictionary[child.tag] = child.text
    return dictionary
