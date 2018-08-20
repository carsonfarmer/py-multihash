"""
 Multihash tests.
"""

from binascii import hexlify

import base58
import pytest

import multihash


class TestHexString:
    def test_valid_to_hex_string(self, valid):
        for case in valid:
            code = case['encoding']['code']
            buf = multihash.encode(bytes.fromhex(case['hex']), code)
            assert multihash.to_hex_string(buf) == hexlify(buf).decode()

    def test_invalid_to_hex_string(self):
        # In actual fact, type checking should catch this for us
        with pytest.raises(TypeError):
            multihash.to_hex_string('hello world')

    def test_valid_from_hex_string(self, valid):
        for case in valid:
            code = case['encoding']['code']
            buf = multihash.encode(bytes.fromhex(case['hex']), code)
            assert multihash.from_hex_string(hexlify(buf).decode()) == buf


class TestBase58String:
    def test_valid_to_b58_string(self, valid):
        for case in valid:
            code = case['encoding']['code']
            buf = multihash.encode(bytes.fromhex(case['hex']), code)
            # Currently a lame test, but good for regression testing if we change our underlying base58 lib
            assert multihash.to_b58_string(buf) == base58.b58encode(buf).decode()

    def test_invalid_to_b58_string(self):
        # In actual fact, type checking should catch this for us
        with pytest.raises(TypeError):
            multihash.to_b58_string('hello world')

    def test_valid_from_b58_string(self):
        src = 'QmPfjpVaf593UQJ9a5ECvdh2x17XuJYG5Yanv5UFnH3jPE'
        expected = bytes.fromhex('122013bf801597d74a660453412635edd8c34271e5998f801fac5d700c6ce8d8e461')
        assert multihash.from_b58_string(src) == expected


def sample(code, size, hexi):
    return code.to_bytes((code.bit_length() + 7) // 8, byteorder='big') + \
           size.to_bytes((size.bit_length() + 7) // 8, byteorder='big') + \
           bytes.fromhex(hexi)


class TestDecode:
    def test_valid_decode(self, valid):
        for case in valid:
            code = case['encoding']['code']
            buf = sample(code, case['size'], case['hex'])
            name = case['encoding']['name']
            d1 = bytes.fromhex(case['hex'])

            r = multihash.decode(buf)
            d2 = r['digest']

            assert r['code'] == code
            assert r['name'] == name
            assert r['length'] == len(d1)
            assert d1 == d2

    def test_invalid_decode(self):
        # In actual fact, type checking should catch this for us
        with pytest.raises(TypeError):
            multihash.decode('hello')


class TestEncode:
    def test_valid_encode(self, valid):
        for case in valid:
            code = case['encoding']['code']
            buf = sample(code, case['size'], case['hex'])
            name = case['encoding']['name']
            results = [
                multihash.encode(bytes.fromhex(case['hex']), code),
                multihash.encode(bytes.fromhex(case['hex']), name)
            ]

            for result in results:
                assert hexlify(result) == hexlify(buf)

    def test_invalid_encode(self):
        # In actual fact, type checking should catch these for us
        with pytest.raises(TypeError):
            multihash.encode()
        with pytest.raises(TypeError):
            multihash.encode('hello', 0x11)
        with pytest.raises(ValueError):
            multihash.encode('hello'.encode(), 0x11, 2)


class TestValidate:
    def test_valid_validate(self, valid):
        for case in valid:
            assert multihash.validate(sample(case['encoding']['code'], case['size'], case['hex'])) is True

    def test_invalid_validate(self, invalid):
        for case in invalid:
            assert multihash.validate(sample(case['code'], case['size'], case['hex'])) is False

        # bytes array of length 150
        long_buffer = bytes(150)
        assert multihash.validate(long_buffer) is False


class TestIsValidCode:
    def test_valid_is_valid_code(self):
        assert multihash.is_valid_code(2) is True
        assert multihash.is_valid_code(0x13) is True

    def test_invalid_is_valid_code(self):
        assert multihash.is_valid_code(0x10) is False
        assert multihash.is_valid_code(0x90) is False


class TestIsAppCode:
    def test_valid_is_app_code(self):
        for n in range(1, 0x10):
            assert multihash.is_app_code(n) is True

    def test_invalid_is_app_code(self):
        assert multihash.is_app_code(0) is False

        for m in range(0x10, 0xff + 1):
            assert multihash.is_app_code(m) is False


class TestCoerceCode:
    def test_valid_coerce_code(self):
        names = {
            'sha1': 0x11,
            'sha2-256': 0x12,
            'sha2-512': 0x13,
            'sha3-512': 0x14
        }
        for name in names:
            assert multihash.coerce_code(name) == names[name]
            # Should also work for codes
            assert multihash.coerce_code(names[name]) == names[name]

    def test_invalid_coerce_code(self):
        invalid_names = [
            'sha256',
            'sha9',
            'Blake4b'
        ]

        for name in invalid_names:
            with pytest.raises(ValueError):
                multihash.coerce_code(name)

        with pytest.raises(TypeError):
            multihash.coerce_code(b'hello world')

        with pytest.raises(ValueError):
            multihash.coerce_code(0x99)


class TestPrefix:
    def test_valid_prefix(self):
        mhash = multihash.encode(b'hey', 0x11, 3)
        prefix = multihash.prefix(mhash)
        assert hexlify(prefix).decode() == '1103'

    def test_invalid_prefix(self):
        with pytest.raises(ValueError):
            multihash.prefix(b'definitely not valid')


class TestConstants:
    def test_has_constants(self):
        from multihash.constants import names, codes, default_lengths
        assert len(names.keys()) > 0
        assert len(codes.keys()) > 0
        assert len(default_lengths.keys()) > 0
