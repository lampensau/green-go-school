document.addEventListener('DOMContentLoaded', async function () {
  let containers = Array.from(document.querySelectorAll('.svg-container'));

  await Promise.all(
    containers.map(async (container) => {
      let filename = container.getAttribute('data-filename');
      try {
        let response = await fetch(filename + '.svg');
        if (!response.ok) {
          throw new Error(`HTTP Status ${response.status}`);
        }
        let data = await response.text();
        container.innerHTML = data;
        let svg = container.querySelector('svg');
        if (svg) {
          let allElements = svg.querySelectorAll('[class], [id]');
          let classMap = {}; // To map old class names to new ones
          let idMap = {}; // To map old IDs to new ones

          allElements.forEach((el) => {
            ['class', 'id'].forEach((attr) => {
              let map = attr === 'class' ? classMap : idMap;
              let currentValue = el.getAttribute(attr);
              if (currentValue) {
                let newValue = currentValue.split(' ').map((name) => {
                  if (!map[name]) {
                    map[name] = name + Math.random().toString(36).substring(2, 15);
                  }
                  return map[name];
                });
                el.setAttribute(attr, newValue.join(' '));
              }
            });
          });

          // Update <style> within <defs>
          let styles = svg.querySelector('defs style');
          if (styles) {
            let updatedCSS = styles.innerHTML;
            for (let oldClassName in classMap) {
              let regex = new RegExp(`\\.${oldClassName}\\b`, 'g');
              updatedCSS = updatedCSS.replace(regex, '.' + classMap[oldClassName]);
            }
            styles.innerHTML = updatedCSS;
          }

          // Update ID references within <defs> and url() function calls
          ['defs', '[filter]', '[clip-path]', '[mask]', '[fill]'].forEach((selector) => {
            let elements = svg.querySelectorAll(selector);
            elements.forEach((el) => {
              let updatedContent = el.innerHTML || el.getAttribute(selector.slice(1));
              if (updatedContent) {
                for (let oldId in idMap) {
                  let regex = new RegExp(`#${oldId}(?!\\w)|url\\(#${oldId}\\)`, 'g');
                  updatedContent = updatedContent.replace(regex, (match) =>
                    match.startsWith('#') ? `#${idMap[oldId]}` : `url(#${idMap[oldId]})`
                  );
                }
                if (el.innerHTML !== undefined) {
                  el.innerHTML = updatedContent;
                } else {
                  el.setAttribute(selector.slice(1), updatedContent);
                }
              }
            });
          });
        }
      } catch (error) {
        container.textContent = `${error.message}`;
      }
    })
  );
});
