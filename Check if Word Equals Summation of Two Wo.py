from itertools import zip_longest
from string import ascii_lowercase

def isSumEqual(firstWord: str, secondWord: str, targetWord: str) -> bool:
    firstVal, secVal, thirdVal = "", "", ""
    vals = {'a': '0','b':'1','c':'2','d':'3','e':'4','f':'5','g':'6','h':'7','i':'8','j':'9', 'space': ' '}

    for (x, y, z) in zip_longest(firstWord, secondWord, targetWord, fillvalue='space'):
        firstVal += vals[x]
        secVal += vals[y]
        thirdVal += vals[z]
    if int(thirdVal) == int(firstVal) + int(secVal):
        return True
    return False


