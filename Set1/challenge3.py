from collections import Counter

def single_xor(key,cipher):
    result = bytearray()
    hex = bytes.fromhex(cipher)

    for byte in hex:
        result.append(byte ^ key)

    return result


def isEnglish(string):

    string = string.upper()

    english_freq = ["E","T","A","O","I","N","S","H"]
    symbols = ["+",",","`","~","!","@","*"]
    words = ["THE"," BE "," TO "," OF ","AND"," A "," IN "]

    counter = Counter(string)
    high_freq = counter.most_common(8)

    score = 0

    for letter, freq in counter.items():
        percentage = float(freq)/float(len(string))

        if letter in english_freq:
                score += 1
        if letter in symbols:
                score -= 1

    has_word = False
    for word in words:
        if word in string:
            score += 1
            has_word = True

    if not has_word:
        score -=2

    if score < 7:
        return False
    return True


def main():
    input = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

    print("Possible Solutions...\n")
    for i in range(1,int("ff",16)):
        xor_bytes = single_xor(i,input)

        try:
            xor_string = xor_bytes.decode("ascii")
        except UnicodeDecodeError:
            next

        if isEnglish(xor_string):
            print("[+] Key: {0:#x} | Text: {1}".format(i,xor_string))

if __name__ == "__main__":
    main()