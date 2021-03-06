from typing import List


def can_construct(target: str, word_bank: List[str], memo={}) -> bool:
    if target in memo:
        return memo[target]

    if target == '':
        return True

    for word in word_bank:
        if target.startswith(word):
            suffix = target[len(word)::]

            if can_construct(suffix, word_bank, memo):
                memo[target] = True
                return True

    memo[target] = False
    return False

print(can_construct('abcdef', ['ab', 'abc', 'cd', 'def','abcd'], {}))
print(can_construct('skateboard', ['bo', 'rd', 'ate', 't','ska','sk','boar'], {}))
print(can_construct('enterapotentpot', ['a', 'p', 'ent', 'enter','ot','o','t'], {}))
print(can_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',
                    ['e', 'ee', 'eee', 'eeee','eeeee','eeeeeee'], {}))