"""
This module is a `Sphinx extension
<https://www.sphinx-doc.org/en/master/usage/extensions/index.html>`_
that exposes the functionality of `plasmapy_sphinx.directives`.

.. automodapi:: plasmapy_sphinx.directives
   :no-index:
   :no-groups:

"""
from sphinx.application import Sphinx

from plasmapy_sphinx.directives import confval, event


def setup(app: Sphinx) -> None:
    """
    A `sphinx` ``setup()`` function for setting up all the functionality defined in
    `plasmapy_sphinx.directives`.
    """
    confval.setup(app)
    event.setup(app)
