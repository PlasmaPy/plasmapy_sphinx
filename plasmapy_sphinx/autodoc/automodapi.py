"""
This module contains the functionality used to define the :rst:dir:`automodapi`
directive and its :ref:`supporting configuration values <automodapi-confvals>`.

.. contents:: Content
    :local:

`automodapi` Directive
----------------------

.. rst:directive:: automodapi

    The :rst:dir:`automodapi` directive is a wrapper on Sphinx's
    :rst:dir:`automodule` directive and registered as one of the
    `sphinx.ext.autodoc` directives.  As such, many of the :rst:dir:`automodule`
    options still work, except any of the *member* options and *ignore-module-all*.
    The registration of :rst:dir:`automodapi` with `~sphinx.ext.autodoc` means
    :rst:dir:`automodapi` is used by Sphinx when indexing the documented module.

    :rst:dir:`automodapi` is used to document modules (i.e. packages and ``.py``
    files.  The contents of the `plasmapy_sphinx.utils` page shows an example
    of how the following declaration is rendered.

    .. code-block:: rst

        `plasmapy_sphinx.utils`
        =======================

        .. automodapi:: plasmapy_sphinx.utils

    The module level docstring is first rendered and then the categorized groups
    are rendered in :rst:dir:`automodsumm` tables filtered for the associated group
    and placed under the appropriate object type heading.  The order in which the
    :rst:dir:`automodsumm` tables are displayed is controlled by the configuration
    value :confval:`automodapi_group_order`.

    .. rst:directive:option:: groups

        When a module is inspected all the identified objects are categorized into
        groups.  The built-in groups are:

        +----------------+-------------------------------------------------------------+
        | **modules**    | Direct sub-packages and modules.                            |
        +----------------+-------------------------------------------------------------+
        | **classes**    | Python classes. (excluding **exceptions** and **warnings**) |
        +----------------+-------------------------------------------------------------+
        | **exceptions** | Classes that inherit from `BaseException`. (excluding       |
        |                | **warnings**)                                               |
        +----------------+-------------------------------------------------------------+
        | **warnings**   | Classes that inherit from `Warning`.                        |
        +----------------+-------------------------------------------------------------+
        | **functions**  | Objects that satisfy :func:`inspect.isroutine`.             |
        +----------------+-------------------------------------------------------------+
        | **variables**  | All other objects.                                          |
        +----------------+-------------------------------------------------------------+

        In addition to the built-in groups, groups defined in
        :confval:`automodapi_custom_groups` will be categorized.  When objects are
        collected and grouped the **modules** will be done first, followed by any
        custom group, and, finally, the built-in groups.  By default, tables will
        be generated for **all** groups.

        The contents of the :ref:`API section <automodapi-api>` below shows
        an example of how the follow declaration is rendered.

        .. code-block:: rst

            .. automodapi:: plasmapy_sphinx.autodoc.automodapi
               :no-main-docstring:

            or

            .. automodapi:: plasmapy_sphinx.autodoc.automodapi
               :no-main-docstring:
               :groups: all

        The behavior of ``:no-main-docstring:`` is described below
        in the :rst:dir:`automodapi:no-main-docstring` section.  If you
        only want to display only **classes**, then the following can be done.

        .. code-block:: rst

            .. automodapi:: plasmapy_sphinx.autodoc.automodapi
               :no-main-docstring:
               :groups: classes

        If you want to include multiple groups, then specify all groups as a
        comma separated list.

        .. code-block:: rst

            .. automodapi:: plasmapy_sphinx.autodoc.automodapi
               :groups: classes, functions

    .. rst:directive:option:: exclude-groups

        This option behaves just like :rst:dir:`automodapi:groups` except
        you are selectively excluding groups for the generated tables.  Using the
        same example as before, a table of just **classes** can be generated by
        doing

        .. code-block:: rst

            .. automodapi:: plasmapy_sphinx.autodoc.automodapi
               :exclude-groups: functions

    .. rst:directive:option:: no-groups

        Specify if you want to exclude all :rst:dir:`automodsumm` tables from
        being generated.

        .. code-block:: rst

            .. automodapi:: plasmapy_sphinx.autodoc.automodapi
               :no-groups:

    .. rst:directive:option:: skip

        This option allows you to skip (exclude) selected objects from the
        generated tables.  The argument is given as a comma separated list of
        the object's short name.  Continuing with the example from above, let's
        skip `~plasmapy_sphinx.autodoc.automodapi.ModAPIDocumenter` and
        `~plasmapy_sphinx.autodoc.automodapi.setup` from the tables.

        .. code-block:: rst

            .. automodapi:: plasmapy_sphinx.autodoc.automodapi
               :no-main-docstrings:
               :skip: ModAPIDocumenter, setup

        .. automodapi:: plasmapy_sphinx.autodoc.automodapi
           :noindex:
           :no-toctree:
           :no-main-docstring:
           :skip: ModAPIDocumenter, setup

    .. rst:directive:option:: noindex

        Like the rest of Sphinx's `~sphinx.ext.autodoc` directives,
        :rst:dir:`automodapi` is used by Sphinx to index the documented module
        and make available cross-referencing.  To prevent multiple
        cross-references to the same documented module, ``:noindex:`` can be used
        to prevent the indexing.

        .. code-block:: rst

            .. automodapi:: plasmapy_sphinx.autodoc.automodapi
               :noindex:

    .. rst:directive:option:: include-heading

        This option will create a top level heading for the documented module.

        .. code-block:: rst

            .. automodapi:: foo.bar
               :include-heading:

        If ``bar`` is a package, then the heading will look like

        .. code-block:: rst

            foo.bar Package
            ---------------

        and if ``bar`` is a ``.py`` file, then the heading will look like

        .. code-block:: rst

            foo.bar Module
            --------------

    .. rst:directive:option:: heading-chars

        (Default ``-^``) A two character string specifying the underline characters
        used for the heading created by :rst:dir:`automodapi`.  The following code

        .. code-block:: rst

            .. automodapi:: foo.bar
               :include-heading:
               :heading-chars: ^~

        would generate reStructuredText equivalent to

        .. code-block:: rst

            foo.bar Package
            ^^^^^^^^^^^^^^^

            I am the main docstring

            Sub-Packages & Modules
            ~~~~~~~~~~~~~~~~~~~~~~

            .. automodsumm:: foo.bar
               :toctree: api
               :groups: modules

        If :rst:dir:`automodapi:include-heading` is not given, then the first
        character will be used for the :rst:dir:`automodsumm` table headings.

    .. rst:directive:option:: toctree

        If you want the tables generated by :rst:dir:`automodapi` to serve as
        :rst:dir:`toctree`'s, then specify this option with a directory path
        ``DIRNAME`` with respect to the location of your ``conf.py``.

        .. code-block:: rst

            .. automodapi:: plasmapy_sphinx.autodoc.automodapi
               :toctree: DIRNAME

        If ``:toctree:`` is not set, then ``DIRNAME`` will default to what is set
        by :confval:`automodapi_default_toctree_dir`.  If no :rst:dir:`toctree`
        is desired, then use option :rst:dir:`automodapi:no-toctree`.

    .. rst:directive:option:: no-toctree

        Use this option if you do not want the tables generated by
        :rst:dir:`automodapi` to serve as :rst:dir:`toctree`'s.

        .. code-block:: rst

            .. automodapi:: plasmapy_sphinx.autodoc.automodapi
               :no-toctree:

    .. rst:directive:option:: no-main-docstring

        By default the module level docstring will be rendered and displayed, but
        setting this option will omit the module level docstring and leave just
        the :rst:dir:`autosummary` tables for each collected group of objects.

        .. code-block:: rst

            .. automodapi:: plasmapy_sphinx.autodoc.automodapi
               :no-main-docstring:

    .. rst:directive:option:: inheritance-diagram

        Set this option to generate inheritance diagrams (using the directive
        :rst:dir:`inheritance-diagram`) for the groups listed in the configuration
        value :confval:`automodapi_groups_with_inheritance_diagrams`.  Default
        behavior is controlled by the configuration value
        :confval:`automodapi_include_inheritance_diagram`.  The option
        :rst:dir:`automodapi:no-inheritance-diagram` will supersede this option.

        .. code-block:: rst

            .. automodapi:: plasmapy_sphinx.autodoc.automodapi
               :inheritance-diagram:

    .. rst:directive:option:: no-inheritance-diagram

        Set this option to not generate inheritance diagrams.  This option will
        take precedence over the :rst:dir:`automodapi:inheritance-diagram` option.

        .. code-block:: rst

            .. automodapi:: plasmapy_sphinx.autodoc.automodapi
               :no-inheritance-diagram:

.. _automodapi-confvals:

`automodapi` Configuration Values
---------------------------------

A configuration value is a variable that can be defined in ``conf.py`` to configure
the default behavior of related `sphinx` directives.  The configuration values
below relate to the behavior of the :rst:dir:`automodapi` directive.

.. confval:: automodapi_default_toctree_dir

    (Default ``"api"``)  The default directory name, with respect to ``conf.py``,
    for :rst:dir:`automodapi` to write stub files to.  This is the default
    value for :rst:dir:`automodapi:toctree`.

.. confval:: automodapi_group_order

    (Default ``("modules", "classes", "exceptions", "warnings", "functions",
    "variables")``)  A tuple defining the order :rst:dir:`automodapi` should
    display the collected groups.  If :rst:dir:`automodapi` identifies groups
    that are not identified here (e.g. unlisted custom groups), then those
    groups will be displayed alphabetically after the groups defined in
    :confval:`automodapi_group_order`.  *This configuration value should be
    defined if custom groups are defined by* :confval:`automodapi_custom_groups` *.*

.. confval:: automodapi_groups_with_inheritance_diagrams

    (Default ``["classes", "exceptions", "warnings"]``) A list defining which
    groups should have inheritance diagrams associated with them when displayed
    by :rst:dir:`automodapi`.

.. confval:: automodapi_include_inheritance_diagram

    (Default `True`) Controls if :rst:dir:`automodapi` will by default generated
    inheritance diagrams (see directive :rst:dir:`inheritance-diagram`) for a
    given group.  The groups that should get inheritance diagrams are defined by
    the configuration value :confval:`automodapi_groups_with_inheritance_diagrams`.

"""
__all__ = ["AutomodapiOptions", "ModAPIDocumenter", "setup"]

