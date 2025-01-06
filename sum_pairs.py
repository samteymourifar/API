from typing import List, Dict, Tuple
from collections import defaultdict
import json

def find_all_equal_sum_pairs(arr: List[int]) -> Dict[int, List[Tuple[int, int]]]:
    """
    Finds all unique pairs of elements in `arr` that share a common sum.
    Returns a dictionary where the keys are sums, and the values are lists of unique pairs.

    :param arr: A list of integers.
    :return: A dictionary with sums as keys and lists of pairs as values.
    """

    sum_map = defaultdict(set)  # sum -> set of (min, max) pairs

    # 1) Build the dictionary of sum -> pairs
    n = len(arr)
    for i in range(n - 1):
        for j in range(i + 1, n):
            s = arr[i] + arr[j]
            pair = (min(arr[i], arr[j]), max(arr[i], arr[j]))
            sum_map[s].add(pair)

    # 2) Convert to a JSON-compatible format, keeping only sums with >= 2 unique pairs
    result = {
        s: list(pairs) for s, pairs in sum_map.items() if len(pairs) >= 2
    }

    return result

def print_equal_sum_pairs(result: Dict[int, List[Tuple[int, int]]]) -> None:
    """
    Prints the results of sums and their associated pairs.

    :param result: A dictionary with sums as keys and lists of pairs as values.
    :return: None. Prints the output.
    """
    for s, pairs in result.items():
        print(f"Pairs: ", end="")
        for pr in pairs:
            print(f"({pr[0]}, {pr[1]})", end=" ")
        print(f"have sum: {s}")

# -----------------------------
# -----------------------------
# Test code: Only runs if this file is executed directly (not when imported).
if __name__ == "__main__":
    A1 = [6, 4, 12, 10, 22, 54, 32, 42, 21, 11]
    print("Example #1 result:")
    result1 = find_all_equal_sum_pairs(A1)
    print_equal_sum_pairs(result1)

    A2 = [6, 4, 4, 4, 4, 4, 12, 10, 22, 54, 32, 42, 21, 11]
    print("Example #2 result:")
    result2 = find_all_equal_sum_pairs(A2)
    print_equal_sum_pairs(result2)

    print("\nExample #3 result:")
    A3 = [4, 23, 65, 67, 24, 12, 86]
    result3 = find_all_equal_sum_pairs(A3)
    print_equal_sum_pairs(result3)
