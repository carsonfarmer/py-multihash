#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
Multihash implementation in Python.
"""

from binascii import hexlify
from typing import Any
from typing import Dict
from typing import Optional
from typing import Union

import base58

from . import constants
from . import varint


def to_hex_string(multihash: bytes) -> str:
    """
    Convert the given multihash to a hex encoded string.

    :param multihash: The input multihash as an array of bytes.
    :return: Output hex string representation of input hash.
    """
    return hexlify(multihash)


def from_hex_string(multihash: str) -> bytes:
    """
    Convert the given hex encoded string to a multihash.

    :param multihash: The input multihash as a hex encoded string.
    :return: Output byte array representation of input hash.
    """
    return bytes.fromhex(multihash)


def to_b58_string(multihash: bytes) -> str:
    """
    Convert the given multihash to a base58 encoded string.

    :param multihash: The input multihash as an array of bytes.
    :return: Output Base58 encoded string representation of input hash.
    """
    if not isinstance(multihash, bytes):
        raise TypeError('input must be bytes array')
    return base58.b58encode(multihash).decode()


def from_b58_string(multihash: str) -> bytes:
    """
    Convert the given base58 encoded string to a multi-hash.

    :param multihash: The input multihash as a base58 encoded string.
    :return: Output byte array representation of input hash.
    """
    if not isinstance(multihash, str):
        raise TypeError('input must be string')
    return base58.b58decode(multihash)


# TODO: Should this return a namedtuple instead of a dict to match JS syntax?
def decode(buf: bytes) -> Dict[str, Any]:
    """
    Decode a hash from the given multihash.

    :param buf: Input multihash as an array of bytes.
    :return: Dictionary of type {code: int, name: str, length: int, digest: bytes}
    """
    if not isinstance(buf, bytes):
        raise TypeError('multihash should be `bytes` object')

    if len(buf) < 3:
        raise ValueError('multihash too short. must be > 3 bytes.')

    code, n = varint.from_varint(buf)
    if not is_valid_code(code):
        raise ValueError('multihash unknown function code: {code}'.format(code=code))

    length, n = varint.from_varint(buf, n)
    if length < 1:
        raise ValueError('multihash invalid length: {length}'.format(length=length))

    buf = buf[n:]

    if len(buf) != length:
        raise ValueError('multihash length inconsistent: {} != {}'.format(len(buf), length))

    return dict(code=code, name=constants.codes[code], length=length, digest=buf)


def encode(digest: bytes, code: Union[str, int], length: Optional[int] = None) -> bytes:
    """
    Encode a hash digest along with the specified function code.

    :param digest: Input hash digest as an array of bytes.
    :param code: The hash function code as an int or string.
    :param length: The digest length. Defaults to None, in which case length is derived from the digest itself.
    :return: Output digest bytes array.
    """
    # Ensure it's a hash function code.
    hash_function = coerce_code(code)

    if not isinstance(digest, bytes):
        raise TypeError('digest should be `bytes` object')

    length = len(digest) if length is None else length

    if length != len(digest):
        raise ValueError('digest length should be equal to specified length')

    return varint.to_varint(hash_function) + varint.to_varint(length) + digest


def coerce_code(name: Union[str, int]):
    """
    Converts a hash function name into the matching code.

    If passed a number it will return the number if it's a valid code.

    :param name: The input hash function code.
    :return: Output hash function number/code.
    """
    code = name
    if isinstance(name, str):
        if name not in constants.names:
            raise ValueError('Unrecognized hash function name: {name}'.format(name=name))
        code = constants.names[name]

    if not isinstance(code, int):
        raise TypeError('Hash function code should be a number. Got: {code}'.format(code=code))

    if code not in constants.codes and not is_app_code(code):
        raise ValueError('Unrecognized function code: {code}'.format(code=code))

    return code


def is_app_code(code: int) -> bool:
    """
    Checks whether a code is part of the app range.

    :param code: Code to check.
    :return: Boolean indicating whether `code` is within the app range.
    """
    return 0 < code < 0x10


def is_valid_code(code: int) -> bool:
    """
    Checks whether a multihash code is valid.

    :param code: Code to check.
    :return: Boolean indicating whether `code` is a valid multihash code.
    """

    if is_app_code(code):
        return True

    if code in constants.codes:
        return True

    return False


def validate(multihash: bytes) -> bool:
    """
    Check if the given buffer is a valid multihash.

    :param multihash: Input multihash bytes array.
    :return: Boolean indicating if input in  a valid multihash.
    """
    try:
        decode(multihash)
        return True
    except ValueError:
        return False


def prefix(multihash: bytes) -> bytes:
    """
    Returns a prefix from a valid multihash. Throws an error if it is not valid.

    :param multihash: Input multihash bytes array.
    :return: Bytes array with multihash prefix.
    """
    if validate(multihash):
        return multihash[:2]
    raise ValueError('invalid multihash')
