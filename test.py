import xml.etree.ElementTree as ET
import uuid

def replace_ids_and_classes(svg_string):
    namespaces = {'ns': 'http://www.w3.org/2000/svg', 'xlink': 'http://www.w3.org/1999/xlink'}
    ET.register_namespace("", namespaces['ns'])
    ET.register_namespace("xlink", namespaces['xlink'])

    root = ET.fromstring(svg_string)

    # Create a dictionary to store the old and new names
    name_changes = {}

    # Replace the style classes and id's
    for elem in root.iter():
        if 'class' in elem.attrib:
            old_names = elem.attrib['class'].split(' ')
            new_names = []
            for old_name in old_names:
                if old_name not in name_changes:
                    name_changes[old_name] = str(uuid.uuid4()).replace('-', '')
                new_names.append(name_changes[old_name])
            elem.attrib['class'] = ' '.join(new_names)

        if 'id' in elem.attrib:
            old_name = elem.attrib['id']
            if old_name not in name_changes:
                name_changes[old_name] = str(uuid.uuid4()).replace('-', '')
            elem.attrib['id'] = name_changes[old_name]
        
        if 'clip-path' in elem.attrib:
            old_name = elem.attrib['clip-path'].split('#')[-1]
            if old_name in name_changes:
                elem.attrib['clip-path'] = 'url(#' + name_changes[old_name] + ')'

        if 'mask' in elem.attrib:
            old_name = elem.attrib['mask'].split('#')[-1]
            if old_name in name_changes:
                elem.attrib['mask'] = 'url(#' + name_changes[old_name] + ')'
        
        if 'filter' in elem.attrib:
            old_name = elem.attrib['filter'].split('#')[-1]
            if old_name in name_changes:
                elem.attrib['filter'] = 'url(#' + name_changes[old_name] + ')'

        for gradient in elem.findall('{'+namespaces['ns']+'}linearGradient'):
            old_name = gradient.attrib['id']
            if old_name in name_changes:
                gradient.attrib['id'] = name_changes[old_name]

        for radial in elem.findall('{'+namespaces['ns']+'}radialGradient'):
            old_name = radial.attrib['id']
            if old_name in name_changes:
                radial.attrib['id'] = name_changes[old_name]

    return ET.tostring(root, encoding='unicode')

