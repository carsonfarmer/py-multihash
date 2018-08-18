=====
Usage
=====

To use py-multihash in a project::

    from base64 import b64encode

    import multihash

    buf = bytes.fromhex('0beec7b5ea3f0fdbc95d0dd47f3c5bc275da8a33')
    encoded = multihash.encode(buf, 'sha1')
    # b'\x11\x14\x0b\xee\xc7\xb5\xea?\x0f\xdb\xc9]\r\xd4\x7f<[\xc2u\xda\x8a3'

    multihash.decode(encoded)
    # {'code': 17,
    # 'digest': b'\x0b\xee\xc7\xb5\xea?\x0f\xdb\xc9]\r\xd4\x7f<[\xc2u\xda\x8a3',
    # 'length': 20,
    # 'name': 'sha1'}


