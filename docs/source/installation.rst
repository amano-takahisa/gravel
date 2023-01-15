============
Installation
============

Install dependencies.

..  code-block:: bash

   sudo apt-get install gdal-bin libgdal-dev python3-pip python3-numpy make

Then install ``gravel``.

.. code-block:: bash

   git clone --depth=1 https://github.com/amano-takahisa/gravel
   pip install gravel

Plotting features are extra. If you want to plot, add a ``[plot]`` option.

.. code-block:: bash

   pip install gravel[plot]
