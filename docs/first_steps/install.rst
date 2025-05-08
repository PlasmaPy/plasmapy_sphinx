.. _plasmapy-install:

.. |minpython| replace:: 3.8

.. _git: https://git-scm.com/
.. |git| replace:: git_

.. _pip: https://pip.pypa.io
.. |pip| replace:: pip_

.. _Python: https://www.python.org/
.. |Python| replace:: Python_

.. _PyPI: https://pypi.org/
.. |PyPI| replace:: PyPI_

.. _`Github repository`: https://github.com/PlasmaPy/plasmapy_sphinx
.. |Github repository| replace:: `Github repository`_

.. role:: py(code)
    :language: python

.. role:: bash(code)
   :language: bash

****************************
Installing `plasmapy_sphinx`
****************************

`plasmapy_sphinx` requires a minimum |Python| version of |minpython|. If
you do not have |Python| installed already, here are the instructions
to `download Python`_ and install it. 🐍

.. contents:: Contents
   :local:

.. _install-pip:

Installing with pip
===================

To install the most recent release of `plasmapy_sphinx` on |PyPI| with
|pip| into an existing |Python| |minpython|\ + environment on macOS or
Linux, open a terminal and run:

.. code-block:: bash

   python -m pip install plasmapy

On some systems, it might be necessary to specify the |Python| version
number by using ``python3``, ``python3.8``, ``python3.9``,
``python3.10``, or ``python3.11`` instead of ``python``.

To install PlasmaPy on Windows, run:

.. code-block:: bash

   py -3.11 -m pip install plasmapy

The version of |Python| may be changed from ``3.11`` to another supported
Python |minpython|\ + release that has been installed on your computer.

For more detailed information, please refer to this tutorial on
`installing packages`_.

Installing from source code
===========================

Obtaining official releases
---------------------------

A ZIP_ file containing the source code for official releases of
`plasmapy_sphinx` can be obtained `from PyPI`_.

Alternatively, official releases can be downloaded from the releases_
page on the |GitHub repository|.

Obtaining source code from GitHub
---------------------------------

If you have |git| installed on your computer, you may clone the
|Github repository| and access the source code from the most
recent development version by running:

.. code-block:: bash

   git clone https://github.com/PlasmaPy/plasmapy_sphinx.git

The repository will be cloned inside a new subdirectory called
:file:`plasmapy_sphinx`.

If you do not have |git| installed on your computer, then you may
download the most recent source code from |Github repository|
by going to :guilabel:`Code` and selecting :guilabel:`Download ZIP`.
`Unzipping <https://www.wikihow.com/Unzip-a-File>`__ the file will
create a subdirectory called :file:`plasmapy_sphinx` that contains the
source code.

Building and installing
-----------------------

To install the downloaded version of `plasmapy_sphinx`, enter the
:file:`plasmapy_sphinx` directory and run:

.. code-block:: bash

   pip install .

If you expect to occasionally edit the source code, instead run:

.. code-block:: bash

   pip install -e .

The ``-e`` flag makes the installation editable.

.. note::

   If you noticed any places where the installation instructions could
   be improved or have become out of date, please `create an issue`_ on
   |Github repository|. It would really help!

.. _clone a repository using SSH: https://docs.github.com/en/get-started/getting-started-with-git/about-remote-repositories#cloning-with-ssh-urls
.. _create an issue: https://github.com/PlasmaPy/plasmapy_sphinx/issues/new
.. _download Python: https://www.python.org/downloads
.. _from PyPI: https://pypi.org/project/plasmapy_sphinx
.. _installing packages: https://packaging.python.org/en/latest/tutorials/installing-packages/#installing-from-vcs
.. _releases: https://github.com/PlasmaPy/plasmapy_sphinx/releases
.. _virtual environment: https://realpython.com/python-virtual-environments-a-primer
.. _ZIP: https://en.wikipedia.org/wiki/ZIP_(file_format)
