# Sphinx Guide to Theme Development
# https://www.sphinx-doc.org/en/master/development/theming.html
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
