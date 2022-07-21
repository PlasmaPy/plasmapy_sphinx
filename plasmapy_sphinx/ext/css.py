import os

from sphinx.application import Sphinx

from plasmapy_sphinx.utils import css_dir


def setup(app: Sphinx) -> None:
    app.add_css_file(
        os.path.join(css_dir, "admonition_color_contrast.css"),
    )
    app.add_css_file(
        os.path.join(css_dir, "plasmapy.css"),
        priority=501,
    )
