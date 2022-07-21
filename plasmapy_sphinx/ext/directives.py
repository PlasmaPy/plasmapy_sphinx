from sphinx.application import Sphinx

from plasmapy_sphinx.directives import confval, event


def setup(app: Sphinx) -> None:
    """
    A `sphinx` ``setup()`` function for setting up all the functionality defined in
    `plasmapy_sphinx.directives`.
    """
    confval.setup(app)
    event.setup(app)
