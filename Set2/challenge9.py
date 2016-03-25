from libcrypto import pkcs7

def validate(output):
    answer = b"YELLOW SUBMARINE\x04\x04\x04\x04"
    if output == answer:
        print("Valid Answer")

def main():
    input = b"YELLOW SUBMARINE"

    output = pkcs7(bytearray(input),blockSize=20)

    print(output)
    validate(output)

if __name__ == "__main__":
    main()