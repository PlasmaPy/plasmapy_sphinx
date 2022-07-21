"""
This sub-package defines
`directives
<https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html>`_
and
`roles
<https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html>`_
that do not fall under the scopes of `~plasmapy_sphinx.autodoc` or
`~plasmapy_sphinx.automodsumm`.  If a directive that has an associated role,
then that role is used for cross-referencing the declared item.  For example,
``:meth:`Foo.bar``` is a cross-referencing role to link back to where
``.. automethod:: Foo.bar`` was declared.

+-------------------------+-----------------------+------------------------------------+
| Directive               | Role                  | Description                        |
+=========================+=======================+====================================+
| | :rst:dir:`confval`    | | :rst:role:`confval` | For declaring and referencing      |
| | ``.. confval:: name`` | | ``:confval:`name``` | Sphinx configuration values.       |
+-------------------------+-----------------------+------------------------------------+
| | :rst:dir:`event`      | | :rst:role:`event`   | For declaring and referencing      |
| | ``.. event:: name``   | | ``:event:`name```   | Sphinx events.                     |
+-------------------------+-----------------------+------------------------------------+

"""
from plasmapy_sphinx.directives import confval, event
