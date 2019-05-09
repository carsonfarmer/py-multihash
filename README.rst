========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - tests
      - | |travis| |requires|
        | |coveralls| |codecov|

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

Notice
=======

There are other Python implementations of multihash out there, including https://github.com/ivilata/pymultihash, https://github.com/multiformats/py-multihash, and at one point, https://github.com/tehmaze/python-multihash. These versions will likely be similar, with minor differences. Currently, it looks like https://github.com/ivilata/pymultihash is the one to use (see https://github.com/libp2p/py-libp2p).

License
=======

`MIT Licensed <LICENSE>`_ © 2018 Carson Farmer, 2016 Protocol Labs Inc.

Installation
============

::

    pip install git+https://github.com/carsonfarmer/py-multihash

Contributing
============

This package is no longer maintained. If you'd like to contribute, see one of the options above, or fork this one!

Notes
=====

This package is a direct port of the official `Node/Javascript version <https://github.com/multiformats/js-multihash>`_.
As this projects matures, it may become more 'Pythonic'.

**Obsolete and deprecated hash functions are included** in this package. `MD4`, `MD5` and `SHA-1` should no longer be
used for cryptographic purposes, but since many such hashes already exist they are included in the multihash
specification and may be implemented in multihash libraries such as this one.
