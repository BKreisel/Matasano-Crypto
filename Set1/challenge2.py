from binascii import hexlify

def validate(output):
    answer = b"746865206b696420646f6e277420706c6179"
    if output == answer:
        print("Valid Answer")

def equal_xor(hex1,hex2):
    """XOR's hex strings of equal length"""
    hex1 = bytes.fromhex(hex1)
    hex2 = bytes.fromhex(hex2)

    result = bytearray()
    for h1,h2 in zip(hex1,hex2):
        result.append(h1 ^h2)

    return result


def main():
    input_1 = "1c0111001f010100061a024b53535009181c"
    input_2 = "686974207468652062756c6c277320657965"

    output = equal_xor(input_1, input_2)

    print(output)
    validate(hexlify(output))

if __name__ == "__main__":
    main()