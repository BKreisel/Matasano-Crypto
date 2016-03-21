from libcrypto import xor
from libcrypto import freq_score
from binascii import hexlify

def main():
    input = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

    print("Possible Solutions...\n")
    solutions = []
    for i in range(1,int("ff",16)):
        key = bytes({i})
        xor_bytes = xor(bytearray(key),bytearray(bytes.fromhex(input)))

        try:
            xor_string = xor_bytes.decode("ascii")
        except UnicodeDecodeError:
            next
        solutions.append([key, xor_string, freq_score(xor_string)])

    solutions.sort(key=lambda x: x[2], reverse=True)
    solutions = solutions[:1]

    for solution in solutions:
        print("[+] Key: {0:#x} | Text: {1}".format(bytes({solution[0]}), solution[1]))

if __name__ == "__main__":
    main()