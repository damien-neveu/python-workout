from functools import reduce
from typing import List


def mysum(*nums: int) -> int:
    return reduce(lambda a, b: a+b, nums)


def mysum2(nums: List[int], start_value: int = 0) -> int:
    return mysum(*nums) + start_value


print(mysum(1, 2, 3, 4, 5))
print(f"mysum2([1, 2, 3]) = {mysum2([1, 2, 3])}, mysum2([1, 2, 3], 4) = {mysum2([1, 2, 3], 4)}")
