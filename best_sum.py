from typing import List


def best_sum(target_sum: int, numbers: List[int], memo={}):
    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return []

    if target_sum < 0:
        return None

    shortest_combination = None

    for number in numbers:
        remainder = target_sum - number
        remainder_result = best_sum(remainder, numbers, memo)

        if remainder_result is not None:
            combination = [*remainder_result, number]
            if shortest_combination is None \
               or len(combination) < len(shortest_combination):
                shortest_combination = combination

    memo[target_sum] = shortest_combination
    return memo[target_sum]

# m = target sum
# n = numbers.length

# Brute Force:
# Time: O((n ^ m) * m)
# Space: O(m * m)

# Memoization:
# Time: O(n * m * m)
# Space: O(m * m)

print(best_sum(7, [5, 3, 4, 7], {}))
print(best_sum(8, [2, 3, 5], {}))
print(best_sum(8, [1, 4, 5], {}))
print(best_sum(100, [1, 2, 5, 25], {}))
