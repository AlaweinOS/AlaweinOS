# Configuration file for the Sphinx documentation builder.
# MEZAN V4.1.0 - API Documentation

import os
import sys
from datetime import datetime

# Add MEZAN to path
sys.path.insert(0, os.path.abspath('..'))
sys.path.insert(0, os.path.abspath('../MEZAN'))

# -- Project information -----------------------------------------------------
project = 'MEZAN'
copyright = f'{datetime.now().year}, Meshal Alawein'
author = 'Meshal Alawein'
release = '4.1.0'
version = '4.1.0'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',  # Google/NumPy docstring support
    'sphinx.ext.viewcode',  # Add links to source code
    'sphinx.ext.intersphinx',  # Link to other projects
    'sphinx.ext.todo',  # Support for TODO items
    'sphinx.ext.coverage',  # Documentation coverage
    'sphinx.ext.mathjax',  # Math support
    'sphinx.ext.githubpages',  # GitHub Pages support
]

# Napoleon settings (Google-style docstrings)
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = True
napoleon_use_admonition_for_notes = True
napoleon_use_admonition_for_references = True
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_type_aliases = None

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '**.ipynb_checkpoints']

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'  # ReadTheDocs theme
html_static_path = ['_static']
html_logo = None
html_favicon = None

html_theme_options = {
    'canonical_url': '',
    'analytics_id': '',
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}

# -- Options for autodoc ------------------------------------------------------
autodoc_default_options = {
    'members': True,
    'member-order': 'bysource',
    'special-members': '__init__',
    'undoc-members': True,
    'exclude-members': '__weakref__'
}

autodoc_typehints = 'description'
autodoc_class_signature = 'separated'

# -- Options for intersphinx --------------------------------------------------
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'numpy': ('https://numpy.org/doc/stable/', None),
    'scipy': ('https://docs.scipy.org/doc/scipy/', None),
    'networkx': ('https://networkx.org/documentation/stable/', None),
}

# -- Options for todo extension ----------------------------------------------
todo_include_todos = True

# -- Options for coverage ----------------------------------------------------
coverage_write_headline = False
coverage_show_missing_items = True
