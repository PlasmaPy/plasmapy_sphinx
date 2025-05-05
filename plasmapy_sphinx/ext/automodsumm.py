"""
This module is a `Sphinx extension
<https://www.sphinx-doc.org/en/master/usage/extensions/index.html>`_
that exposes the functionality of `plasmapy_sphinx.automodsumm`.

.. automodapi:: plasmapy_sphinx.automodsumm
   :no-index:
   :no-groups:

"""
from sphinx.application import Sphinx

from plasmapy_sphinx.automodsumm import core


def setup(app: Sphinx):
    """
    Sphinx ``setup()`` function for setting up the :rst:dir:`automodsumm`
    functionality.
    """
    rtn = core.setup(app)
    return rtn
