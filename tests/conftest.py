"""
py-multihash test fixtures.
"""

import pytest


@pytest.fixture()
def invalid():
    return [
        {
            'code': 0x00,
            'size': 32,
            'hex': '0beec7b5ea3f0fdbc95d0dd47f3c5bc275da8a33'
        }, {
            'code': 0x11,
            'size': 21,
            'hex': '0beec7b5ea3f0fdbc95d0dd47f3c5bc275da8a33'
        }, {
            'code': 0x11,
            'size': 20,
            'hex': '0beec7b5ea3f0fdbc95d0dd47f3c5bc275da8a'
        }, {
            'code': 0x11,
            'size': 20,
            'hex': ''
        }, {
            'code': 0x31,
            'size': 20,
            'hex': '0beec7b5ea3f0fdbc95d0dd47f3c5bc275da8a33'
        }, {
            'code': 0x12,
            'size': 32,
            'hex': '2c26b46b68ffc68ff99b453c1d30413413422d706483bfa0f98a5e886266e7'
        }, {
            'code': 0xb205,
            'size': 5,
            'hex': '2c26b32a'
        }, {
            'code': 0xb23f,
            'size': 0x3f,
            'hex': '2c26b46b68ffc68ff99b453c1d30413413422d706483bfa0f98a5e886266e72c26b46b68ffc68ff99b45'
        }
    ]


@pytest.fixture()
def valid():
    return [
        {
            'encoding': {
                'code': 0x11,
                'name': 'sha1'
            },
            'hex': '0beec7b5ea3f0fdbc95d0dd47f3c5bc275da8a33',
            'size': 20
        }, {
            'encoding': {
                'code': 0x11,
                'name': 'sha1'
            },
            'hex': '0beec7b8',
            'size': 4
            }, {
            'encoding': {
                'code': 0x12,
                'name': 'sha2-256'
            },
            'hex': '2c26b46b68ffc68ff99b453c1d30413413422d706483bfa0f98a5e886266e7ae',
            'size': 32
        }, {
            'encoding': {
                'code': 0x12,
                'name': 'sha2-256'
            },
            'hex': '2c26b46b',
            'size': 4
        }
    ]
