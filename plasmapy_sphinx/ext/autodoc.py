"""
This module is a `Sphinx extension
<https://www.sphinx-doc.org/en/master/usage/extensions/index.html>`_
that exposes the functionality of `plasmapy_sphinx.autodoc`.

.. automodapi:: plasmapy_sphinx.autodoc
   :no-index:
   :no-groups:

"""
__all__ = ["automodapi", "setup"]
from sphinx.application import Sphinx

from plasmapy_sphinx.autodoc import automodapi


def setup(app: Sphinx):
    """
    Sphinx ``setup()`` function for setting up all the
    `plasmapy_sphinx.autodoc` functionality, this includes
    `plasmapy_sphinx.automodsumm` functionality.
    """
    # Note: automodsumm functionality is set up by the autodoc setup, since
    # automodsumm is needed for autodoc.automodapi

    rtn = automodapi.setup(app)

    return rtn
