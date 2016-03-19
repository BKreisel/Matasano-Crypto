from libcrypto import char_xor
from libcrypto import isEnglish


def main():

    for line in open("../assets/inputS1C4.txt","r"):
        for i in range(1,int("ff",16)):
            xor_bytes = char_xor(i,line.rstrip())

            try:
                xor_string = xor_bytes.decode("ascii")

                if isEnglish(xor_string,threshold=10):
                    print("[+] Key: {0:#x} | Text: {1} | Ciphertext: {2}".format(i, xor_string, line))
            except UnicodeDecodeError:
                next

if __name__ == "__main__":
    main()