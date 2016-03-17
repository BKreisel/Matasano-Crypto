import base64

def validate(output):
    answer = b"SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
    if output == answer:
        print("Valid Answer")

def main():
    input = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

    output = bytes.fromhex(input)
    output = base64.b64encode(output)
    
    print(output)
    validate(output)

if __name__ == "__main__":
    main()