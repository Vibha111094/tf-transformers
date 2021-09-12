# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

sys.path.insert(0, os.path.abspath("../../src"))


# -- Project information -----------------------------------------------------

project = 'TF Transformers'
copyright = "2019, The TFT Team, Licenced under the Apache License, Version 2.0"
author = "tft"

# The short X.Y version
version = " "
# The full version, including alpha/beta/rc tags
release = " "


# Prefix link to point to master, comment this during version release and uncomment below line
extlinks = {"prefix_link": ("https://github.com/huggingface/transformers/blob/master/%s", "")}
# Prefix link to always point to corresponding version, uncomment this during version release
# extlinks = {'prefix_link': ('https://github.com/huggingface/transformers/blob/v'+ release + '/%s', '')}

# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
needs_sphinx = '2.1'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.extlinks",
    "sphinx.ext.coverage",
    "sphinx.ext.napoleon",
    "recommonmark",
    "sphinx.ext.viewcode",
    "sphinx_markdown_tables",
    "sphinxext.opengraph",
    "sphinx_copybutton",
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'numpy': ('https://numpy.org/doc/stable/', None),
    'scipy': ('https://docs.scipy.org/doc/scipy/reference/', None),
}

suppress_warnings = [
    'ref.citation',  # Many duplicated citations in numpy/scipy docstrings.
    'ref.footnote',  # Many unreferenced footnotes in numpy/scipy docstrings
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
# Note: important to list ipynb before md here: we have both md and ipynb
# copies of each notebook, and myst will choose which to convert based on
# the order in the source_suffix list. Notebooks which are not executed have
# outputs stored in ipynb but not in md, so we must convert the ipynb.
source_suffix = ['.rst', '.ipynb', '.md']

# The master toctree document.
master_doc = "index"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    # Sometimes sphinx reads its own outputs as inputs!
    'build/html',
    'build/jupyter_execute',
    'notebooks/README.md',
    'README.md',
    # Ignore markdown source for notebooks; myst-nb builds from the ipynb
    # These are kept in sync using the jupytext pre-commit hook.
    'notebooks/*.md',
    'jax-101/*.md',
    'autodidax.md',
    # Attempt to fix RTD build failure
    'transformations.md',
]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = None
autosummary_generate = True

# Remove the prompt when copying examples
copybutton_prompt_text = r">>> |\.\.\. "
copybutton_prompt_is_regexp = True

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    "analytics_id": "UA-83738774-2",
    "navigation_with_keys": True,
    'logo_only': True,
}

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = '_static/transformers_mix.png'

html_favicon = '_static/favicon.png'

# -- <JAX? Options for myst ----------------------------------------------
jupyter_execute_notebooks = "force"
execution_allow_errors = False
execution_fail_on_error = True  # Requires https://github.com/executablebooks/MyST-NB/pull/296

# Notebook cell execution timeout; defaults to 30.
execution_timeout = 100

# List of patterns, relative to source directory, that match notebook
# files that will not be executed.
execution_excludepatterns = [
    # Slow notebook: long time to load tf.ds
    'notebooks/neural_network_with_tfds_data.*',
    # Slow notebook
    'notebooks/Neural_Network_and_Data_Loading.*',
    'notebooks/score_matching.*',
    'notebooks/maml.*',
    # Strange error apparently due to asynchronous cell execution
    'notebooks/thinking_in_jax.*',
    # TODO(jakevdp): enable execution on these
    'jax-101/*',
    'notebooks/xmap_tutorial.*',
]

#  Configuration for OpenGraph and Twitter Card Tags.
# These are responsible for creating nice shareable social images https://ahrefs.com/blog/open-graph-meta-tags/
# https://ogp.me/#type_website
ogp_image = "png location"
ogp_description = "State-of-the-art Faster Natural Language Processing in Tensorflow 2.0"
ogp_description_length = 160

ogp_custom_meta_tags = [
    f'<meta name="twitter:image" content="{ogp_image}">',
    f'<meta name="twitter:description" content="{ogp_description}">',
]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}

# This must be the name of an image file (path relative to the configuration
# directory) that is the favicon of the docs. Modern browsers use this as
# the icon for tabs, windows and bookmarks. It should be a Windows-style
# icon file (.ico).
html_favicon = "favicon.ico"


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "transformersdoc"


# -- Options for LaTeX output ------------------------------------------------

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
# 'figure_align': 'htbp',}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, "transformers.tex", "transformers Documentation", "huggingface", "manual"),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, "transformers", "transformers Documentation", [author], 1)]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "transformers",
        "transformers Documentation",
        author,
        "transformers",
        "One line description of project.",
        "Miscellaneous",
    ),
]


# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ["search.html"]

# Localization
locale_dirs = ['locale/']
gettext_compact = False


def setup(app):
    app.add_css_file("css/huggingface.css")
    # app.add_css_file("css/code-snippets.css")
    # app.add_js_file("js/custom.js")


# -- Extension configuration -------------------------------------------------
