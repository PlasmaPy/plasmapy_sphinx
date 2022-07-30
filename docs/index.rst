:tocdepth: 3

.. _plasmapy-sphinx-documentation:

###############################
`plasmapy_sphinx` Documentation
###############################

`plasmapy_sphinx` is a
`Sphinx <https://www.sphinx-doc.org/en/master/>`__ extension package
that contains custom documentation functionality used to document
`PlasmaPy's packages <https://github.com/PlasmaPy>`_ .  The package is
organized in such a way that users can use all available extensions, or
just the select the desired ones.

.. note::

    `plasmapy_sphinx` is not currently released in any form and can
    only be installed directly from its `GitHub repository
    <https://github.com/plasmapy/plasmapy_sphinx>`__.  We do plan to
    release it to https://pypi.org but there is no scheduled release
    date at this time.

    Additionally, this package currently has no tests covering its
    functionality.


.. toctree::
    :caption: First Steps
    :maxdepth: `

    Installing <first_steps/install>
    Configuring <first_steps/configure>

.. toctree::
    :captions: Extensions
    :maxdepth: 1

    Autodoc <ext/autodoc>
    Automodsumm <ext/automodsumm>
    CSS <ext/css>
    Directives <ext/directives>

.. toctree::
    :caption: Contributor Guide
    :maxdepth: 1

.. toctree::
    :caption: All the Rest
    :maxdepth: 1

    changelog/index