from setuptools import setup, find_packages

setup(
    name='mkdocs-plugin-svg-inline',
    version='0.1',
    description='An MkDocs plugin to inline SVG images',
    long_description='',
    keywords='mkdocs svg',
    author='Timo Toups',
    author_email='github@timotoups.de',
    license='MIT',
    python_requires='>=3.6',
    install_requires=[
        'mkdocs>=1.4',
        'beautifulsoup4>=4.9.3',
    ],
    packages=find_packages(),
    entry_points={
        'mkdocs.plugins': [
            'svg-inline = src.plugin:SvgInlinePlugin',
        ]
    }
)
