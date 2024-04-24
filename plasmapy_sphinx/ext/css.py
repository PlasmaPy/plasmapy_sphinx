from sphinx.application import Sphinx

from plasmapy_sphinx.utils import static_dir, css_dir


def add_plasmapy_css(app, config):

    if static_dir not in config.html_static_path:
        config.html_static_path.append(str(static_dir))

    rel_path = css_dir.relative_to(static_dir)
    app.add_css_file(str(rel_path / "plasmapy.css"), priority=501)


def setup(app: Sphinx) -> None:
    app.setup_extension("sphinx_gallery.load_style")

    # for some "unknown" reason, an extension can not add a style sheet
    # to the sphinx build unless it's done through the 'config-inited'
    # event
    app.connect("config-inited", add_plasmapy_css)
