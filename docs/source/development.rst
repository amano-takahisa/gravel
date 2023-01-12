===========
Development
===========

-----
Setup
-----

Clone code from repository.

.. code-block:: bash

   git clone https://github.com/amano-takahisa/gravel


Prepare virtual environment for development
===========================================

Install ``pyenv`` to switch different version of python.
Follow the `official guide <https://github.com/pyenv/pyenv>`_ to install.

Create virtural env to install gravel.

.. code-block::

   python venv gravel/.venv
   source gravel/.venv/bin/activate

Then, prefix ``(.env)`` will be added to PS1 string in your terminal while you are in virtual environment.


Install gravel
==============

Install package from cloned repository into virtual environment with editable mode.

.. code-block:: bash

   pip install -e gravel[dev]


Install pre-commit
==================

``pre-commit`` is a tool which automatically check format, coding style, programming errors etc when you commit codes.

To maintain code quality, enable ``pre-commit`` in the local repository as follows.

.. code-block:: bash

   pre-commit install


Update code
===========
Edit the code as required.
Since ``main`` branch is protected, you need to create a feature branch with following command.

.. code-block:: bash

   git switch -c <feature_branch_name>


Once you have edited the code and updated the corresponding test code, run ``pytest`` to test as follows.

.. code-block:: bash

   # in gravel directory
   pytest

   # pytest with verbose.options
   # pytest -vvs

Following command also check code blocks marked with ``doctest::``.

.. code-block:: bash

   make -C doctests


If your update is document, run following command and confirm that the build is done without error, and open built html files with your browser.

.. code-block:: bash

    make -C docs html

The above code builds only pages which source files are updated from previous build.
If you want to build from scratch, remove a directory ``docs/build`` before `make`.
