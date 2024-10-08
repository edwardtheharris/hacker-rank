"""Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
"""
# pylint: disable=invalid-name,redefined-builtin

import os
import sys

sys.path.append(os.path.abspath('python/python-basic-cert/reverse_and_swap'))
sys.path.append(os.path.abspath('python/python-basic-cert/implement_multiset'))
sys.path.append(os.path.abspath('python/simple_array_sum'))
sys.path.append(os.path.abspath('python/compare_the_triplets'))

author = 'Xander Harris'
autoyaml_root = "."
autoyaml_doc_delimiter = "###"
autoyaml_comment = "#"
autoyaml_level = 10
autoyaml_safe_loader = True
copyright = '2024, Xander Harris'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

exclude_patterns = [
    '_build',
    'Thumbs.db',
    '.DS_Store',
    '.venv/*',
    '.tmp/*',
    '.pytest_cache/*',
]

extensions = [
    'myst_parser',
    'sphinx_design',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.githubpages',
    'sphinx.ext.intersphinx',
    'sphinxcontrib.autoyaml',
    'sphinxcontrib.youtube',
]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_logo = '_static/img/hr-logo.svg'
html_favicon = '_static/img/hr-logo.svg'
html_static_path = ['_static']
html_theme = 'sphinx_book_theme'
myst_dmath_double_inline=True
myst_enable_extensions = [
    "amsmath",
    "attrs_block",
    "attrs_inline",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]
myst_title_to_header = True
project = 'Hacker Rank Challenges'
rst_epilog = """
.. sectionauthor:: Xander Harris <xandertheharris@gmail.com>
"""
release = '0.0.1'
show_authors=True
source_suffix = {
    '.md': 'markdown',
    '.rst': 'restructuredtext'
}
templates_path = ['_templates']
