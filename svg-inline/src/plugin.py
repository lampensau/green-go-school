import os
import re
import random
import string
from bs4 import BeautifulSoup
from xml.dom import minidom
from xml.parsers.expat import ExpatError
from mkdocs.plugins import BasePlugin
from mkdocs import utils

class SvgInlinePlugin(BasePlugin):
    def __init__(self):
        self.svg_count = 0

    def on_page_content(self, content, **kwargs):
        self.svg_count = 0
        self.current_file = kwargs.get("page").file.src_path
        basepath = os.path.dirname(kwargs.get("page").file.abs_src_path)
        # match any img tag
        pattern = re.compile(r'<img[^>]*>', flags=re.IGNORECASE)
        content = re.sub(pattern, lambda match: process_img_tag(basepath, match.group(), self), content)
        if self.svg_count > 0:
            utils.log.info(f"SVG Inline: Replaced and inlined {self.svg_count} SVG images in document {self.current_file}.")
        return content

def read_file(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

def random_id(size=6):
    return ''.join(random.choice(string.ascii_letters) for _ in range(size))

def process_img_tag(basepath, img_tag, plugin):
    soup = BeautifulSoup(img_tag, 'lxml')
    img = soup.img
    # check if it's an SVG image with the inline="true" attribute
    if img['src'].endswith('.svg') and img.get('inline') == 'true':
        return process_svg_img(basepath, img, plugin)
    else:
        return img_tag

def process_svg_img(basepath, img, plugin):
    classes = img.get('class', '')
    alt_text = img.get('alt', '')
    src = img['src'].replace('.svg', '')
    # check if the source file is not 'index.md' and adjust the src attribute
    if not plugin.current_file.endswith('index.md'):
        src = os.path.relpath(src, '..')
    filename = os.path.abspath(os.path.join(basepath, src + '.svg'))
    utils.log.debug(f"basepath: {basepath}, src: {src}, filename: {filename}")
    svg_content = read_file(filename)
    svg_doc = minidom.parseString(svg_content)
    svg_doc = randomize_ids_and_classes(svg_doc)
    # convert back to string
    svg_content = svg_doc.toxml()
    soup = BeautifulSoup(svg_content, 'lxml-xml')
    add_accessibility_features(soup, alt_text)
    plugin.svg_count += 1
    return wrap_svg(soup, classes)

def randomize_ids_and_classes(svg_doc):
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
            new_name = random_id()
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
    return svg_doc

def add_accessibility_features(soup, alt_text):
    svg = soup.svg
    svg['role'] = 'img'
    title_id = random_id()
    desc_id = random_id()
    svg['aria-labelledby'] = f'{title_id} {desc_id}'
    title = soup.new_tag('title', id=title_id)
    title.string = alt_text
    svg.insert(0, title)
    desc = soup.new_tag('desc', id=desc_id)
    desc.string = alt_text
    svg.insert(1, desc)

def wrap_svg(soup, classes):
    wrapper = soup.new_tag('div')
    wrapper['class'] = classes
    wrapper.append(soup.svg.extract())
    return str(wrapper)
