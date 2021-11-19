from typing import List


def how_sum(target_sum: int, numbers: List[int], memo={}):
    if target_sum in memo:
        return memo[target_sum]

    if target_sum == 0:
        return []
    if target_sum < 0:
        return None

    for number in numbers:
        remainder = target_sum - number
        remainder_result = how_sum(target_sum - number, numbers, memo)

        if (remainder_result is not None):
            memo[target_sum] = [*remainder_result, number]
            return memo[target_sum]

    memo[target_sum] = None
    return memo[target_sum]

# m = target sum
# n = numbers.length

# Brute Force:
# Time: O((n ^ m) * m)
# Space: O(m)

# Memoization:
# Time: O(n * m * m)
# Space: O(m * m)


print(how_sum(7, [2, 3], {}))
print(how_sum(7, [5, 3, 4, 7], {}))
print(how_sum(7, [2, 4], {}))
print(how_sum(8, [2, 3, 5], {}))
print(how_sum(300, [7, 14], {}))
