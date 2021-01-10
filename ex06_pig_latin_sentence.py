from ex05_pig_latin import pig_latin
from typing import List


def pl_sentence(sentence: str) -> str:
    res = []
    for word in sentence.split():
        res.append(pig_latin(word))
    return " ".join(res)


def transpose_list_of_words(list_of_words: List[str]) -> List[str]:
    transposed_list_of_words = zip(*map(lambda x: x.split(), list_of_words))
    return list(map(lambda x: " ".join(x), transposed_list_of_words))


print(f"pl_sentence('this is a test translation')={pl_sentence('this is a test translation')}")
print(f"transpose_list_of_words(['abc def ghi', 'jkl mno pqr', 'stu vwx yz'])={transpose_list_of_words(['abc def ghi', 'jkl mno pqr', 'stu vwx yz'])}")