import inspect
import re
import sys
import warnings

from collections import OrderedDict
from docutils.parsers.rst import directives
from docutils.statemachine import StringList
from sphinx.application import Sphinx

try:
    from sphinx.deprecation import RemovedInSphinx50Warning
except ImportError:

    class RemovedInSphinx50Warning(PendingDeprecationWarning):
        pass


from sphinx.ext.autodoc import bool_option, ModuleDocumenter
from sphinx.locale import __
from sphinx.util import logging
from typing import Any, Callable, Dict, List, Optional, Union

from plasmapy_sphinx.automodsumm.core import AutomodsummOptions, option_str_list
from plasmapy_sphinx.utils import default_grouping_info

if sys.version_info >= (3, 0):
    text_type = str
else:
    text_type = unicode

logger = logging.getLogger(__name__)


_option_spec = {
    **ModuleDocumenter.option_spec,
    "groups": option_str_list,
    "exclude-groups": option_str_list,
    "no-groups": bool_option,
    # "group-order": option_str_list,
    # "merge-groups": bool_option,
    "skip": option_str_list,
    "include-heading": bool_option,
    # "members": lambda x: None,
    "heading-chars": directives.unchanged,
    "toctree": directives.unchanged,
    "no-toctree": bool_option,
    "no-main-docstring": bool_option,
    "inheritance-diagram": bool_option,
    "no-inheritance-diagram": bool_option,
}  # type: Dict[str, Callable]
for option_name in list(_option_spec):
    if "member" in option_name:
        del _option_spec[option_name]
