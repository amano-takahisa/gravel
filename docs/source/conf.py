# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import geopandas  # noqa

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "gravel"
copyright = "2023, Takahisa Amano"
author = "Takahisa Amano"
release = "0.1.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "matplotlib.sphinxext.plot_directive",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# These patterns also affect html_static_path and html_extra_path
exclude_patterns = []

# A list of ignored prefixes for module index sorting.
modindex_common_prefix = ["gravel."]

# -- Options for HTML output -------------------------------------------------
# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

html_context = {
    "display_github": True,  # Integrate GitHub
    "github_user": "amano-takahisa",  # Username
    "github_repo": "gravel",  # Repo name
    "github_version": "master",  # Version
    "conf_py_path": "/docs/source/",  # Path in the checkout to the docs root
}

# -- Options for extensions -------------------------------------------------
# -- sphinx.ext.autodoc
autodoc_default_options = {
    "members": True,
    "member-order": "bysource",
    "special-members": True,
    "undoc-members": True,
    "special-members": "__init__",
    "noindex": True,
}


# -- matplotlib.sphinxext.plot_directive
# https://matplotlib.org/stable/api/sphinxext_plot_directive_api.html

# Default value for the include-source option (default: False).
plot_include_source = True

# Whether to show a link to the source in HTML (default: True).
plot_html_show_source_link = False

# File formats to generate (default: ['png', 'hires.png', 'pdf']).
# List of tuples or strings:
plot_formats = ["png"]

# Whether to show links to the files in HTML (default: True).
plot_html_show_formats = False
