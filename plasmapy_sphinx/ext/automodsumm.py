from sphinx.application import Sphinx

from plasmapy_sphinx.automodsumm import core


def setup(app: Sphinx):
    """
    Sphinx ``setup()`` function for setting up the :rst:dir:`automodsumm`
    functionality.
    """
    rtn = core.setup(app)
    return rtn
