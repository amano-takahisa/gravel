# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import gravel  # noqa

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "gravel"
copyright = "2023, Takahisa Amano"
author = "Takahisa Amano"
release = gravel.__version__

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "matplotlib.sphinxext.plot_directive",
    # "sphinx.ext.viewcode"
    "sphinx.ext.linkcode",
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

# -- sphinx.ext.linkcode

code_url = f"https://github.com/amano-takahisa/gravel/blob/main"


def linkcode_resolve(domain, info):
    import importlib
    import inspect
    import os
    import sys
    import warnings

    if domain != "py":
        return None

    modname = info["module"]
    fullname = info["fullname"]
    submod = sys.modules.get(modname)
    if submod is None:
        return None

    obj = submod
    for part in fullname.split("."):
        try:
            with warnings.catch_warnings():
                # Accessing deprecated objects will generate noisy warnings
                warnings.simplefilter("ignore", FutureWarning)
                obj = getattr(obj, part)
        except AttributeError:
            return None

    try:
        fn = inspect.getsourcefile(inspect.unwrap(obj))  # type: ignore
        if fn == "<string>":
            return None
    except TypeError:
        try:  # property
            fn = inspect.getsourcefile(inspect.unwrap(obj.fget))
        except AttributeError:
            fn = None
    if not fn:
        return None

    try:
        source, lineno = inspect.getsourcelines(obj)
    except TypeError:
        try:  # property
            source, lineno = inspect.getsourcelines(obj.fget)
        except AttributeError:
            lineno = source = None
    except OSError:
        lineno = source = None

    if lineno is not None and source is not None:
        linespec = f"#L{lineno}-L{lineno + len(source) - 1}"
    else:
        linespec = ""

    fn = os.path.relpath(fn, start=os.path.dirname(gravel.__file__))

    return f"https://github.com/amano-takahisa/gravel/blob/main/gravel/{fn}{linespec}"
    # the following is
    # if "+" in gravel.__version__:
    #     return (
    #         f"https://github.com/amano-takahisa/gravel/blob/main/gravel/{fn}{linespec}"
    #     )
    # else:
    #     return (
    #         f"https://github.com/amano-takahisa/gravel/blob/"
    #         f"v{gravel.__version__}/gravel/{fn}{linespec}"
    #     )
