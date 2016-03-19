from libcrypto import char_xor
from libcrypto import isEnglish

def main():
    input = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

    print("Possible Solutions...\n")
    for i in range(1,int("ff",16)):
        xor_bytes = char_xor(i,input)

        try:
            xor_string = xor_bytes.decode("ascii")
        except UnicodeDecodeError:
            next

        if isEnglish(xor_string):
            print("[+] Key: {0:#x} | Text: {1}".format(i,xor_string))

if __name__ == "__main__":
    main()