from sphinx.application import Sphinx

from plasmapy_sphinx.utils import css_dir


def add_plasmapy_css(app, config):
    path = str(css_dir)
    if path not in config.html_static_path:
        config.html_static_path.append(path)

    app.add_css_file("admonition_color_contrast.css")
    app.add_css_file("plasmapy.css", priority=501)


def setup(app: Sphinx) -> None:
    app.setup_extension("sphinx_gallery.load_style")

    # for some "unknown" reason, an extension can not add a style sheet
    # to the sphinx build unless it's done through the 'config-inited'
    # event
    app.connect("config-inited", add_plasmapy_css)
