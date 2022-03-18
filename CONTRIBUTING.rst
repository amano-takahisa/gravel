.. highlight:: shell

============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every little bit
helps, and credit will always be given.

You can contribute in many ways:

Types of Contributions
----------------------

Report Bugs
~~~~~~~~~~~

Report bugs at https://github.com/amano-takahisa/gravel/issues.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

Fix Bugs
~~~~~~~~

Look through the GitHub issues for bugs. Anything tagged with "bug" and "help
wanted" is open to whoever wants to implement it.

Implement Features
~~~~~~~~~~~~~~~~~~

Look through the GitHub issues for features. Anything tagged with "enhancement"
and "help wanted" is open to whoever wants to implement it.

Write Documentation
~~~~~~~~~~~~~~~~~~~

gravel could always use more documentation, whether as part of the
official gravel docs, in docstrings, or even on the web in blog posts,
articles, and such.

Submit Feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at https://github.com/amano-takahisa/gravel/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

Get Started!
------------

Ready to contribute? Here's how to set up ``gravel`` for local development.

1. Fork the ``gravel`` repo on GitHub.
2. Clone your fork locally::

    $ git clone git@github.com:your_name_here/gravel.git

3. Install your local copy into a conda env. Assuming you have conda installed, this is how you set up your fork for local development::

    $ conda create -n gravel_dev python=3.10
    $ conda activate gravel_dev
    $ pip install -e gravel

4. Create a feature branch for local development
   In this repository, we are using git flow branch model.
   Create a feature branch from ``develop`` branch.

   Without the git-flow extensions::

    $ git checkout develop
    $ git checkout -b name_of_your_bugfix_or_feature

   With the git-flow extensions::

    $ git flow feature start name_of_your_bugfix_or_feature

   Now you can make your changes locally.

5. When you're done making changes, check that your changes pass linters.
   The following command test and fix code style by flake8, black, and isort.::

    $ make lint

6. Update docs
   If you update docs, run the next command to check your update.
   ::

    $ make docs

   This command reflesh html files in ``docs/_build/html``.
   Open html files with browser and check contents.

7. Commit your changes and push your branch to GitHub
   Files under `docs/_build/` is not necessary to add to commits of feature branch.
   Documents will be build from release branch when it is released.::

    $ git add -u
    $ git restore --staged docs/_build/  # unstage _build files
    $ git restore docs/_build/           # rollback
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature

8. Submit a pull request through the GitHub website.

9. Delete ``feature/name_of_your_bugfix_or_feature`` branch after PR is merged to ``develop``

   Remote branch can delete on GitHub.
   To delete local branch, run::

    $ git checkout develop
    $ git pull
    $ git branch -d feature/name_of_your_bugfix_or_feature

Pull Request Guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add the
   feature to the list in README.rst.

Tips
----

To run a subset of tests::

$ pytest tests.test_gravel


Deploying
---------

A reminder for the maintainers on how to deploy.
Make sure all your changes are committed (including an entry in HISTORY.rst).
Then run::

$ bump2version patch # possible: major / minor / patch
$ git push
$ git push --tags

Travis will then deploy to PyPI if tests pass.
