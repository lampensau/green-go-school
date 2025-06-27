import os
from bs4 import BeautifulSoup
from collections import defaultdict

# Directory containing the SVG files
svg_dir = '/home/timo/green-go-school/docs/assets/images'

# Dictionary to store style definitions
styles = defaultdict(list)

# Walk through the directory and subdirectories
for root, dirs, files in os.walk(svg_dir):
    for file in files:
        if file.endswith('.svg'):
            # Open SVG file and parse it with BeautifulSoup
            with open(os.path.join(root, file), 'r') as f:
                soup = BeautifulSoup(f.read(), 'xml')
                
            # Find all style elements within defs
            for style in soup.find_all('style'):
                for rule in style.string.split('}'):
                    if rule.strip():
                        selector, properties = rule.split('{')
                        # Remove any leading/trailing whitespace and add to dictionary
                        styles[selector.strip()].append((file, properties.strip()))

# Sort the styles alphabetically by their selectors
sorted_styles = sorted(styles.items(), key=lambda x: x[0])

# Print common styles
for selector, definitions in sorted_styles:
    if len(definitions) > 1:
        # This style appears in more than one file
        print(f"{selector}{{{definitions[0][1]}}}")

# Print unique styles
for selector, definitions in sorted_styles:
    if len(definitions) == 1:
        # This style appears in only one file
        print(f"{selector}{{{definitions[0][1]}}} in {definitions[0][0]}")
