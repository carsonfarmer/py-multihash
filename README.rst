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

`Multihash <https://github.com/multiformats/multihash>`_ implementation in Python

Multihash is a protocol for differentiating outputs from various well-established cryptographic hash functions,
addressing size + encoding considerations.

It is useful to write applications that future-proof their use of hashes, and allow multiple hash functions to coexist.
See `jbenet/random-ideas#1 <https://github.com/jbenet/random-ideas/issues/1>`_ for a longer discussion.

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

Contributing
============

See our `contribution guidelines <CONTRIBUTING.rst>`_ for a development workflow and details on how to contribute.

Notes
=====

This package is a direct port of the official `Node/Javascript version <https://github.com/multiformats/js-multihash>`_.
As this projects matures, it may become more 'Pythonic'.

**Obsolete and deprecated hash functions are included** in this package. `MD4`, `MD5` and `SHA-1` should no longer be
used for cryptographic purposes, but since many such hashes already exist they are included in the multihash
specification and may be implemented in multihash libraries such as this one.
