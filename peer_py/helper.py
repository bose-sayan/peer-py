def byte_str_to_int(byteStr):
    return int.from_bytes(byteStr, byteorder="big")


def byte_str_to_hex(byteStr):
    return byteStr.hex()
