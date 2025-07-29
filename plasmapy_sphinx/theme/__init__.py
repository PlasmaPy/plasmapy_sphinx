# Sphinx Guide to Theme Development
# https://www.sphinx-doc.org/en/master/development/theming.html
r"""
The PlasmaPy theme is a `Sphinx theme
<https://www.sphinx-doc.org/en/master/usage/theming.html>`_ that
inherits from the `sphinx_rtd_theme`.  As such, it shares all the same
`configuration values supported by sphinx_rtd_theme
<https://sphinx-rtd-theme.readthedocs.io/en/stable/configuring.html#theme-options>`_\ .

To use the PlasmaPy theme one needs to the :file:`conf.py`:

.. code-block:: python

    extensions = ["plasmapy_sphinx.theme"]
    html_theme = "plasmapy_theme"

"""
__all__ = ["setup"]
from sphinx.application import Sphinx

from plasmapy_sphinx.ext.css import setup as css_setup
from plasmapy_sphinx.utils import theme_dir


def setup(app: Sphinx) -> None:
    """
    Sphinx ``setup()`` function for setting up the PlasmaPy theme.
    """
    css_setup(app)
    app.setup_extension("sphinx_gallery.load_style")

    # Register the theme that can be referenced without adding a theme path
    app.add_html_theme("plasmapy_theme", theme_path=str(theme_dir.absolute()))
