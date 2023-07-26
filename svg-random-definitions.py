import os
import sys
import re
import random
import string
from xml.dom import minidom
from xml.parsers.expat import ExpatError

def random_string(length=6):
    """Generate a random string of fixed length"""
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))

def update_svg(svg_path):
    try:
        with open(svg_path, 'r') as f:
            svg_content = f.read()

        # Parse SVG content
        svg_doc = minidom.parseString(svg_content)

        # Get all style elements
        style_elements = svg_doc.getElementsByTagName('style')

        # Map for old name -> new name
        name_map = {}

        for style in style_elements:
            style_text = style.firstChild.nodeValue

            # Find all unique identifiers in the style block
            identifiers = re.findall(r'(?<!\d)\.(.*?)[,{]', style_text)
            identifiers += re.findall(r'url\(#(.*?)\)', style_text)

            # Randomize these identifiers
            for identifier in set(identifiers):
                new_name = random_string()
                name_map[identifier] = new_name

            # Replace all instances of these identifiers in the style block
            for old_name, new_name in name_map.items():
                style_text = re.sub(r'(?<!\d)\.' + re.escape(old_name) + r'(?=[,{])', '.' + new_name, style_text)
                style_text = re.sub(r'url\(#' + re.escape(old_name) + r'\)', 'url(#' + new_name + ')', style_text)

            # Update style text
            style.firstChild.nodeValue = style_text

        # Now update all elements which reference these identifiers
        for elem in svg_doc.getElementsByTagName('*'):
            for attr in ['class', 'id']:
                if attr in elem.attributes.keys():
                    old_value = elem.getAttribute(attr)
                    if old_value in name_map:
                        elem.setAttribute(attr, name_map[old_value])

        # Write the updated SVG content to new file
        new_file_path = svg_path[:-4] + '-rw.svg'
        with open(new_file_path, 'w') as f:
            # Write elements without XML declaration
            for element in svg_doc.childNodes:
                element.writexml(f)
    except ExpatError:
        print(f"Warning: Skipped file '{svg_path}' due to XML parsing error.")

def main():
    directory = sys.argv[1]

    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        # If the file is SVG, process it
        if filename.endswith('.svg'):
            svg_path = os.path.join(directory, filename)
            update_svg(svg_path)

if __name__ == "__main__":
    main()