del _option_spec["ignore-module-all"]
del option_name


class AutomodapiOptions(AutomodsummOptions):
    """
    Class for advanced conditioning and manipulation of option arguments of
    `plasmapy_sphinx.autodoc.automodapi.ModAPIDocumenter`.
    """

    option_spec = _option_spec
    logger = logger

    def condition_options(self):
        super().condition_options()
        self.condition_heading_chars_option()
        self.condition_include_heading_option()
        self.condition_inheritance_diagram_option()

    def condition_toctree_option(self):
        """
        Additional conditioning of the ``:toctree:`` option. (See options
        :rst:dir:`automodapi:toctree` and :rst:dir:`automodapi:no-toctree`
        for additional details.)
        """
        if "no-toctree" in self.options and self.options["no-toctree"]:
            if "toctree" in self.options:
                del self.options["toctree"]
        elif "toctree" not in self.options:
            self.options["toctree"] = self.app.config.automodapi_default_toctree_dir

        super().condition_toctree_option()

    def condition_heading_chars_option(self):
        """
        Additional conditioning of the ``:heading-chars:`` option. (See option
        :rst:dir:`automodapi:heading-chars` for additional details.)
        """
        non_alphanumerics = re.compile("[^0-9a-zA-Z]]+")
        heading_chars = self.options.get("heading-chars", None)
        if (
            heading_chars is None
            or heading_chars == ""
            or len(heading_chars) < 2
            or non_alphanumerics.fullmatch(heading_chars) is None
        ):
            self.options["heading-chars"] = "-^"

    def condition_include_heading_option(self):
        """
        Additional conditioning of the ``:include-heading:`` option. (See option
        :rst:dir:`automodapi:include-heading` for additional details.)
        """
        if "include-heading" not in self.options:
            self.options["include-heading"] = False

    def condition_inheritance_diagram_option(self):
        """
        Additional conditioning of the ``:inheritance-diagram:`` option. (See options
        :rst:dir:`automodapi:inheritance-diagram` and
        :rst:dir:`automodapi:no-inheritance-diagram` for additional details.)
        """
        if "no-inheritance-diagram" in self.options:
            self.options["inheritance-diagram"] = False
            del self.options["no-inheritance-diagram"]
        elif "inheritance-diagram" in self.options:
            self.options["inheritance-diagram"] = False
        else:
            self.options[
                "inheritance-diagram"
            ] = self.app.config.automodapi_include_inheritance_diagram

    def condition_group_options(self):
        """
        Additional conditioning of the grouping options. (See options
        :rst:dir:`automodapi:groups`, :rst:dir:`automodapi:exclude-groups`, and
        :rst:dir:`automodapi:no-groups` for additional details.)
        """
        if "no-groups" in self.options and self.options["no-groups"]:
            self.options["groups"] = []
            if "exclude-groups" in self.options:
                del self.options["exclude-groups"]

            return

        super().condition_group_options()

    @property
    def options_for_automodsumm(self) -> Dict[str, Any]:
        """
        A dictionary of options suitable for :rst:dir:`automodsumm` based on the
        options given to :rst:dir:`automodapi`, and excluding the group options.
        """
        options = {}

        asumm_opts = list(AutomodsummOptions.option_spec)
        for name in asumm_opts:
            if name in self.options and name not in ("groups", "exclude-groups"):
                val = self.options[name]
                if isinstance(val, list):
                    val = ", ".join(val)

                if name == "toctree" and self.toctree["original"] is not None:
                    # automodsumm requires path relative to the confdir but
                    # Automodsumm.review_toctree_option generates the path relative
                    # to the file location
                    options[name] = self.toctree["original"]
                else:
                    options[name] = val

        return options


