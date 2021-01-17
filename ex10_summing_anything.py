from typing import List, Dict
from functools import reduce


def mysum(*args):
    if not args:
        return None
    else:
        return reduce(lambda a, b: a+b, args)


def combine_dicts(dicts: List[Dict]) -> Dict:
    res = {}
    for dict in dicts:
        for key, value in dict.items():
            if key not in res:
                res[key] = [value]
            else:
                res[key].append(value)
    return res


print(f"mysum('abc', 'def')={mysum('abc', 'def')}, mysum([1,2,3], [4,5,6])={mysum([1,2,3], [4,5,6])}, mysum(1,2,3)={mysum(1,2,3)}")
print(f"combine_dicts([{{'1': 'one', '3': 'three', '7': 'seven'}}, {{'3': 'trois', '13': 'treize', '15': 'quinze'}}, {{'1': 'uno', '3': 'tres'}}])={combine_dicts([{'1': 'one', '3': 'three', '7': 'seven'}, {'3': 'trois', '13': 'treize', '15': 'quinze'}, {'1': 'uno', '3': 'tres'}])}")


