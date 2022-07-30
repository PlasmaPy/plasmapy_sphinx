# Sphinx Guide to Theme Development
# https://www.sphinx-doc.org/en/master/development/theming.html
from sphinx.application import Sphinx

from plasmapy_sphinx.ext.css import setup as css_setup
from plasmapy_sphinx.utils import theme_dir


def setup(app: Sphinx) -> None:
    app.setup_extension("sphinx_rtd_theme")
    app.setup_extension("sphinx_gallery.load_style")
    css_setup(app)

    # Register the theme that can be referenced without adding a theme path
    app.add_html_theme('plasmapy_theme', theme_path=theme_dir)