class ModAPIDocumenter(ModuleDocumenter):
    """
    The class that defines the `~sphinx.ext.autodoc` directive :rst:dir:`automodapi`.
    """

    objtype = "modapi"
    """Defines the *auto* directive name.  In this case ``automodapi``."""

    directivetype = "module"
    """Defines the generated directive name. In this case ``.. :py:module::``."""

    titles_allowed = True
    content_indent = ""

    logger = logger
    """
    Instance of the `~sphinx.util.logging.SphinxLoggerAdapter` for report during
    builds.
    """

    option_spec = _option_spec
    """Mapping of option names to validator functions."""

    # Templates used for generated the additional content associated with the
    # directive (e.g. the automodsumm tables)
    _templates = {
        "mod-heading": "\n".join(["{modname} {pkg_or_mod}", "{underline}", ""]),
        "heading": "\n".join(["{title}", "{underline}"]),
        "automodsumm": "\n".join([".. automodsumm:: {modname}", "   :groups: {group}"]),
        "options": "   :{option}: {opt_args}",
        "inheritance-diagram": "\n".join(
            [
                ".. inheritance-diagram:: {cls_list}",
                "   :private-bases:",
                "   :parts: 1",
            ],
        ),
    }

    @property
    def grouping_info(self) -> Dict[str, Dict[str, Union[str, None]]]:
        """
        Dictionary of :rst:dir:`automodapi` and :rst:dir:`automodsumm` group
        information.  The primary key is the group name, e.g. **modules**,
        **classes**, etc.  The value associated with the primary key is a
        dictionary with the following keys:

        +-------------+------------------------------------------------------------+
        | title       | Title used to head the :rst:dir:`automodsumm` table.       |
        +-------------+------------------------------------------------------------+
        | description | Brief description to follow the title.                     |
        +-------------+------------------------------------------------------------+
        | dunder      | Name of the dunder variable used to define a custom group. |
        +-------------+------------------------------------------------------------+
        """

        group_order = tuple(self.env.app.config.automodapi_group_order)
        custom_group_info = self.env.app.config.automodapi_custom_groups

        group_names = set(default_grouping_info) | set(custom_group_info)
        remainder = list(group_names - set(group_order))
        if len(remainder) > 0:
            group_order += tuple(sorted(remainder))

        _grouping_info = OrderedDict()
        for name in group_order:
            if name in default_grouping_info:
                _info = default_grouping_info[name]
            else:
                _info = custom_group_info[name]

            _grouping_info.update(
                {
                    name: {
                        "title": _info.get("title", None),
                        "description": _info.get("description", None),
                        "dunder": _info.get("dunder", None),
                    },
                },
            )

        return _grouping_info

    def generate_more_content(self, modname: str) -> List[str]:
        """
        Generate the "more content" associate with the :rst:dir:`automodsumm` tables
        and inheritance diagrams.

        Parameters
        ----------
        modname : str
            Name of the module being documented (i.e. that given to
            :rst:dir:`automodapi`).

        Returns
        -------
        List[str]
            A list of strings to be added the to the directive's content.
        """
        app = self.env.app
        inheritance_groups = app.config.automodapi_groups_with_inheritance_diagrams

        lines = []

        option_processor = AutomodapiOptions(
            app,
            modname,
            self.options,
            _warn=self.logger.warning,
            docname=self.env.docname,
        )
        asumm_options = option_processor.options_for_automodsumm
        mod_objs = option_processor.mod_objs_option_filtered
        heading_char = (
            option_processor.options["heading-chars"][1]
            if option_processor.options["include-heading"]
            else option_processor.options["heading-chars"][0]
        )
        include_inheritance_diagram = option_processor.options["inheritance-diagram"]

        # scan thru default groups first
        for group, info in self.grouping_info.items():
            if group not in mod_objs:
                continue

            title = info["title"]
            description = info["description"]  # type: str

            underline = heading_char * len(title)

            # sub-heading
            lines.extend(
                self._templates["heading"]
                .format(title=title, underline=underline)
                .splitlines()
            )
            lines.append("")

            # add group description
            if description is not None:
                description = inspect.cleandoc(description)
                descr_list = description.split("\n")
                lines.extend(descr_list)
                lines.append("")

            # add automodsumm directive
            lines.extend(
                self._templates["automodsumm"]
                .format(modname=modname, group=group)
                .splitlines()
            )

            # add options for automodsumm directive
            for name, val in asumm_options.items():
                if name == "toctree" and group == "modules":
                    continue

                lines.extend(
                    self._templates["options"]
                    .format(option=name, opt_args=val)
                    .splitlines()
                )
            lines.append("")

            # add inheritance-diagram
            if group in inheritance_groups and include_inheritance_diagram:
                cls_list = " ".join(mod_objs[group]["qualnames"])
                lines.extend(
                    self._templates["inheritance-diagram"]
                    .format(cls_list=cls_list)
                    .splitlines()
                )
                lines.append("")

        return lines

    def generate_heading(self, modname: str) -> None:
        """
        Generate and place a heading at the top of the directive's content.  If
        ``modname`` is a package then the title will be ``<modname> Package``;
        and if a module (``.py`` file) then the title will be ``<modname> Module``.

        Parameters
        ----------
        modname : str
            Name of the module being documented (i.e. that given to
            :rst:dir:`automodapi`).
        """
        app = self.env.app
        sourcename = self.get_sourcename()

        option_processor = AutomodapiOptions(
            app,
            modname,
            self.options,
            _warn=self.logger.warning,
            docname=self.env.docname,
        )
        if not option_processor.options["include-heading"]:
            return

        modname = re.escape(modname)

        if option_processor.pkg_or_module == "pkg":
            pkg_or_mod = "Package"
        else:
            pkg_or_mod = "Module"

        heading_char = option_processor.options["heading-chars"][0]
        underline = heading_char * (len(modname) + 1 + len(pkg_or_mod))

        heading_lines = (
            self._templates["mod-heading"]
            .format(modname=modname, pkg_or_mod=pkg_or_mod, underline=underline)
            .splitlines()
        )

        for line in heading_lines:
            self.add_line(line, source=sourcename)

    def add_content(
        self, more_content: Optional[StringList], no_docstring: bool = False
    ) -> None:
        """Add content from docstrings, attribute documentation and user."""
        if no_docstring:
            warnings.warn(
                "The 'no_docstring' argument to %s.add_content() is deprecated."
                % self.__class__.__name__,
                RemovedInSphinx50Warning,
                stacklevel=2,
            )

        no_docstring = self.options.get("no-main-docstring", False)

        # set sourcename and add content from attribute documentation
        sourcename = self.get_sourcename()
        if self.analyzer:
            attr_docs = self.analyzer.find_attr_docs()
            if self.objpath:
                key = (".".join(self.objpath[:-1]), self.objpath[-1])
                if key in attr_docs:
                    no_docstring = True
                    # make a copy of docstring for attributes to avoid cache
                    # the change of autodoc-process-docstring event.
                    docstrings = [list(attr_docs[key])]

                    for i, line in enumerate(self.process_doc(docstrings)):
                        self.add_line(line, sourcename, i)

        # add content from docstrings
        if not no_docstring:
            docstrings = self.get_doc()
            if docstrings is None:
                # Do not call autodoc-process-docstring on get_doc() returns None.
                pass
            else:
                if not docstrings:
                    # append at least a dummy docstring, so that the event
                    # autodoc-process-docstring is fired and can add some
                    # content if desired
                    docstrings.append([])
                for i, line in enumerate(self.process_doc(docstrings)):
                    self.add_line(line, sourcename, i)

        # add additional content (e.g. from document), if present
        if more_content:
            for line, src in zip(more_content.data, more_content.items):
                self.add_line(line, src[0], src[1])

    def generate(
        self,
        more_content: Optional[StringList] = None,
        real_modname: str = None,
        check_module: bool = False,
        all_members: bool = False,
    ) -> None:
        """
        Generate reST for the object given by *self.name*, and possibly for
        its members.

        If *more_content* is given, include that content. If *real_modname* is
        given, use that module name to find attribute docs. If *check_module* is
        True, only generate if the object is defined in the module name it is
        imported from. If *all_members* is True, document all members.
        """

        docname = self.env.docname
        if not docname.endswith(".rst"):
            docname += ".rst"

        if not self.parse_name():
            # need a module to import
            logger.warning(
                __(
                    f"don't know which module to import for autodocumenting "
                    f"{self.name} (try placing a 'module' or 'currentmodule' "
                    f"directive in the document, or giving an explicit module name)"
                ),
                type="autodoc",
            )
            return

        # now, import the module and get object to document
        if not self.import_object():
            return

        # If there is no real module defined, figure out which to use.
        # The real module is used in the module analyzer to look up the module
        # where the attribute documentation would actually be found in.
        # This is used for situations where you have a module that collects the
        # functions and classes of internal submodules.
        real_modname = real_modname or self.get_real_modname()  # type: str

        # Generate heading
        self.generate_heading(modname=real_modname)

        # Generate the 'more_content' (automodsumm and inheritance diagrams)
        more_content = StringList()
        more_lines = self.generate_more_content(modname=real_modname)
        for line in more_lines:
            more_content.append(line, source=docname)

        # generate
        super().generate(
            more_content=more_content,
            real_modname=real_modname,
            check_module=check_module,
            all_members=all_members,
        )


def setup(app: Sphinx):
    """Sphinx ``setup()`` function for the :rst:dir:`automodapi` functionality."""

    from plasmapy_sphinx.automodsumm.core import setup as setup_automodsumm

    rtn = setup_automodsumm(app)

    app.setup_extension("sphinx.ext.inheritance_diagram")

    app.add_autodocumenter(ModAPIDocumenter)

    app.add_config_value("automodapi_include_inheritance_diagram", True, True)
    app.add_config_value("automodapi_default_toctree_dir", "api", True)
    app.add_config_value(
        "automodapi_group_order",
        ("modules", "classes", "exceptions", "warnings", "functions", "variables"),
        True,
    )
    app.add_config_value(
        "automodapi_groups_with_inheritance_diagrams",
        ["classes", "exceptions", "warnings"],
        True,
    )

    return rtn
