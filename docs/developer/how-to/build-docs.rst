Build the docs using sphinx
===========================

You can build the `sphinx`_ based docs from the project directory by running::

    $ docs/make_docs.sh

This will build the static docs on the ``docs`` directory.


The docs will be built into the ``build/html`` directory, and can be opened
locally with a web browse::

    $ firefox build/html/index.html

Autobuild
---------

You can also run an autobuild process, which will watch your ``docs``
directory for changes and rebuild whenever it sees changes, reloading any
browsers watching the pages::

    $ sphinx-autobuild -T docs build/html

You can view the pages at localhost::

    $ firefox http://localhost:8000

If you are making changes to source code too, you can tell it to watch
changes in this directory too::

    $ tox -e docs autobuild -- --watch src

.. _sphinx: https://www.sphinx-doc.org/