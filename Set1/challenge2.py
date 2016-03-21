from binascii import hexlify
from libcrypto import xor

def validate(output):
    answer = b"746865206b696420646f6e277420706c6179"
    if output == answer:
        print("Valid Answer")

def main():
    input_1 = bytearray(bytes.fromhex("1c0111001f010100061a024b53535009181c"))
    input_2 = bytearray(bytes.fromhex("686974207468652062756c6c277320657965"))

    output = xor(input_1, input_2)

    print(output)
    validate(hexlify(output))

if __name__ == "__main__":
    main()