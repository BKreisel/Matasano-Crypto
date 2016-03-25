from collections import Counter
from scipy import spatial

from sys import exit

LETTER_FREQ = {
    " " : 0.1831685753,
    "e" : 0.1026665037,
    "t" : 0.0751699827,
    "a" : 0.0653216702,
    "o" : 0.0615957725,
    "n" : 0.0571201113,
    "i" : 0.0566844326,
    "s" : 0.0531700534,
    "r" : 0.0498790855,
    "h" : 0.0497856396,
    "l" : 0.0331754796,
    "d" : 0.0328292310,
    "u" : 0.0227579536,
    "c" : 0.0223367596,
    "m" : 0.0202656783,
    "f" : 0.0198306716,
    "w" : 0.0170389377,
    "g" : 0.0162490441,
    "p" : 0.0150432428,
    "y" : 0.0142766662,
    "b" : 0.0125888074,
    "v" : 0.0079611644,
    "k" : 0.0056096272,
    "x" : 0.0014092016,
    "j" : 0.0009752181,
    "q" : 0.0008367550,
    "z" : 0.0005128469
}


def verify_bytearray(object):
    if object.__class__.__name__ != "bytearray":
        raise TypeError("Input Not ByteArray")


def xor(a, b):
    """ XOR bytearray's """

    verify_bytearray(a)
    verify_bytearray(b)

    if len(a) < len(b):
        key = a
        bytestr = b
    else:
        key = b
        bytestr = a

    result = bytearray()
    idx = 0

    for char in bytestr:
        x = idx % len(key)
        xor_val = key[x] ^ char
        result.append(xor_val)
        idx += 1

    return result


def freq_score(string):
    score = 0
    for char in string.lower():
        if char in LETTER_FREQ:
            score += LETTER_FREQ[char] * 100
    return score


def hamming_distance(a, b):

    verify_bytearray(a)
    verify_bytearray(b)

    if len(a) != len(b):
        raise ValueError("Inputs are of unequal length")

    xored = xor(a, b)
    count = Counter()
    for byte in xored:
        bin_str = str(bin(byte)[2:])
        count.update(list(bin_str))

    return count['1']


def split_blocks(key, data):

    verify_bytearray(data)
    blocks, block = [], bytearray()

    for ctr in range(0,len(data)):
        if ctr % key == 0:
            blocks.append(block)
            block = bytearray()
        block.append(data[ctr])

    return blocks[1:]


def pkcs7(input, blockSize=8):

    verify_bytearray(input)

    input_length = len(input)

    if input_length < blockSize:
        pad = blockSize - input_length
    else:
        pad = blockSize % input_length

    for char in range(0, pad):
        input.append(pad)

    return input
