Docker Utils 
========

  === **Under Development** ===

Supported Platforms :

 - Linux
 - Windows (Not tested yet)

Pre-requisites
-------
1. Python 3 and pip3
2. Docker

Preparing for Development
--------------------------
1. Ensure ``pip``, and ``pipenv`` are installed.
2. Clone the repo
3. Fetch development dependencies : ``make install``

Usage
-----

::

  $ docker-utils  

Running Tests :
--------------

::

  $  make


Build :
-------
Build a wheel

::

    $ python setup.py bdist_wheel
    $ ls dist/hybr-0.1.0-py2.py3-none-any.whl

