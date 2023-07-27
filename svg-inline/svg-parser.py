import os
import argparse
import re
import tinycss2
from bs4 import BeautifulSoup
from uuid import uuid4

def parse_args():
    parser = argparse.ArgumentParser(description='Process SVG files in a directory.')
    parser.add_argument('directory', help='Directory to process')
    return parser.parse_args()

def process_svg_elements(soup, tag, attr):
    elements = soup.find_all(tag)
    for element in elements:
        element[attr] = str(uuid4())
    return soup

def main():
    args = parse_args()
    base_path = args.directory

    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file.endswith(".svg"):
                file_path = os.path.join(root, file)
                print(f'Processing {file_path}')
                try:
                    with open(file_path, 'r+') as f:
                        soup = BeautifulSoup(f.read(), 'xml')

                        # Process SVG elements
                        tags_attrs = [
                            ('style', 'class'),
                            ('mask', 'id'),
                            ('filter', 'id'),
                            ('clipPath', 'id'),
                            (re.compile('(linear|radial)Gradient'), 'id'),
                            ('pattern', 'id'),
                        ]
                        for tag, attr in tags_attrs:
                            soup = process_svg_elements(soup, tag, attr)

                        # TODO: Add CSS parsing and modification here

                        f.seek(0)
                        f.write(str(soup))
                        f.truncate()

                except IOError:
                    print(f"Error opening or writing to file: {file_path}")

if __name__ == "__main__":
    main()
