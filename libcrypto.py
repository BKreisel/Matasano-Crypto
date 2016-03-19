from collections import Counter

def hexstr_xor(hex1, hex2):
    """XOR's hex strings of equal length"""
    hex1 = bytes.fromhex(hex1)
    hex2 = bytes.fromhex(hex2)

    result = bytearray()
    for h1,h2 in zip(hex1,hex2):
        result.append(h1 ^h2)

    return result


def char_xor(key,cipher):
    """XOR's character against hexstring"""
    result = bytearray()
    hex = bytes.fromhex(cipher)

    for byte in hex:
        result.append(byte ^ key)

    return result


def isEnglish(string, threshold=7):
    """ Butcher Frequency Analysis to determine if phrase
        is English Text"""
    string = string.upper()

    english_freq = ["E","T","A","O","I","N","S","H"," "]
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

    if score < threshold:
        return False
    return True