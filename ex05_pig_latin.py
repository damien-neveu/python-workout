

def pig_latin(word: str) -> str:
    if len(word) > 0:
        if is_vowel(word[0]):
            return word + "way"
        else:
            return word[1:] + word[0] + "ay"
    return word


def is_vowel(char: str) -> bool:
    return char in ['a', 'e', 'i', 'o', 'u', 'y']


print(f"pig_latin('eat')={pig_latin('eat')}, pig_latin('computer')={pig_latin('computer')}")

