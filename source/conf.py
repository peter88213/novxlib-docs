# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'novxlib Online documentation'
copyright = '2024, peter88213'
author = 'Peter Triesberger'
version = 'Version 4.1+'
release = '4.1.0'
# The release is related to the novelibre application's major/minor version numbers.

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

extensions = []

templates_path = ['_templates']
exclude_patterns = []

highlight_language = 'ini'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# html_title = 'novxlib Online documentation'
# html_favicon = '_images/nLogo32.ico'

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#
html_extra_path = ['_custom_files']

# If true, links to the reST sources are added to the pages.
#
html_copy_source = False

