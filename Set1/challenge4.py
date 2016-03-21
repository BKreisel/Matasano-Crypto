from libcrypto import xor
from libcrypto import freq_score


def main():

    solutions = []
    for line in open("../assets/inputS1C4.txt","r"):

        for i in range(1,int("ff",16)):
            key = bytes({i})
            xor_bytes = xor(bytearray(key), bytearray.fromhex(line.rstrip()))
            try:
                xor_string = xor_bytes.decode("ascii")
                solutions.append([key,xor_string,freq_score(xor_string)])
            except UnicodeDecodeError:
                next

    print("Possible Solutions...\n")
    solutions.sort(key=lambda x: x[2], reverse=True)
    solutions = solutions[:1]

    for solution in solutions:
        print("[+] Key: {0:#x} | Text: {1}".format(solution[0][0], solution[1]))

if __name__ == "__main__":
    main()