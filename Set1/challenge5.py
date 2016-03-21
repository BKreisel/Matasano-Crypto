from libcrypto import xor
from binascii import hexlify


def validate(output):
    answer = "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272"
    answer += "a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"
    answer = bytearray.fromhex(answer)

    if output == answer:
        print("Valid Answer")


def main():
    input = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"

    key = "ICE"
    ctr = 0

    output = xor(bytearray(key.encode()), bytearray(input.encode()))

    print(hexlify(output))
    validate(output)

if __name__ == "__main__":
    main()