svg_string = '<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 205.76 66.44"><defs><style>.cls-1,.cls-5{fill:none;}.cls-2{isolation:isolate;}.cls-3{clip-path:url(#clip-path);}.cls-4{fill:#356cb4;}.cls-5{stroke:#1d1d1b;stroke-miterlimit:10;}.cls-6{fill:#305784;}.cls-7{fill:#202020;}.cls-8{fill:#fff;}.cls-9{fill:#1d1d1b;}.cls-10{fill:#106e31;}.cls-11{opacity:0.52;mix-blend-mode:multiply;}.cls-12{clip-path:url(#clip-path-4);}.cls-13{fill:#368a41;}</style><clipPath id="clip-path"><rect class="cls-1" x="12.63" y="6.7" width="185.76" height="52"/></clipPath><clipPath id="clip-path-4"><rect class="cls-1" x="133.77" y="18.29" width="40.72" height="29.87" transform="translate(81.5 173.17) rotate(-74.74)"/></clipPath></defs><g class="cls-2"><g id="Ebene_1" data-name="Ebene 1"><g id="MCX-Display-Setup"><g class="cls-3"><g class="cls-3"><path class="cls-4" d="M28.48,22H16.13a3,3,0,0,1-3-3V12.36a3,3,0,0,1,3-3H28.48a3,3,0,0,1,3,3V19a3,3,0,0,1-3,3"/><rect class="cls-5" x="13.13" y="9.36" width="18.34" height="12.66" rx="3"/><path class="cls-4" d="M28.48,39H16.13a3,3,0,0,1-3-3V29.36a3,3,0,0,1,3-3H28.48a3,3,0,0,1,3,3V36a3,3,0,0,1-3,3"/><rect class="cls-5" x="13.13" y="26.36" width="18.34" height="12.66" rx="3"/><path class="cls-4" d="M28.48,56H16.13a3,3,0,0,1-3-3V46.32a3,3,0,0,1,3-3H28.48a3,3,0,0,1,3,3V53a3,3,0,0,1-3,3"/><rect class="cls-5" x="13.13" y="43.32" width="18.34" height="12.66" rx="3"/><path class="cls-4" d="M139.64,22H127.29a3,3,0,0,1-3-3V12.36a3,3,0,0,1,3-3h12.35a3,3,0,0,1,3,3V19a3,3,0,0,1-3,3"/><rect class="cls-5" x="124.29" y="9.36" width="18.35" height="12.66" rx="3"/><path class="cls-6" d="M171.58,22H159.23a3,3,0,0,1-3-3V12.36a3,3,0,0,1,3-3h12.35a3,3,0,0,1,3,3V19a3,3,0,0,1-3,3"/><rect class="cls-5" x="156.23" y="9.36" width="18.35" height="12.66" rx="3"/><path class="cls-4" d="M171.58,56H159.23a3,3,0,0,1-3-3V46.32a3,3,0,0,1,3-3h12.35a3,3,0,0,1,3,3V53a3,3,0,0,1-3,3"/><rect class="cls-5" x="156.23" y="43.32" width="18.35" height="12.66" rx="3"/><path class="cls-4" d="M139.64,39H127.29a3,3,0,0,1-3-3V29.36a3,3,0,0,1,3-3h12.35a3,3,0,0,1,3,3V36a3,3,0,0,1-3,3"/><rect class="cls-5" x="124.29" y="26.36" width="18.35" height="12.66" rx="3"/><path class="cls-4" d="M139.64,56H127.29a3,3,0,0,1-3-3V46.32a3,3,0,0,1,3-3h12.35a3,3,0,0,1,3,3V53a3,3,0,0,1-3,3"/><rect class="cls-5" x="124.29" y="43.32" width="18.35" height="12.66" rx="3"/><path class="cls-7" d="M46.12,7.19a2.55,2.55,0,0,0-2.55,2.55V55.65a2.55,2.55,0,0,0,2.55,2.55h63.53a2.55,2.55,0,0,0,2.55-2.55V9.74a2.55,2.55,0,0,0-2.55-2.55"/><rect class="cls-8" x="44.24" y="17.86" width="67.29" height="8.51"/></g><path class="cls-9" d="M52.45,22.39H50.29v1.77h2.5v.53H49.63v-5h3.13v.53H50.29v1.61h2.16Z"/><path class="cls-9" d="M54.75,22.35,55.57,21h.74L55.1,22.82l1.25,1.87h-.73l-.86-1.38-.85,1.38h-.74l1.25-1.87L53.21,21h.73Z"/><path class="cls-9" d="M57,20a.38.38,0,0,1,.1-.26.32.32,0,0,1,.28-.11.34.34,0,0,1,.28.11.37.37,0,0,1,.09.26.37.37,0,0,1-.09.25.37.37,0,0,1-.28.1.34.34,0,0,1-.28-.1A.37.37,0,0,1,57,20Zm.69,4.67H57V21h.63Z"/><path class="cls-9" d="M59.54,20.1V21h.69v.49h-.69v2.29a.5.5,0,0,0,.09.33.37.37,0,0,0,.31.12,2.39,2.39,0,0,0,.31,0v.5a1.71,1.71,0,0,1-.49.07.8.8,0,0,1-.64-.25,1.13,1.13,0,0,1-.21-.73V21.49h-.68V21h.68v-.9Z"/><path class="cls-8" d="M53.14,28.72V32.1a1.62,1.62,0,0,1-.45,1.16,1.83,1.83,0,0,1-1.19.5h-.17a1.81,1.81,0,0,1-1.3-.44,1.56,1.56,0,0,1-.5-1.21V28.72h.65v3.37a1.15,1.15,0,1,0,2.3,0V28.72Z"/><path class="cls-8" d="M56.23,32.72a.45.45,0,0,0-.2-.4,1.77,1.77,0,0,0-.67-.25,3.6,3.6,0,0,1-.76-.24,1.14,1.14,0,0,1-.42-.34.84.84,0,0,1-.13-.48,1,1,0,0,1,.38-.77,1.49,1.49,0,0,1,1-.31,1.58,1.58,0,0,1,1,.32,1.05,1.05,0,0,1,.39.84h-.63a.58.58,0,0,0-.22-.45.81.81,0,0,0-.56-.19.87.87,0,0,0-.54.15.47.47,0,0,0-.19.39.39.39,0,0,0,.18.35,2.16,2.16,0,0,0,.65.22,3.66,3.66,0,0,1,.77.25,1.16,1.16,0,0,1,.44.36.87.87,0,0,1,.14.5,1,1,0,0,1-.4.8,1.64,1.64,0,0,1-1,.29,1.94,1.94,0,0,1-.78-.15,1.31,1.31,0,0,1-.54-.44,1,1,0,0,1-.19-.61h.63a.64.64,0,0,0,.26.5.92.92,0,0,0,.62.19A1,1,0,0,0,56,33.1.44.44,0,0,0,56.23,32.72Z"/><path class="cls-8" d="M59.22,33.76A1.63,1.63,0,0,1,58,33.27,1.85,1.85,0,0,1,57.52,32v-.12a2.24,2.24,0,0,1,.21-1,1.7,1.7,0,0,1,.59-.68,1.48,1.48,0,0,1,.82-.24,1.41,1.41,0,0,1,1.12.47,2.05,2.05,0,0,1,.4,1.37V32H58.15a1.33,1.33,0,0,0,.32.88,1,1,0,0,0,.78.34,1.15,1.15,0,0,0,.57-.14,1.54,1.54,0,0,0,.41-.36l.38.3A1.53,1.53,0,0,1,59.22,33.76Zm-.08-3.31a.81.81,0,0,0-.64.28,1.34,1.34,0,0,0-.33.78H60v-.05a1.27,1.27,0,0,0-.26-.75A.83.83,0,0,0,59.14,30.45Z"/><path class="cls-8" d="M63.18,30.57a1.55,1.55,0,0,0-.31,0,.84.84,0,0,0-.85.53V33.7h-.63V30H62v.43a1,1,0,0,1,.88-.5.7.7,0,0,1,.28.05Z"/><path class="cls-8" d="M52.38,41.4H50.3l-.47,1.3h-.68l1.9-5h.58l1.9,5h-.67Zm-1.89-.54h1.7l-.85-2.33Z"/><path class="cls-8" d="M56.38,42.33a1.32,1.32,0,0,1-1.08.44,1.16,1.16,0,0,1-.9-.35,1.44,1.44,0,0,1-.31-1V39h.63v2.39c0,.56.23.84.68.84a1,1,0,0,0,1-.54V39H57v3.7h-.6Z"/><path class="cls-8" d="M57.81,40.82a2.17,2.17,0,0,1,.4-1.37,1.36,1.36,0,0,1,2.08-.07V37.45h.64V42.7h-.58l0-.4a1.35,1.35,0,0,1-2.1-.06,2.19,2.19,0,0,1-.4-1.37Zm.63.07a1.57,1.57,0,0,0,.26,1,.83.83,0,0,0,.72.36.91.91,0,0,0,.87-.54V40a.92.92,0,0,0-.87-.52.83.83,0,0,0-.72.36A1.75,1.75,0,0,0,58.44,40.89Z"/><path class="cls-8" d="M61.91,38a.39.39,0,0,1,.09-.26.38.38,0,0,1,.28-.11.35.35,0,0,1,.28.11.39.39,0,0,1,0,.52.38.38,0,0,1-.28.1.41.41,0,0,1-.28-.1A.39.39,0,0,1,61.91,38Zm.68,4.68H62V39h.63Z"/><path class="cls-8" d="M63.44,40.82a2.21,2.21,0,0,1,.21-1,1.51,1.51,0,0,1,.6-.67,1.69,1.69,0,0,1,2.09.28,2,2,0,0,1,.47,1.4v0a2.19,2.19,0,0,1-.21,1,1.61,1.61,0,0,1-.59.67,1.65,1.65,0,0,1-.89.24,1.58,1.58,0,0,1-1.22-.53,2,2,0,0,1-.46-1.38Zm.63.07a1.6,1.6,0,0,0,.29,1,.9.9,0,0,0,.76.37.93.93,0,0,0,.77-.38,1.7,1.7,0,0,0,.28-1,1.53,1.53,0,0,0-.29-1,.91.91,0,0,0-.76-.38.92.92,0,0,0-.76.37A1.75,1.75,0,0,0,64.07,40.89Z"/><path class="cls-8" d="M53.29,50.12a1.81,1.81,0,0,1-.58,1.22,1.89,1.89,0,0,1-1.3.43A1.77,1.77,0,0,1,50,51.14a2.58,2.58,0,0,1-.53-1.7V49a2.74,2.74,0,0,1,.25-1.22,1.86,1.86,0,0,1,.7-.81,2,2,0,0,1,1.06-.28,1.79,1.79,0,0,1,1.27.44,1.81,1.81,0,0,1,.55,1.22h-.66a1.4,1.4,0,0,0-.37-.86,1.1,1.1,0,0,0-.79-.27,1.19,1.19,0,0,0-1,.47A2.12,2.12,0,0,0,50.12,49v.48a2.17,2.17,0,0,0,.34,1.29,1.1,1.1,0,0,0,.95.48,1.26,1.26,0,0,0,.84-.25,1.36,1.36,0,0,0,.38-.86Z"/><path class="cls-8" d="M53.92,49.82a2.08,2.08,0,0,1,.22-1,1.61,1.61,0,0,1,.59-.67,1.58,1.58,0,0,1,.87-.24,1.56,1.56,0,0,1,1.22.53,2,2,0,0,1,.47,1.39v0a2.16,2.16,0,0,1-.21,1,1.54,1.54,0,0,1-.59.67,1.64,1.64,0,0,1-.88.24,1.59,1.59,0,0,1-1.22-.52,2,2,0,0,1-.47-1.39Zm.64.07a1.59,1.59,0,0,0,.28,1,.92.92,0,0,0,.77.37.9.9,0,0,0,.76-.37,1.76,1.76,0,0,0,.29-1.06,1.6,1.6,0,0,0-.29-1,.93.93,0,0,0-.77-.38.9.9,0,0,0-.75.38A1.63,1.63,0,0,0,54.56,49.89Z"/><path class="cls-8" d="M58.68,48l0,.47a1.34,1.34,0,0,1,1.11-.54c.78,0,1.17.44,1.18,1.33V51.7h-.63V49.25a.85.85,0,0,0-.18-.59.73.73,0,0,0-.56-.19,1,1,0,0,0-.54.16,1.14,1.14,0,0,0-.37.44V51.7h-.63V48Z"/><path class="cls-8" d="M62.26,51.7V48.49h-.59V48h.59v-.38a1.28,1.28,0,0,1,.31-.92,1.25,1.25,0,0,1,.9-.32,1.67,1.67,0,0,1,.44.06l0,.51a1.79,1.79,0,0,0-.34,0,.61.61,0,0,0-.47.18.69.69,0,0,0-.17.51V48h.79v.49h-.79V51.7Z"/><path class="cls-8" d="M64.38,47a.39.39,0,0,1,.09-.26.36.36,0,1,1,0,.52A.39.39,0,0,1,64.38,47Zm.68,4.68h-.63V48h.63Z"/><path class="cls-8" d="M65.92,49.82a2.24,2.24,0,0,1,.4-1.38,1.38,1.38,0,0,1,2.12,0l0-.41h.58v3.61a1.47,1.47,0,0,1-.43,1.13,1.54,1.54,0,0,1-1.14.42A1.92,1.92,0,0,1,66.7,53a1.4,1.4,0,0,1-.59-.47l.33-.38a1.24,1.24,0,0,0,1,.5,1,1,0,0,0,.72-.26,1,1,0,0,0,.26-.73v-.32a1.38,1.38,0,0,1-2.09-.08A2.36,2.36,0,0,1,65.92,49.82Zm.64.07a1.69,1.69,0,0,0,.25,1,.87.87,0,0,0,.72.35.93.93,0,0,0,.88-.54V49a.93.93,0,0,0-.87-.53.83.83,0,0,0-.72.36A1.82,1.82,0,0,0,66.56,49.89Z"/><g class="cls-3"><path class="cls-9" d="M109,58.7H46.74a3.5,3.5,0,0,1-3.5-3.5v-45a3.5,3.5,0,0,1,3.5-3.5H109a3.5,3.5,0,0,1,3.5,3.5v45a3.5,3.5,0,0,1-3.5,3.5M46.74,7.7a2.5,2.5,0,0,0-2.5,2.5v45a2.51,2.51,0,0,0,2.5,2.5H109a2.51,2.51,0,0,0,2.5-2.5v-45A2.5,2.5,0,0,0,109,7.7Z"/><path class="cls-10" d="M172,28.4h0a1.65,1.65,0,0,1,0-3.3h1.49a3.05,3.05,0,0,0-5.47.65h-9.6a1,1,0,0,0,0,2H168a3.07,3.07,0,0,0,2.89,2.07,3,3,0,0,0,2.58-1.43"/><polyline class="cls-10" points="165.41 35.55 158.82 38.61 161.01 38.61 161.01 41.19 169.8 41.19 169.8 38.61 171.99 38.61"/><path class="cls-9" d="M198.37,32.7c0,1.82-.87.7-1.23,2.21s.91,1,0,2.53-1.14.22-2.18,1.29.25,1.36-1.29,2.18-1-.39-2.53,0-.43,1.24-2.21,1.24-.78-.81-2.21-1.24-1,.87-2.54,0-.19-1.08-1.27-2.16-1.25.19-2.2-1.31.21-1.13,0-2.53-1.24-.38-1.24-2.21,1-.69,1.24-2.21-.88-.94,0-2.54,1.07-.27,2.18-1.29-.21-1.27,1.29-2.18,1.09.37,2.54,0,.46-1.24,2.21-1.24.71.79,2.21,1.24.92-.89,2.53,0,.16,1.17,1.29,2.18,1.3-.36,2.18,1.29-.31,1,0,2.54,1.23.38,1.23,2.21"/></g><path class="cls-8" d="M49.63,60.7v-5H51a2.3,2.3,0,0,1,1.15.28,2,2,0,0,1,.77.82,2.64,2.64,0,0,1,.27,1.22v.31A2.7,2.7,0,0,1,53,59.6a1.91,1.91,0,0,1-.78.81A2.31,2.31,0,0,1,51,60.7Zm.66-4.44v3.91H51a1.48,1.48,0,0,0,1.18-.48,1.94,1.94,0,0,0,.42-1.34v-.29a2,2,0,0,0-.4-1.32,1.43,1.43,0,0,0-1.12-.48Z"/><path class="cls-8" d="M55.66,60.77a1.6,1.6,0,0,1-1.22-.49A1.82,1.82,0,0,1,54,59v-.12a2.21,2.21,0,0,1,.21-1,1.64,1.64,0,0,1,.59-.68,1.51,1.51,0,0,1,.82-.24,1.36,1.36,0,0,1,1.12.47,2,2,0,0,1,.4,1.36V59H54.6a1.31,1.31,0,0,0,.32.89,1,1,0,0,0,.77.33,1.09,1.09,0,0,0,.57-.13,1.4,1.4,0,0,0,.41-.36l.38.3A1.56,1.56,0,0,1,55.66,60.77Zm-.08-3.31a.84.84,0,0,0-.64.27,1.33,1.33,0,0,0-.32.78h1.85v0a1.27,1.27,0,0,0-.26-.75A.79.79,0,0,0,55.58,57.46Z"/><path class="cls-8" d="M59.05,59.84,60,57h.64l-1.32,3.7h-.48L57.47,57h.64Z"/><path class="cls-8" d="M61.23,56a.39.39,0,0,1,.09-.26.44.44,0,0,1,.56,0A.4.4,0,0,1,62,56a.38.38,0,0,1-.1.26.44.44,0,0,1-.56,0A.37.37,0,0,1,61.23,56Zm.68,4.68h-.63V57h.63Z"/><path class="cls-8" d="M64.41,60.25a.9.9,0,0,0,.59-.2.73.73,0,0,0,.28-.51h.6a1.26,1.26,0,0,1-.22.6,1.51,1.51,0,0,1-.54.46,1.61,1.61,0,0,1-.71.17,1.55,1.55,0,0,1-1.21-.5,2.06,2.06,0,0,1-.44-1.38v-.11a2.12,2.12,0,0,1,.2-1,1.45,1.45,0,0,1,.57-.65,1.53,1.53,0,0,1,.87-.23,1.49,1.49,0,0,1,1,.37,1.36,1.36,0,0,1,.44,1h-.6a.88.88,0,0,0-.27-.59.84.84,0,0,0-.61-.23.86.86,0,0,0-.74.34,1.62,1.62,0,0,0-.27,1v.11a1.64,1.64,0,0,0,.26,1A.9.9,0,0,0,64.41,60.25Z"/><path class="cls-8" d="M68.12,60.77a1.6,1.6,0,0,1-1.22-.49A1.81,1.81,0,0,1,66.43,59v-.12a2.21,2.21,0,0,1,.21-1,1.62,1.62,0,0,1,.58-.68,1.53,1.53,0,0,1,.82-.24,1.36,1.36,0,0,1,1.12.47,2,2,0,0,1,.4,1.36V59h-2.5a1.31,1.31,0,0,0,.32.89,1,1,0,0,0,.77.33,1.09,1.09,0,0,0,.57-.13,1.4,1.4,0,0,0,.41-.36l.39.3A1.57,1.57,0,0,1,68.12,60.77ZM68,57.46a.85.85,0,0,0-.64.27,1.39,1.39,0,0,0-.32.78h1.85v0a1.21,1.21,0,0,0-.26-.75A.77.77,0,0,0,68,57.46Z"/><path class="cls-8" d="M52,12.91H49.1v-.55H52Zm0,1.42H49.1v-.55H52Z"/><path class="cls-8" d="M55.79,12.91H52.94v-.55h2.85Zm0,1.42H52.94v-.55h2.85Z"/><path class="cls-8" d="M59.64,12.91H56.78v-.55h2.86Zm0,1.42H56.78v-.55h2.86Z"/><path class="cls-8" d="M65.92,10.72V14.1a1.57,1.57,0,0,1-.44,1.15,1.79,1.79,0,0,1-1.19.51h-.18a1.83,1.83,0,0,1-1.3-.44,1.57,1.57,0,0,1-.49-1.21V10.72H63v3.37a1.14,1.14,0,0,0,.3.84,1.12,1.12,0,0,0,.84.3,1,1,0,0,0,1.15-1.14V10.72Z"/><path class="cls-8" d="M69,14.71a.44.44,0,0,0-.19-.39,1.84,1.84,0,0,0-.67-.25,3,3,0,0,1-.77-.25.94.94,0,0,1-.41-.34.82.82,0,0,1-.14-.47,1,1,0,0,1,.39-.77,1.48,1.48,0,0,1,1-.31,1.58,1.58,0,0,1,1,.32,1,1,0,0,1,.39.83H69a.54.54,0,0,0-.22-.44.78.78,0,0,0-.55-.19.87.87,0,0,0-.54.15.47.47,0,0,0-.2.39.4.4,0,0,0,.18.35,2.46,2.46,0,0,0,.66.22,3.48,3.48,0,0,1,.77.25,1.12,1.12,0,0,1,.43.36.8.8,0,0,1,.14.5.94.94,0,0,1-.39.79,1.68,1.68,0,0,1-1,.3,2,2,0,0,1-.79-.15,1.36,1.36,0,0,1-.53-.44,1.06,1.06,0,0,1-.2-.61h.64a.63.63,0,0,0,.25.5,1,1,0,0,0,.63.19,1,1,0,0,0,.57-.15A.44.44,0,0,0,69,14.71Z"/><path class="cls-8" d="M72,15.76a1.6,1.6,0,0,1-1.22-.49A1.81,1.81,0,0,1,70.31,14v-.12a2.24,2.24,0,0,1,.21-1,1.63,1.63,0,0,1,.59-.68,1.47,1.47,0,0,1,.81-.24A1.39,1.39,0,0,1,73,12.4a2,2,0,0,1,.4,1.36V14h-2.5a1.28,1.28,0,0,0,.32.88,1,1,0,0,0,.78.34,1.08,1.08,0,0,0,.56-.14,1.4,1.4,0,0,0,.41-.36l.39.3A1.57,1.57,0,0,1,72,15.76Zm-.08-3.31a.83.83,0,0,0-.64.28,1.33,1.33,0,0,0-.32.78h1.85v0a1.21,1.21,0,0,0-.26-.75A.8.8,0,0,0,71.92,12.45Z"/><path class="cls-8" d="M76,12.56l-.31,0a.84.84,0,0,0-.84.53v2.62h-.63V12h.61v.42a1,1,0,0,1,.88-.49A.52.52,0,0,1,76,12Z"/><path class="cls-8" d="M77.14,12l0,.46a1.37,1.37,0,0,1,1.11-.53c.78,0,1.18.44,1.18,1.32v2.44h-.63V13.25a.82.82,0,0,0-.18-.59.73.73,0,0,0-.56-.2.89.89,0,0,0-.54.17,1,1,0,0,0-.36.43v2.63h-.64V12Z"/><path class="cls-8" d="M82.69,15.69a1.11,1.11,0,0,1-.09-.39,1.38,1.38,0,0,1-1,.46,1.28,1.28,0,0,1-.9-.31,1,1,0,0,1-.35-.78,1.06,1.06,0,0,1,.44-.9A2.08,2.08,0,0,1,82,13.45h.61v-.29a.72.72,0,0,0-.2-.53.8.8,0,0,0-.58-.19.88.88,0,0,0-.57.17A.5.5,0,0,0,81,13h-.63a.86.86,0,0,1,.19-.53,1.26,1.26,0,0,1,.54-.41,1.78,1.78,0,0,1,.74-.15,1.43,1.43,0,0,1,1,.32,1.14,1.14,0,0,1,.37.88v1.7a2.21,2.21,0,0,0,.13.81v0Zm-1-.48a1.09,1.09,0,0,0,.56-.15.94.94,0,0,0,.39-.4V13.9H82.1c-.78,0-1.17.23-1.17.68a.6.6,0,0,0,.2.47A.76.76,0,0,0,81.64,15.21Z"/><path class="cls-8" d="M84.81,12l0,.41a1.35,1.35,0,0,1,1.09-.48,1.07,1.07,0,0,1,1.06.59,1.33,1.33,0,0,1,.48-.43,1.42,1.42,0,0,1,.7-.16c.81,0,1.22.43,1.24,1.29v2.47h-.64V13.25a.85.85,0,0,0-.18-.59.8.8,0,0,0-.61-.2.83.83,0,0,0-.58.21.81.81,0,0,0-.27.57v2.45h-.64V13.27a.71.71,0,0,0-.79-.81.86.86,0,0,0-.85.53v2.7h-.63V12Z"/><path class="cls-8" d="M91.88,15.76a1.61,1.61,0,0,1-1.22-.49A1.85,1.85,0,0,1,90.19,14v-.12a2.24,2.24,0,0,1,.21-1,1.63,1.63,0,0,1,.59-.68,1.48,1.48,0,0,1,.82-.24,1.41,1.41,0,0,1,1.12.47,2.1,2.1,0,0,1,.4,1.36V14H90.82a1.33,1.33,0,0,0,.32.88,1,1,0,0,0,.78.34,1.15,1.15,0,0,0,.57-.14,1.37,1.37,0,0,0,.4-.36l.39.3A1.57,1.57,0,0,1,91.88,15.76Zm-.07-3.31a.85.85,0,0,0-.65.28,1.33,1.33,0,0,0-.32.78h1.85v0a1.15,1.15,0,0,0-.26-.75A.79.79,0,0,0,91.81,12.45Z"/><path class="cls-8" d="M98.68,12.91H95.83v-.55h2.85Zm0,1.42H95.83v-.55h2.85Z"/><path class="cls-8" d="M102.52,12.91H99.67v-.55h2.85Zm0,1.42H99.67v-.55h2.85Z"/><path class="cls-8" d="M106.37,12.91h-2.85v-.55h2.85Zm0,1.42h-2.85v-.55h2.85Z"/></g></g><g id="Fingers"><image class="cls-11" width="237" height="268" transform="translate(124.94 4.81) scale(0.24)" xlink:href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAO0AAAEMCAYAAAAoIjEcAAAACXBIWXMAAC4jAAAuIwF4pT92AAAgAElEQVR4Xu2d63bjuK6EIad7v//zzunE50ca7XK5CqB8lRzWWlgEL5IoEp/BOOmZ5Xg8xtTU1H506AZMTU1tSxPaqamdaUI7NbUzTWinpnamCe3U1M40oZ2a2pkmtFNTO9OEdmpqZ5rQTk3tTBPaqamdaUI7NbUzTWinpnamCe3U1M40oZ2a2pkmtFNTO9OEdmpqZ5rQTk3tTBPaqamdaUI7NbUzTWinpnamCe3U1M40oZ2a2pkmtFNTO9OEdmpqZ5rQTk3tTL+6AVNTo1qWZeG24/xfWNxdy1zTqTVSYF6rCfR1mtBOlbonpJ0mxGOa0E5d6ApQR8avCrQJsNeEdioihkEdGbNWbQBOgM81of3hGoC1648YGzMSaOWYCe+3JrQ/VA2srm8EzjWqgs/2/XR4J7Q/UAWwqp3b7gWuCrzRth8N7oT2B2kFrGvr14gDb239u/EHBvCE9ofIAFvB6HxVd31rjr9Yd76q/zhwJ7RvrjvBWgHs2lgdfEcqR/1T4w8J5gntG2sA2M53JftV29qMWsHbgf8jwJ3QvqlWANvBOjKO21FdRl1bVv53w5sH9YT2DSWAvSajVuDeC9oK0A7eHwvu/Fc+b6ZBYLmtgvUaeFkKMAbzGN/3yTb0UzimG/u2mpn2jbQS2A7OkTZVskaBReN2V8eS/bfNtjPT/gyNAKusG8P3UlKQVcBif6djfD83x6Mfy7Is7wjuhPZNVGRZByr6zg5NP9/XaQTSzvh+C/kS3HfUhPYNdAWwqs6AdvVRcEeB/TJtThW4//SO2XZC+34aAdbZgUrX1sGbOopSAfoVJ+i+oDyAr8TZlcvvzjcDd0K7c1GWZWhGgWUwD6atgjegTCloGUaELOFNSNfAewaqqL+NJrQ71uA/ALgF1oNpc/dTclk2YcQSgXXwjmbdM71Ttp3Qvo842ymQHLAVrMrw+hFo2b7iHN4EFg3hZLAr2WPyu2hCu1M1f6aIfSojjgL6UfQpcJU6YD/pHu4+CSxmWwWkBfVdsu2E9j3EkGZZWQfph2hz8CJsWfKxmI/GmGEZXrwPC7OtGsPHZAvxXjWh3aEG/zHAGlgZUud30PK8VJbFDIvQLnECd0R8VEYw3w5U1IR2/2JYuQ9hdfAypMpGwUVVwB6ozOs/QyuzpvqQOMb5s222fYcj8oR2Z1qZZbk+kmE/4jsu1sDbQcvHYgesU94nffWO2Zf6B+q7aUK7bzGs3KfMgcuw/hJtDtwRaNHyug5YPl4f/16XfYso8dq31IR2R7ohy3JWZFjZfoGNgLsG2sywDDzrGN/3Tx+NP4gCSoaVwd79EXlCu18xrOg7G8myv4zxuGugdcC669I/QNuR2hhKda+30oR2J1qRZdFnYBlchE8B+zvOoXUZt4Mvgf34W/6h61gM5we1qYx7lk3fWRPafYphRV+BOwIsQ/s7xsDFe0ecns9ZNoHN5/+BsSm8xmXW/FWPMgfuW0E9od2BzD8KGIGVwXVHYz4eM7AVuHzUTTG0CCyP5WvwWpzvF5T5Ti7j8n3PtOefaye0G1fxjwIixsA9kM+wMrAq0/6mvrXQ8tHYjWVg+dtmBS6vT4L7tprQblgC2IXK9BWsCOxB+CrTsv2OS2h/w/i8h4NWHY1xfjlOwZrjP+IEas5fgZv2NsdgpwntRjUALAdrBS5Cyn4FLkPLx+Q0/ICIuISQj8Ypl1kzM2OmRWDVO6ccsG8D9IR2gyqAdfVsY1gVvHisrY7IfDx2R2SEkYHk4y3PG4H9FZdH6QOZ+4BC/wh15e9eE9qNqQGWfWeYmZR1P9OqL6K4bSTTKmjVmAQ276e+tFpEnSFOJaT4rAvt9cuoCe0GVHzZpIDlIOWgRmAVuJxlGdgKXHVE7oBUf6qI/XkMVh8uPP8KVmzbHYhrNKF9sppvg1EdsCqA2Spwq59lRzJuB607GmMfZlY8tit4HbAM79trQvtgrYA04jL4VCZBv4JVmTsWV/D+Jss2vA6hjNCZVvXxPdYAy7CuWedda0J7R60ENMIHmgrGewCrAEZAq6zL2Xc002KbyrLXwIpSbdn+lsfkCe2VuiOgrt+By4AqULEN4eBMq7Isg+u+jOoybWZZFLarDxN8pwrWCuC314R2UCshHRnrsoOqL8JXQe4gHgFWZVn15ZPKtAhRZlQGK7Mr//zK8+V3Ue9eCefxlprQGt0ZUtffgasCFq2ClEF18P4S5YjhPRgm/AOIY5yey19MMagOUr5/t95OOZ9dQz2h/asVkI6M62B07cp3QeyAZUgdqAhfBSaPYdjzGSic80ecjsUMrILVgRpF24/Sj4Z2ENRuzAiMru1aYBW0VTZV0FXwKt/dh6HlP2rI+iisqW7dr9GRyl3qx0E7AOo1/SNtjwRWZVkFrgO1yrYq+6IhhBHfGfUIxn87rMBFqbYp0I+A9kZQR4BUbR2Uzu+gVQAwqOoYW2XMDmTXhnNILXEOrsqsASX7nThLqvquM2mnt4X2BlDXAtnVKzBVmwKVjX82RGgdcCpjjmZVBpczPL4P/yschjXA7/aI1R1v3xrW1NtB28A6AqRqWwul89eU7B/Id0fjERh/hf5XOx28bHw0zsyavgK405HsWt1y7ab1NtDeCOutkK5tc3Bim4MWSwVsBy3//bD7J3cOVszsCC1CUkGKbZw5FWgMMJY3gbnHf+ET8SbQDv4rma6+xh8FsisrX5kCtoOW/2541Pg+Clg8Gi9xyq4ofLeIHkKVaSu475GVd6VdQ3slrGv8UUhHAFVj2Vd1PhZnicAiuAgcZ1RlLttWmVZBm9AsZCgHGwPatQf5qLeHd7fQGmC5TcGGfgejK69pq3wOcqxXx2KVaRW0ClSEucq01dH4EGNysFWgOnjxOrw2TFldu0vtDtobYB0FdLRv1O/6RqwCVkHLUFZWwdtl2nyf1DHO31MBw/Zl/FHDe6O6+m61K2gHgK18BMaVHWSj41S9a2frjsUKWAbXZdoKXoQV/ZEsu4RWB+taCyrfBsgR7QbaFcC6tlHftY2MGe0bMXUszhIBqqB1wP7PtHeZlrNsvqfKemvsGoADyvR/BMC7gPYKYBka56O59tH+0esOocepfgYV/RFoq0zL4KojsoIV5xLRQ1JB+kU+tq0FGdXNabe/7onYAbQNsNjHgKCv6q8yBS23uezKpsDlbInQpv8/Kh2wnG1Vlk1lHbOgAxVL1zYCMEq1vaU2D63QMlAupr4WppG+a/qrugI2yw5YBK2C1mXa6nissmzKATQCrsqwt2TaI5Sub9faNLQiyy4D5aiNgHNtfWTMKKhZjkJbZVuE1pmCNp+Tc0lVEDhYO3/UgnwUt70FrKnNQntnYB0wI+B0bWv90f6D8BnYNdA6cDkTc4ZFcHOurGxzUClwqww7mnFTqu1ttVloSUtRsr8Gng6Uqm0Eumv7HKxsnAnd8fgjzqF0Xz6ln9fnfXFOS1wCw6pgdH0K6CO1j4DagrvnL6EiNgotZVn0sb4I/xYguK2qV/e8V1nN9UOULtsywApSBhyzLc8t4gSug8hZB68DtbIQ9Wx7S20O2sG/J2a/gtUFvrKRcfeCuevr5sPAos/wMZjKGFbMsDkX1BHaKng7UKuMfCR/FM4jlW7cLrU5aEmLKNnvgO2Mg3OkT93ffUiMQl351fy6bFvBq8bg/XAuCG0CW8HKwHVHYVVX91Twso96G1hTm4LWHIu5TF+Zg4jh+xC+CtYKaLbq+Vxf6ztjYNHnrOkg5XH8zgxshAeBAXW+y6yu7IBNvR2gSpuBdvAfsTtQuwBnEBWoLsushdjNZQTODnxlClhnDmT13vl8hvZo2pRVcHbgdrAG+T9Gm4GWtFCZvrMqwLug7tpVeY2NgHottFyusQP5+GyEEzMb7ktKAVvB6yA+kt/Bq2B+a20C2sEsi3WGVYG7JojVEVEFNAY2B3ln14K6Btz01fyrupor2tGUKc5+DOsxNKBdplXwohSobw/xJqAlLVSmj5/6DK4LYgem8h24DmAX8M4qGNdAXBmDWJVu7rzWESdQ01fAVrCugfRoLFVB+bagol4O7UCWdVYFLQZm9QXMmi9n7g3uWl/V2dy8GNpqfvzhOJK1XGassqwCWt3DwRum7e31cmhJC5WqvwMYIXOAKnMgV/COgMBQ3NtXpubk5rlAqYDN8gvqKAWWAnAETq7zM9jHflbO+7JjWZY9/1XU1qBFOUArYDM4GdzK+G9uGWS8D9+/AkTNTYHXganGqfqouWcwsBHngGA/92FdATgCbGX4DOWneH5Wewb3pdA2v5c9GyqMg5FBGoFU/f2tglZl3YMocS4VtCNwjoxhv2pz96mAXeIbLmxndcC5I7PrT5AYWBbHjhubfRdj9gruS6Et5IKpC9ZDXMKFAKt/1cL/wkVlXoYXn3OA0pmbdwfs0vS5+3T9fN+AMpXQHOIcXBw3Amzlq2wbUKZfAXkBI/Vj38XYPYK7FWhd4GSbMg6+hEfBqoBV/46Uyw9RumzLPoPTwVlBOtrWley7dc/M5GBlVcB24FbAOqm5qLa812L874adgfsyaJt/GKCCCk0BoYBV4Kap/7gZZ1o0l20VrA7cNUAxXCPjOsiVpZY4ByfBdWLYuE0BjD6Or3wUzhlLnDsr+3DMxfg9gfsyaIVUgFTB5iCpMq0CduQ/cOayLQObPs5P+QyWgkvBNtLWjQnhpxiWJU4Bj9ewGNDqS6YgP+soN1fszxLnp4TAZhnkfzfsBNwtQIuLzcGm2hSkCliE1h2N+T9wVoE7Ci3PcREl+6ru2pSNjlviW1xGnAd1wofXoBi+tRbkO+E81Tuod1J6K3BfAm3zBxWoLgA7WCtw/xceWgaX74nAuqPxUpTsV223Wpg6ioMZr3Fy4GI/Q4rtSvg8niu+wyFOc3bvxGJwQ/gREf/ic6vwvgRakFvwKuhy09gYXD4eq0xbZVt3RHaZlrPsUpSLqbNF0z8yNoTPUsCpa7OPfYZTgYolq3uHQ5wyfwJ7gOuzb434gwr9TevV0KJUoHHJQFTwMnAOWs66HbS/6Dn4XDXHRfiqLUR/18ftalxAyT4G6RLn3xYjuNmWUmBiu+tnufflPf6KE6xH8HF8xGn+Tggql0H+Zo/KT4dWHI25jm3VpipQu0yr4O2+lKqgxVLB2kGrLJo27nd9Icr0OUixzHa8JuIcRGzDPldPde/Oa4hWfRgk1Nlewbt7cJ8OLYgDif1qY3mTGV6GLEF1wHKm/R9dg/dTR2M2NVeuB/Wp9mt9LNnHOgYsB++oHMid+L0drCPQYh2z8jWZN+K6dXiaXgktqwpmlcEYVJdpFbgOYs62KtMyuArYClz3ntH4VVtVprCOAYmBmqXyWWuDWq1BmgMV91gJ74GAJrAj8Dpw/2lr2fap0K48GqePG1ttcAcsH40VsGwVtAcoHbBcD+pTcKiy6sOy8lEyOKnNXTsqfk9eE7eHX39Lzqys6t0SUobX3VOBe7ZGWwL3qdCCuiBTAb1m4/mYrEyB+duU+AFQHY0XKCsL4VdtqZE+9pUyKFVbd22nbu/Ufn2C7/68keWewRk3yzVH5RTXN6FXQcvqNtptuAKV6x28KvtyicB2R+OFfPVeIfwUt1V9lZ91F3QILgcs32dUbg/xA00Bi7AytErL3+uwVJagrjkqR5h120q2fRq0K47GIzYCL8Jagat+zuU6Q3uAEgMSS7QQflV2bZXPbRyADKsaM6JqLrxXas8S1F9RZ1ZevyVOv5dV4DolsIfQ2TiVa8HlZvQ0aEGjgac2vwNVgYvAdRmXTV3PwCK4GKQR5/MP4aeUr9ZD+arOyn6VUdHv7sNS78brgHuHe/JF5oBV90VIGVy8DoXAVmtZgrqFbPsKaFlu47nuNtABzBnSgesysvLxw4GBxSB17xFQos+BUwVVV3fi7MFtKXU/fh/X5/Yn1+0T/LWw5v3UcRjBzevxXqkEFrOteif+UOM1eqmeAu3g3xrzQneBUAHrzGXPql8Bi+Auoow4zTeKsvJH6l17xFgAurbqeaN7o2D9FeewVtDi2uKasyGwCl4UZttu7S7W5tXZ9inQgtxCYTv7Lhg4MBhe9BE6B2xlB1FyEGEwhfCxZH+k3rU75fjqaMzq5qmM4cq1wy+aENYuu/K6qvVWACewI0J41VqMrtdT9WxoUbjQQeWIKXAZVmUK1F+mvQNXBVeEfy8U1rmva+/6Unzs7Y7GTrz23KbAwn1Y+7PrISL+mFJ9SDK8TpjZ8Vr+OZfHj67TU/RwaAePxikVELyZnY2Aq4Dka7r7q+DhoFYl+1XbSF+lvK4KOAxIDnr33G5vEFSVXfnDhO/jgM1SrXtAqYRzOEB7AuvWitfnGBEvPSI/HFohF7C8Adx+IF9BNALswfhYV2MQVDengHpAyb6qd+2sLkCVMAC7PnyHyg7GEFyVYd19OmD/wHg1Hyf1wcHX4kkEr9uUngmtC2AVzNcEiAOWxzjIVYmgqueq4AlRso+qAi01MgaV46893qnnuf3gtUlYjzEGa16Px99PKhWw6fPaoxDQj7jMtgpcvA6Va7h2Le+uZ0LL4iB3dQRkET4HjGqroHagKuPnqw13ZUoFF2tkzC3C+7tAdO/IxmvNsDK0fG+EkmHNkn0GlsXPznkdqD3reC+1Hmp9XnZEfii0gz/PqqCugoMDhc1BeQB/BFB+1lKUGDxcss8aWSMWX+MCB4NNBh6JIaj2Qa17wsDQ8r1w/RBYB2+OU/NhMbAIKGdbBjYt2/Gem9FDoRXiRcYAH7UqaKq+6iisjsNL4WPA4Dtxmwqqqt2pG5/9I8GVQcl1bOf3wzXIvyxy64ygptweIqSfwscjs9ofJQctwpsfLDwvNLWWaq2ermdBWwW2GucWkiFSQeMCSvV346tNxcDherah1PsqjY5TUsF0S4Cp9zvEJbgIa/p4D7WPaQmpAvgQ5+CqtUcxoPklGO9rtuFYFq+bXMdXHJGfBS2Lg5sB4HbctAqyDKDqiKyMn4HPVUEXpi3bUSq41vQ/QxmQ6l2VZcDneitYU+paZwxwWvczbMQ5pMp4r0cyLT7rqWBWehi0d/55dmTDO6uOw7mZi6mruQSU7Kv6aN+tyoBbK7yO31HtAx41P0Kr27+POIHKwDK4OKcUZ9VfcQ5qZuyPOEF6CA8s6tp1fLgeBu0KqcXrTEF2jal7qGeoDV2MjyXLtb9KHJj5LgwvrklCkjAouT1TwKp94V/xqHV1wCag+OeTfERW+8rz3SSwEc+B1gVyVe82fTH+taaeV9laXXPNLXJBh+3p59wcqLj+mF3zmmP4Z+G1DCiClABjdnVH4iMZA5v3wg8FnEe1p7xPah1x3V4C9jOgRalFcnVcaF7sDkIMBncUdr7bzGqeIcoU118hDjCuZ1vEKSDdXiS4OdYB+wnXJaAI7pfwFyh5fVMKVgQWwXX7m37E5XOw/hIoOz0b2kouUFTgoL/W1D34fipouBzRmrFbUQZrtf4pzM5ZLnECNks8oro/nFD7kWJQ00dYR/ad95Ofsws9BNorvoRi3wXLofCrjRoZw5bijeY2bt+T1HzxyMzr3wnHM7Bpiyh5L1h8HFawVuC6PVbvyVqiybjP/rXPQ6AdkAp+tWhqkSsAOzjVJo5sLM8zpTZ5pO8ZcsHWBWHOG7PtIc6/cWWA3XoxsAjrIc7BVusbcQ5qwopH6+o3Ad1eBvlOOOZpcDo9C9pukboFPlCJ7WtMXcfPcJsbou7a9qAlLn/ODWjLOgKbsH6Bz+r2cvl7PR6JP8V9OLMitHi0ruKj28td7uejocUF4EXqFpMNN6b6RHWwdtfhXJTPc2d1/a/WEj7zRlzCymMSXgdurhFmZLU3ClZ8Zs7jK86hVaB2+8mq+pTcmr1Uj4Z2VG7RO3OALlTvQHWbzZuL/dy3Jy1xOv6qbMvKdgYXr0XoHbg4hp+Vv/PNDMvHYN5bt2/q3tdqc8BGPADaO3wJhT5bt3EVvOpTWj3D2R61xCWUI9kW29hHcBng5W9b1vPatC9oYyWsaz5sw7Sl9rpvpe4O7QqphUffmYKvAlVdr+6VWhMAC5Vu3Ba1xGW2xbljWwKaQmBz3DHOr8EvnZTwOvwQ6PYf1a21+oDqsqe7Bt/vpXoFtNXCdxuGVmVaNa771FZBEabtHbVEDy8KQU54OQO7L6wyo+aHhgM24vK5XD8aUzqK8mYQn/nrnojnQFuBgCWOY9+Zy7QL1R24I88IKvnarWuJ88DEevpYBvmVEFasB5QMLgPr1twJ34X9zngcX6v0VCBH9EhoGQrXhmJQrjEEeDS78nOVXPu7aIlLmNPvxPDiWnbH3k4diPncbswIqJsDVOmR0LIqGHgDO7icuSNzd11qgVL1oxYq2d+SljgPSKy7vnwX9DvlOAQ129V6qXoHXUKKdg3IKQWuAhr7sXy61M8br5SDCPseaQElSrXtXdV7XrMHUfh4PQshWAPqWuvur0B9GZiVXg1tFxzo39uUFirfSdU7jawHj+E2rLv7OSgeBanyK4CD/E3qrtCu+B0tb7ALDgVZByNbCN/dB+Xa3knqfdQ6cb/aD6xXcnAqUPG/aMF1Z3gt3nckwyKsmwX3rtDeUR1EI4AqGF0gYr8DdeTaPaubv1obJRXsLpOir4BT8HbAqmtVJs7npxS4WbfZ99m/7onYLrSpCjw31rUr+ByII8G5R42+V/cB1anKaCqbVnD+oXLUKlBHM64CWLU/VVuCtgsUhoyNxymI1TO65ypdc81WpdZirTCY2ccjKvuYHRWsDOwfMge4g5fnMQLu5vRsaLugUFlwVNU119wPdcu1e9LaQFWQIqhYX5NZR4zHjmZbnhO+Q0p9CG1Gj4J2NBN1/ddqJHu4THzLB8fWpQKwCkrsqzKSMgWMyqwui7L9X9GnsuwX+RW87r1Sco1e8fNsxOOgvbc6CEePu+8I4iPUBmz0sDK4DNIf8kdgdX6XaRlcN3cGF6Vgfon2Au295DbkJ6gKRNXPfZUxEC6rjgBaWQduB6/LtgxrBe/LtRdoq+By/d2Cq01RG/fTpGBFP6FEWBlczHDdUZih5HYHs4LeHZMdqFwPKFMy9l51NI54PbSPevFrIK50y7VbkJp/tUb8gXUU9kW+A7XKrpw9FZz/FeMcuM66LFu9/2b0KGhHPrVuVbfQ2YYlt1djKl1zzZZUvb9aUzQHa5VZEVwH6H9Q/lf0d1kW69WxuAM3Cv+lehS016oDcBRCNVa1j9xvVNdc82i5dVS+6kvjQO9g7bJsB24Fr7Iuy44AG6KebWd65dE4YlvQKoCqRawWXPVh6cTPyjZVbl1qntesYwXsKKwK0v+odLBW8I4cj7+gHDkap9RabUJbghblFrFa4K7dBWV3LbftQWqeKgi7NemAdUfiDli2/2IdrHhPdUR2wPI7uLhIXazjq7NsxHP/ETxKLVbE5SLxQnZBxlaNVXLz2JPU3FUgqvXJOgY0BzxC4ID9jHOgFKQMK1sF+S3A4vsyuCm1XpvRXaE9Ho/HgX+ed4zTHzh0wZQlB9VaS7GvxqlNwjlvVW7ezu/WU2Uml2URmi7LKmBVxu0gHj0aq8xavX/qYj23kGUj7gztHcTgdJDdy/AZWaIpYLPd9T9T+A6qjX33nmkdsAkEgtIByz/D/mf8Cugqy1awVvCG8FNqXV+uLUDrFvBaq45DbCm3aahj9HCOjLm31Hz53Vyp1o5Ll13VkdhlV5dlXXZV13CWVdmW55Zzdu+p4gDLU8dGsmzE86DNF8aAdsE2Ely4+O7o8xWX43ijVD3l5reV7Brh58g+vy/61VoxrAjttUdilUlHj8QI7T2yLO9/gK/WdhN6JLQqwLlNBVPWsV0Zb0C3KZUFler5/A6vFq5XVVfvkz7DiuuIpjIYQ8uw/gl95B2FlrMsfzhck2Hd3gaUF9pSlo14LLROHPS4IG6R1xhnimtADihTx9gGrBF6bs4/kq/Wi8t7ZViVXRWkDuQqy96aYVG85//6twZsxGugdVIL6YKMM4TaGJVF2FcWUHY6xvOPyy7g0FelWke1hmhdhkWI3FFWgVllWwfs2izLcVHte4hys3oltG7BKqvAxODr7uM2LsDn/lE4R8ZcK5wn14+iVO+iPsAYVC4RDpVhMcsycGtBdcAyuNWRWH2wj+z5mbaYZSMeAO0Nv6t1sKi2aiM4CN1Gqo3juVTCd3iGeE4q6Hi90K9gPcZ5hqqy69oj8Qi4DtYKWARX7XcXIwFl6l99q8BGPADaK1XB4hYdN0ZtGI/p7lNZ/C3xy7MtAst+tRa8bgjrV+js+hnnACnIKmhHj8JrgVXg4nu6/VTl5vVMaDnYq0UcNbUhI5+2DmKnY/SQ4piR8aPieWGd1wx9984c0Oo4rGBV2VUdiV0GdRmW/T/k3xPY1NGU35UNZ9mIx0ObwdsFdBdw19gIvGF8HpM6hp77vQBlqeez382f14BNwdodiRmuDto1GVZl1zXAqjVwa4Xld2XjwEY8HlonF+gqSF0gcuboNm2NobB9DZxrx7PUPNg/Cp/XiUsH61ecQ8HQcHZFq7LrKKwI7S3AcunW6kJ7ADbiddCm1EI6iKqg5DZu56BV93LGyjb1bTLXr1H1TPSrtfkiX5k7Dl8LbAdpBS3fn0FdCyzvH/sptdab10OgveM3yDh2rfGGjliq8tUxH32Ua3fCZ6m2I5Ts43tz2cHK2TV9BdQIsA5cZ/gMl13XApvitcL2U2UnWTbiQdBeKbewz7AU1pU/AiCPG7kO5+Daq3mlVcBy0KvsiuDeCqwqR2C9B7Bqf9Vafld2BGzE86HNxeGg5kWrNkDZSFblvm48W5DPWfYYHk6+htuVsE89370fA/tJvsquCCtCew9gFbTqQ4EzPRvD+iOBjXgOtCqoXaDjQru2aoNGNnHUWGquERpUHovtndT7Z8k+v7MD1mVXBeva7NoBq0xlWJVdJ7BCz4DWyUGQPsNTbY4K4i+qd3gP2q4AAAyqSURBVNd0zwvy+edx9cGE40aEz8e6mgO/WwVs+h2szwJWZViGlk8JE9i/eiW0o6o2pjMHb7fhLgAWKiPGTg84TukYl8Lnsu/exwGLxpmNQR0FtmtTsCK0XYbld1H72e1X6mx99wxsxDagVUHp/HuY2nT+BP+K7/9SpbqegWVfAR3QxtexsD2fiT6/xyiwDCpn10cBy7Cm72B1WZb3Lv2ANqynztZ578BGvB7aDPL0sd35LogrU5/QI5/YziI8pNkW1I46xqWw7ShKNfdbgGWgFHCjx+BRYKsMy/MfAZbXJ6Bk/y2AjXggtIO/q1VyG8GbMWIMqwt2FxgH8BfoCygjfOZUH0jZ7gKI7z/6jqPActZzdguw6kPBwVplV7Vf+O4h/NTZ+r4LsBEPhPZKdYs/GsAMq9r4qj+BTVgX8LEv/2PvxzgBWgHpIFbvy0Hp5nkNsAwXgzcC7DXZlaHFOfPe8R5OYP9qK9CqReVgZcsxDkLcbBXoro7XcabFtoB2/tlVnTAqmIP6OChxTjxvB24HLNvIz6u3AFtlWJy/2jO39+inztb43YCNeA20uIjq50IltVnOOJi5zQU9m8q0qCUu/7cq+S7XioOQ30vNnQOfM20HbAfmvYBVGZbnz6BOYIVeAW0ntzlZ53Fukx2o7ij2Gd8QYslZFMVQ49iE9yjanNS7RVy+kwNXwVoBW0F5L2Cr7Or2gd91Akt6FrQqiN0453fGAY2+ChAMng/Rt/wtUzzvY3yDy9Diz7Z4gmAfpd7bvRu/F8PK0I4Cy7BWx2WGlYHlueBaO1j5HdlC+Cn03xrYiOdB63QMDbHbpM44qBWkCtjMrhWEEedzOUBZQZs+vqsLqupdXaAzvAgLwlSBew206v74gcEfKC7D8r65vQ1Rsv/2wEa8HlrU6MZUwYx1FSQcPBlkh9DQpnhOCGzCmNeGuAeX7Kv3S999EKksq0zB6oCtjsbK1PPwg6OCVUE7gR3QVqDNwOdFd5vIm67auwD/iBOwWboM+/G3zOck4DnvhfwOXvYjdHByUPOHkQKkg5bhvQZazrKcXdNXH5q4T/huzkKU7P8YYCO2AW0GO9Z5wypzoCpYK2D/hM6waIe/1+KzE3b0HbwR5/fPOgdj945dllWAdaCOQPtHlC67Vhn2CCX7IXxV/tNPAjZiG9BWqoKZA8BBWgGblsCy+JkJLF7L4C5xDm8IH0sUB60CFt+Ts9tolu0gdhlWZVcFrYMV94xhddBmHctTxw8DNmJb0KpNU6Y2HoOkglUBy9k1on72B13L90mQOeOOQBuhn3mMSxgQFgerApfhVG1c8j0Z2JEMexQlWwg/hf53ww8ENuLB0DZ/f3yMU+Cyz+M4gBFWzkAMLmZXBG7kSyd+Tv5q6BCX9+GyspT6sMjSvSe/2yisnD0VvApYvJ/LsiMZtoJVgWqB/amwph4KbaGEFGHl/sowCDCQK2AdrPhhgfbr7/2yzHsz+NeAG1Cmr4IW39O9HwPlwGVgK3gZZH7GJ5QVtPwOE9g76JnQOlCxnTdQmQL2A/wOWHUkds9JYD/AFLiL8Bfhj0AbcTkPl2U/4xJQlWUrYN04ByxDyx+aVXZNP+L8HUOU7E9g/+qZ0FZSICuIGFgVzBzYDhqUetYHlGiHuITWwVtl3YAShcFbZVp1LGYAqwzqvmhiQCtgVXZlaBlcB222YXnqmMD+01agTbmN/Yrv4FfAMriYWRUs7sOBAVFZ9kD+PcAN8FVAuw+nDloF8QiwFcAMrIKW1/IoLISfmsA22hK0xxjPthjECMwfKDtgw9w7gc2grDKtgpehdfCGKCP8eyMgCFAHXQVvBSjbCLAdrArUCexKvRJa3owl6o3ObMvAKnAdJCgMLpXNElyGtjsij8Drsi0GMn+YjGZa9XOq+kZYAesAVsAyrHcFdsLq9XBo6dc+xzgFp8p6I+Au4cHtMmuI+yEYXZYdybQOXgduxPk8MaDV/BhaBA7hVL/O6YBV2XUUWIQV/RA+luxPYBs9HNqVcuAmrBn4nH0UrArYiPN7Ohh+Qdn9TNuBu5DP8EZczpXf/ZZM27UrYD/J72CtsmyQn3UsTx0T2FZbgBY3CbMwbz4D7ICNuIQg6HqEgYPyA8o/MZ5pHbwMbZdtMaC7uTKwCChn3bXA8rMSWAXuKLAK3FPDBHZIr4Y2AeU6B+4CZdonlQoElIJfwZCwYpbFDDsC7Eecw9pBy/N1c3WZFuEd/ZbYHYmr7LoGWAbVAjthXaenQLvi59rsDxjTgZtjK3UQ5M+xCOtollXArs22EefvkGugMu1XXB5hFbRVdnXAusyqYJ3AvkhPgbaR2rQENvsrcBFelAMVAVBfOiWsv8JnWJdl3RFZgZv1iHNwcT0YWpdtMXNW4HbZtcqyCtIJ7Av0KmiPsT7bZpBke6cO2o84B5ezKmZahrU7GnfgcraNuHwnN3cFLWfbteB+ilJl1i67TmCfoKdBS0dkOaRoUwBG1PCOQJvgMrAK0EdC697DzZ0hU9mWgf1Dvsuw/MGwBtwoyn+awN6mp0ErdIxTsKLPY7JMUCtxEI1Ay1A6YFXpIHXgdtDiGrj5I1jqmKt+jlWwVsAqSDuLovyuTFjvoldCm0pgqw39iu8gd+CqYKmAxex6aHwGcTSzcjv/TMvQquNxlpjdGFqGV2XckQxb/Qyr4A0o0Z/APlhPhVYckRFYzLpKCW4GklIG1Af4mVUZ2PQVkKOAOmC5b6G+EWgj+g+eNeBiO4JbHYMZVAfuBPaJeiq0A0KIXb/KukcybDtAidcisAxvBWQFqhtzD2gZXASuA1cdixnYNfC69cbyuzKBvbueDu1Ats0y+1AIHd5DHS0REq5/ga/gXQPkiF0LbcQ5sAgug8fQKoA7cL/AryBFWIP8U+ME9iF6OrQREtx/XXEOrII3gU34gsYh/GgVRIcYA3YNmFV/BS1/oLExXAraCmDOziqjugzL4rZ/9Qns4/QSaIUQUKznxqOf4qybYGKJge7gcrCp9grM0fs4YB20WTK0ClyGkgHmMSrTjmZZnBuWE9gH62XQrjgmVwGQwHLQM7jZhqAzUGv9W+o450N8C9+B5aB1GRfhVNlVZVjOsh2sAf6E9Il6GbQRq8HtAI44hxjBXeIS2BzLMFXlLb4q2QLKFIKRUCFcn6JUkDpT4B7JD+FLzSz7eL0U2kYj4GabM+xngLON4XVwdQA6SEeBXeJbWaYYmrXgMqAVsFWGTTG4//omsM/Ry6Etsi36I8GwBuC0zLrpM6Cqfi3Q6r5sASXKgcTAOXhdmwL1GnAnsE/Uy6GNsOBGnGBDH9twPF/fgZHmYMa6gk1Bi37X7+aFZcQ5IApahvdT+Kqty7L8zIBy6oVatvQBaX4NhG0qqLGt8lXdgcNWZcgqK3N9zdE4fQYo4hwwBa6DuDK8l7MQ5cyyT9amoI2INeA6X0HAbaP1tdZl5MpClCmV+dAYvBFT13WwXgAbMaF9tjYHbepO8GbZtVV+BRjbKKDufliyRsDtAHagjgCrygnsC7RZaCPCgRtxHtidP1K6NlV3bR2QI2OwVFKZT0HrSgXpBHZn2jS0qTvBi/5IOep3YI72BZSVRsB1/lpYLbARE9pXaRfQRkQFboQGs+urgO3Kyl/TFkWppCCqTIFZwVoBe+ZPYF+n3UCbWgEv10f61kI96o+Mw7LSWnDXWAg/NYHdiHYHbeoGeLv6CLjctgboqo21xDk4qQpcro8AOgxsxIT21dottKmV8Kq20foIzFXZjWG/EgPloKtA5TEhSvYnsBvQ7qFNNfBGjAGs2hxUt0KMJfsjqsDFNgdr1ZaawG5QbwMt6kqAVfuaegXiaJursxRYVTkyBkv2vxveMVh2qLeEFnVHgFWbq3cZufKrtohLmNYCjGXXdmp490DZkd4eWtQNALu+kczb9a350IgQQMU4hA7MCeyO9KOgRQ0AHLEO4rVQq7prUxqFd9RX9QnsBvVjoWUNQLwG4FvbrlEH4IT1TTShFRoAOGI9xK595Fkj6jLvSP27cQbFpjWhHdAdIK76u+vWaARc1zZh3YkmtCs1CHDEGIwjY9aq2lDbN4Hdjya0N+rOECvhdddsVnnNhHV/mtDeWSsgTq0d32loQyes+9WE9sG6AmLWrZn2nyao76EJ7Qt0B5CHNUF9P01oN6J7gDwB/Rma0E5N7UyHbsDU1NS2NKGdmtqZJrRTUzvThHZqamea0E5N7UwT2qmpnWlCOzW1M01op6Z2pgnt1NTONKGdmtqZJrRTUzvThHZqamea0E5N7UwT2qmpnWlCOzW1M01op6Z2pgnt1NTONKGdmtqZJrRTUzvT/wMw+6IfP72xRAAAAABJRU5ErkJggg=="/><g class="cls-12"><g class="cls-12"><path class="cls-13" d="M145.37,51.23l7.15,2c.31.09.42,0,.5-.29a22.81,22.81,0,0,1,1.52-4.29A3.78,3.78,0,0,1,156,47.16a55,55,0,0,0,8.42-7,34.33,34.33,0,0,0,3.36-3.68c1-1.37,1.14-3-.37-4.08a3,3,0,0,0-3.21.05c-1,.68-2,1.41-3,2.12-.44.33-.86.68-1.29,1-.07.06-.18.13-.25.1s0-.17,0-.27a42.31,42.31,0,0,1,1.65-6.86c.88-3.37,1.83-6.73,2.75-10.09a2.59,2.59,0,0,0-1.18-3.07,2.64,2.64,0,0,0-3.37.71,2.49,2.49,0,0,0-.44,1l-2.22,8c0,.11-.09.28-.17.3s-.14-.15-.2-.24a2.51,2.51,0,0,0-2.34-1.31,2.61,2.61,0,0,0-2.39,1.68c0,.08-.07.16-.1.23-.1.25-.2.5-.31.74h0a5.11,5.11,0,0,0-1.16-1.23,2.7,2.7,0,0,0-3.83,1.43c-.1.3-.14.81-.31.85s-.36-.39-.56-.6a2.67,2.67,0,0,0-4.45.92,78.65,78.65,0,0,0-2.47,8.8,9,9,0,0,0,.24,5.26A14.79,14.79,0,0,0,140,44a.91.91,0,0,1,.1.74c-.41,1.46-.79,2.93-1.19,4.39-.08.27,0,.4.27.47,1.42.38,2.83.78,4.25,1.15Z"/><path class="cls-8" d="M162.29,15.12a2.29,2.29,0,0,1,.59.24,2.59,2.59,0,0,1,1.18,3.07c-.92,3.36-1.87,6.72-2.75,10.09a42.31,42.31,0,0,0-1.65,6.86c0,.1-.08.23,0,.27h0c.06,0,.17,0,.24-.1.43-.33.85-.68,1.29-1,1-.71,2-1.44,3-2.12a3.13,3.13,0,0,1,2.48-.39,2.24,2.24,0,0,1,.73.34c1.51,1.1,1.39,2.71.37,4.08a34.33,34.33,0,0,1-3.36,3.68,55,55,0,0,1-8.42,7,3.78,3.78,0,0,0-1.49,1.45A22.81,22.81,0,0,0,153,52.9c-.08.31-.18.38-.49.29h0l-3.81-1-3.31-.9h0l-1.91-.53L142,50.31l-.87-.24-1.93-.52h0c-.28-.08-.33-.2-.25-.47.4-1.46.78-2.93,1.19-4.39A.91.91,0,0,0,140,44a14.79,14.79,0,0,1-1.27-2,9,9,0,0,1-.24-5.26,78.65,78.65,0,0,1,2.47-8.8,2.63,2.63,0,0,1,3.2-1.65,2.77,2.77,0,0,1,1.25.73c.17.18.25.55.45.61a.14.14,0,0,0,.11,0c.17,0,.21-.55.31-.85a2.75,2.75,0,0,1,3.23-1.7,2.3,2.3,0,0,1,.6.27,5.11,5.11,0,0,1,1.16,1.23h0c.11-.24.21-.49.31-.74,0-.07.07-.15.1-.23a2.61,2.61,0,0,1,2.39-1.68,2.94,2.94,0,0,1,.8.08,2.61,2.61,0,0,1,1.54,1.23c.05.08.06.22.14.24h.06c.08,0,.14-.19.17-.3l2.22-8a2.49,2.49,0,0,1,.44-1,2.67,2.67,0,0,1,2.78-1m.16-.58a3.27,3.27,0,0,0-3.4,1.15,3,3,0,0,0-.56,1.2c-.7,2.57-1.4,5.09-2,7.28a3,3,0,0,0-1.38-.82,3.28,3.28,0,0,0-3.89,1.93l0,.06v0a3.6,3.6,0,0,0-.7-.61,3.05,3.05,0,0,0-.78-.35,3.36,3.36,0,0,0-3.93,2,3.41,3.41,0,0,0-1.41-.79,3.23,3.23,0,0,0-3.92,2,81.06,81.06,0,0,0-2.5,8.87,9.67,9.67,0,0,0,.27,5.61,6.26,6.26,0,0,0,.84,1.43c.17.24.33.47.47.7a.3.3,0,0,1,0,.27c-.23.83-.46,1.67-.67,2.48-.17.63-.35,1.28-.52,1.92a1,1,0,0,0,.06.77,1,1,0,0,0,.62.44h0l1.93.52.44.12.43.12,1.46.39,1.9.53h0l1.66.45,1.65.45,3.81,1.05h0a1,1,0,0,0,.79-.06,1.07,1.07,0,0,0,.44-.66,21.77,21.77,0,0,1,1.48-4.18,3.33,3.33,0,0,1,1.28-1.21,54.39,54.39,0,0,0,8.51-7.11l.14-.14a31.48,31.48,0,0,0,3.28-3.61,3.81,3.81,0,0,0,.85-2.83,3.17,3.17,0,0,0-1.34-2.08,3.07,3.07,0,0,0-.93-.44,3.71,3.71,0,0,0-3,.48c-.91.61-1.81,1.26-2.67,1.89l-.33.24-.51.39a34.93,34.93,0,0,1,1-3.85c.19-.63.38-1.28.55-1.93.61-2.31,1.25-4.64,1.88-6.9.28-1,.58-2.12.87-3.18a3.21,3.21,0,0,0-1.47-3.76,3.74,3.74,0,0,0-.72-.29"/></g></g></g></g></g></svg>'  # Replace with your SVG string
print(replace_ids_and_classes(svg_string))