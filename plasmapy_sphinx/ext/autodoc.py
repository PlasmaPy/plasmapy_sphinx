from sphinx.application import Sphinx

from plasmapy_sphinx.autodoc import automodapi


def setup(app: Sphinx):
    """
    Sphinx ``setup()`` function for setting up all of the
    `plasmapy_sphinx.autodoc` functionality, this includes
    `plasmapy_sphinx.automodsumm` functionality.
    """
    # Note: automodsumm functionality is set up by the autodoc setup, since
    # automodsumm is needed for autodoc.automodapi

    rtn = automodapi.setup(app)

    return rtn
