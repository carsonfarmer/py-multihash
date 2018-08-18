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
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|

.. |docs| image:: https://readthedocs.org/projects/py-multihash/badge/?style=flat
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

.. |version| image:: https://img.shields.io/pypi/v/multihash.svg
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/multihash

.. |wheel| image:: https://img.shields.io/pypi/wheel/multihash.svg
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/multihash

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/multihash.svg
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/multihash

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/multihash.svg
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/multihash


.. end-badges

Multihash implementation in Python

* Free software: MIT license

Installation
============

::

    pip install multihash

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
