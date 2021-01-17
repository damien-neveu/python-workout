from typing import Sequence, List, Tuple
from functools import reduce


def firstlast(seq: Sequence) -> Sequence:
    return seq if len(seq) <= 1 else seq[:1] + seq[-1:]


def even_odd_sums(nums: Sequence[int]) -> Sequence[int]:
    if not nums:
        return [0, 0]
    elif len(nums) == 1:
        return [nums[0], 0]
    else:
        return [reduce(lambda a, b: a+b, nums[::2]),
                reduce(lambda a, b: a+b, nums[1::2])]


def myzip(*seqs: Sequence) -> List[Tuple]:
    """assume all of the input iterables are of the same length"""
    if not seqs:
        return []
    else:
        res = []
        first_seq = seqs[0]
        for index, elem in enumerate(first_seq):
            curr_tuple = [elem]
            for seq in seqs[1:]:
                curr_tuple.append(seq[index])
            res.append(tuple(curr_tuple))
        return res


print(f"firstlast('abc')={firstlast('abc')}, firstlast([1,2,3,4])={firstlast([1,2,3,4])}, firstlast(('a','b','c'))={firstlast(('a','b','c'))}")
print(f"even_odd_sums([10, 20, 30, 40, 50, 60])={even_odd_sums([10, 20, 30, 40, 50, 60])}")
print(f"myzip([10, 20,30], 'abc', (0.1, 0.2, 0.3))={myzip([10, 20,30], 'abc', (0.1, 0.2, 0.3))}")
