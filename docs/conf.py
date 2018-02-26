#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from recommonmark.parser import CommonMarkParser
import sys
import os
import re
import juliadoc
import sphinx_rtd_theme
import shutil

# pre
shutil.copy2("../CONTRIBUTING.md", ".")
shutil.copy2("../README.md", "MainPage.md")
feature_source = open("../res/META-INF/description.html", "r")
feature_target = open("Features.md", "w")
feature_target.write("# Features\n")
feature_target.write(feature_source.read())
feature_target.close()
feature_source.close()

extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.intersphinx',
              'sphinx.ext.imgmath',
              'sphinx.ext.ifconfig',
              'sphinx.ext.viewcode', 
              'juliadoc.julia',
              'juliadoc.jldoctest',
              'juliadoc.jlhelp']
# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']
source_suffix = ['.rst', '.md']
source_parsers = {
    '.md': CommonMarkParser,
}
master_doc = 'index'

# General information about the project.
project = 'Julia-IntelliJ'
copyright = '2018, ice1000'
author = 'ice1000'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '0.1.0'
# The full version, including alpha/beta/rc tags.
release = '0.1.0'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'julia'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'julia'
html_theme_path = [juliadoc.get_theme_dir(),
                   sphinx_rtd_theme.get_html_theme_path()]
html_static_path = ['_static']
html_sidebars = {
    '**': [
        'relations.html',
        'searchbox.html',
    ]
}
htmlhelp_basename = 'Julia-Intellijdoc'
# latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
# }

# latex_documents = [
#     (master_doc, 'Julia-Intellij.tex', 'Julia-Intellij Documentation',
#      'ice1000', 'manual'),
# ]
# -- Options for manual page output ---------------------------------------
# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'julia-intellij', 'Julia-Intellij Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'Julia-Intellij', 'Julia-Intellij Documentation',
     author, 'Julia-Intellij', 'One line description of project.',
     'Miscellaneous'),
]
