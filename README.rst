========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |requires|
        | |coveralls| |codecov|

.. |docs| image:: https://readthedocs.org/projects/py-multihash/badge/?style=flat&version=latest
    :target: https://readthedocs.org/projects/py-multihash
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/carsonfarmer/py-multihash.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/carsonfarmer/py-multihash

.. |requires| image:: https://requires.io/github/carsonfarmer/py-multihash/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/carsonfarmer/py-multihash/requirements/?branch=master

.. |coveralls| image:: https://coveralls.io/repos/carsonfarmer/py-multihash/badge.svg?branch=master&service=github
    :alt: Coverage Status
    :target: https://coveralls.io/r/carsonfarmer/py-multihash

.. |codecov| image:: https://codecov.io/github/carsonfarmer/py-multihash/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/carsonfarmer/py-multihash

.. end-badges

Multihash implementation in Python


License
=======

`MIT Licensed <LICENSE>`_ © 2018 Carson Farmer, 2016 Protocol Labs Inc.

Installation
============

::

    pip install git+https://github.com/carsonfarmer/py-multihash

Documentation
=============

https://py-multihash.readthedocs.io/

Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
