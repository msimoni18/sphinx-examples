# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = "Sphinx Example's"
copyright = '2022, Matthew Simoni'
author = 'Matthew Simoni'

# The full version, including alpha/beta/rc tags
release = '1.0.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
sys.path.insert(0, os.path.abspath('../sphinxext'))

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.coverage',
    'sphinx.ext.doctest',
    'sphinx.ext.ifconfig',
    'sphinx.ext.intersphinx',
    # 'sphinx.ext.linkcode',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx.ext.todo',
    'sphinx_copybutton',
    'sphinx_design',
    'sphinx_togglebutton',
    'sphinx_gallery',
    'nbsphinx'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '**.ipynb_checkpoints']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'pydata_sphinx_theme'
html_sourcelink_suffix = ""

html_theme_options = {
    'navbar_start': ['navbar-logo'], # default
    'navbar_center': ['navbar-nav'], # default
    'navbar_end': ['theme-switcher', 'navbar-icon-links'],
    'navbar_align': 'content', # default, content/left/right
    'page_sidebar_items': ['page-toc', 'edit-this-page', 'sourcelink'], # default
    'show_prev_next': True, # default
    'footer_items': ['copyright', 'sphinx-version'], # default
    'show_nav_level': 2, # default
    'navigation_depth': 2, # default
    'collapse_navigation': False, # default
    'show_toc_level': 2, # default
    'external_links': [],
    'header_links_before_dropdown': 4, # default
    'icon_links': [
        {
            'name': 'GitHub',
            'url': 'https://github.com',
            'icon': '_static/github-light.svg', 
            'type': 'local'
        },
        {
            'name': 'BitBucket',
            'url': 'https://bitbucket.com',
            'icon': '_static/bitbucket-light.svg', 
            'type': 'local'
        },
        {
            'name': 'Jira',
            'url': 'https://jira.com',
            'icon': '_static/jira-light.svg', 
            'type': 'local'
        },
    ],
    # Overrides html_logo settings. Falls back to 
    # html_logo if only one of the light or dark 
    # variants is provided.
    'logo': { 
        'text': "Sphinx Example's",
        # 'image_light': 'logo-light.svg',
        # 'image_dark': 'logo-dark.svg'
    }
}

# html_sidebars = {}

html_context = {
    'default_mode': 'light'
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_css_files = []

# Name of an image file (within the static path) to use
# as favicon of the docs. This file should be a Windows icon
# file (.ico) being 16x16 or 32x32 pixels large.
html_favicon = ''

# Name of an image file (relative to this directory) to
# place at the top of the sidebar.
html_logo = ''

