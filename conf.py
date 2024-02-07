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

sys.path.append(os.path.abspath('python/python-basic-cert/reverse-words-swap-cases'))
sys.path.append(os.path.abspath('python/python-basic-cert/multiset-implementation'))

author = 'Xander Harris'
copyright = '2024, Xander Harris'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
extensions = [
    'myst_parser',
    'sphinx.ext.autodoc',
    'sphinx.ext.githubpages',
]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_static_path = ['_static']
html_theme = 'alabaster'

myst_title_to_header = True
project = 'Hacker Rank Challenges'
release = '0.0.1'
source_suffix = {
    '.md': 'markdown'
}
templates_path = ['_templates']
