from ex05_pig_latin import is_vowel


def ubbi_dubbi(word: str) -> str:
    res = []
    for char in word:
        if is_vowel(char):
            res.append(f"ub{char}")
        else:
            res.append(char)
    return "".join(res)


print(f"ubbi_dubbi('octopus')={ubbi_dubbi('octopus')}, ubbi_dubbi('soap')={ubbi_dubbi('soap')}")
