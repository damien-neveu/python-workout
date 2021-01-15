from typing import Sequence


def firstlast(seq: Sequence) -> Sequence:
    return seq if len(seq) <= 1 else seq[:1] + seq[-1:]


print(f"firstlast('abc')={firstlast('abc')}, firstlast([1,2,3,4])={firstlast([1,2,3,4])}, firstlast(('a','b','c'))={firstlast(('a','b','c'))}")
