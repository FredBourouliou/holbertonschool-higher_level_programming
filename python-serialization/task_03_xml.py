#!/usr/bin/env python3
import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to XML and save it to a file
    
    Args:
        dictionary: Python dictionary to serialize
        filename: Output XML filename
    """
    # Create the root element
    root = ET.Element("data")
    
    # Add dictionary items as child elements
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    
    # Create an ElementTree object and write to file
    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)

def deserialize_from_xml(filename):
    """
    Deserialize data from an XML file to a Python dictionary
    
    Args:
        filename: Input XML filename
    
    Returns:
        dict: Deserialized dictionary
    """
    try:
        # Parse the XML file
        tree = ET.parse(filename)
        root = tree.getroot()
        
        # Create dictionary from XML elements
        result = {}
        for child in root:
            result[child.tag] = child.text
        
        return result
    except Exception:
        return None
