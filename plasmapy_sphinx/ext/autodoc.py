from sphinx.application import Sphinx

from plasmapy_sphinx.autodoc import automodapi


def setup(app: Sphinx):
    """
    Sphinx ``setup()`` function for setting up all of the
    `plasmapy_sphinx.autodoc` functionality, this includes
    `plasmapy_sphinx.automodsumm` functionality.
    """
    rtn = automodapi.setup(app)

    return rtn
