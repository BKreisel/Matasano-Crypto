from libcrypto import split_blocks
from collections import Counter
from operator import itemgetter

def main():

    print("Possible Solutions...\n")
    for line in open("../assets/inputS1C8.txt","r"):
        bline = bytearray(bytes.fromhex(line.rstrip()))

        blocks = split_blocks(16, bline)
        blocks = [bytes(block) for block in blocks]
        block_counts = Counter(blocks)
        block_counts = [(idx,block_counts[idx]) for idx in blocks]

        max_block = sorted(block_counts,key=itemgetter(1), reverse=True)[:1]

        if max_block[0][1] > 1:
            print("[+] Possible ECB Mode Detected for line: | {0}".format(line))


if __name__ == "__main__":
    main()