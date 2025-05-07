"""
This `Sphinx <https://www.sphinx-doc.org/en/master/>`__ extension package
contains custom documentation functionality used to document
`PlasmaPy's packages <https://github.com/PlasmaPy>`_ .

.. contents:: Content
   :local:

Installation
------------

This package is currently not released in any form and can only be obtained by
installing `plasmapy` directly from its
`GitHub repository <https://github.com/plasmapy/plasmapy>`_.  We do plan to breakout
`plasmapy_sphinx` into its own repository and release it to https://pypi.org at
a future date.

Setup
-----

To enable `plasmapy_sphinx`'s functionality it needs to be added to the
:confval:`extensions` configuration value in your ``conf.py`` file.

.. code-block::

    extensions = ["plasmapy_sphinx"]

If you don't want all of `plasmapy_sphinx`'s functionality, then any module
containing a Sphinx ``setup()`` function can be activated independently.  For
example, you can just implement the :rst:dir:`automodapi` functionality by
setting up the `plasmapy_sphinx.autodoc.automodapi` module like...

.. code-block::

    extensions = ["plasmapy_sphinx.autodoc.automodapi"]

The Rundown
-----------

`plasmapy_sphinx.autodoc`
~~~~~~~~~~~~~~~~~~~~~~~~~

   The `plasmapy_sphinx.autodoc` sub-package contains functionality that extends
   `sphinx.ext.autodoc`.  The defined directives are registered as
   `sphinx.ext.autodoc` directives and, thus, will behave similarly to
   :rst:dir:`autoclass`, :rst:dir:`autofunction`, etc. and work with
   `sphinx.ext.autosummary` and `plasmapy_sphinx.automodsumm`.

`plasmapy_sphinx.automodsumm`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   The `plasmapy_sphinx.automodsumm` sub-package is an evolution of
   `sphinx.ext.autosummary` and was adapted from `sphinx_automodapi.automodsumm`.
   Unlike the :rst:dir:`autosummary` directive where you have to manually list
   all the objects/members to appear in the summary table, the
   :rst:dir:`automodsumm` directive will inspect a given module and automatically
   populate the summary table with the detected objects/members.

`plasmapy_sphinx.directives`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   This sub-package contains custom reStructuredText directives and roles that
   do not fall under `plasmapy_sphinx.autodoc` or `plasmapy_sphinx.automodsumm`.

"""
# The code here was adapted from v0.14.0.dev0 of sphinx_automodapi
__all__ = ["__version__"]

# Enforce Python version check during package import.
# This is the same check as the one at the top of setup.py
import sys

if sys.version_info < (3, 8):  # coverage: ignore
    raise ImportError("plasmapy_sphinx does not support Python < 3.8")

from importlib.metadata import version, PackageNotFoundError

from plasmapy_sphinx import autodoc, automodsumm, directives, utils


# define version
try:
    # note: if there's any distribution metadata in your source files, then this
    #       will find a version based on those files.  Keep distribution metadata
    #       out of your repository unless you've intentionally installed the package
    #       as editable (e.g. `pip install -e {root_directory}`),
    #       but then __version__ will not be updated with each commit, it is
    #       frozen to the version at time of install.
    #
    #: `plasmapy_sphinx` version string
    __version__ = version("plasmapy_sphinx")
except PackageNotFoundError:
    # package is not installed
    fallback_version = "unknown"
    try:
        # code most likely being used from source
        # if setuptools_scm is installed then generate a version
        from setuptools_scm import get_version

        __version__ = get_version(
            root="..", relative_to=__file__, fallback_version=fallback_version
        )
        del get_version
        warn_add = "setuptools_scm failed to detect the version"
    except ModuleNotFoundError:
        # setuptools_scm is not installed
        __version__ = fallback_version
        warn_add = "setuptools_scm is not installed"

    if __version__ == fallback_version:
        from warnings import warn

        warn(
            f"plasmapy_sphinx.__version__ not generated (set to 'unknown'), "
            f"plasmapy_sphinx is not an installed package and {warn_add}.",
            RuntimeWarning,
        )

        del warn
    del fallback_version, warn_add

del sys
