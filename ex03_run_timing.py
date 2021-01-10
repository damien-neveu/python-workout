from typing import List
from functools import reduce


def is_number(s: str) -> bool:
    return s.strip().replace('.', '', 1).isdigit()


def calculate_average(floats: List[float]) -> float:
    return reduce(lambda a, b: a + b, floats) / len(floats)


if __name__ == "__main__":
    runs_timings = []
    while True:
        answer = input("Enter 10 km run time:")
        if is_number(answer):
            runs_timings.append(float(answer))
        else:
            break
    print(f"Average of {calculate_average(runs_timings):0.2f}, over {len(runs_timings)} runs")

