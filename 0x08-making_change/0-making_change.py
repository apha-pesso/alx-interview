#!/usr/bin/python3
"""
coins = [1, 2, 25]
total = 37
"""


def makeChange(coins, total):
    """
    make change
    """
    counter = 0
    if total <= 0:
        return 0
    if min(coins) > total:
        return -1
    if sum(coins) == total:
        return len(coins)
    if total in coins:
        return 1
    sort = sorted(coins, reverse=True)

    '''
    [50, 20, 15] -> 50 + - => -1
             -> 20 + 20 + 20 => 3
             -> 15 * 4 => 4
             box = [-1, 3, 4].filter(mins: for mins > -1)
    box = []

    box = []
    for i in range(len(sort)):
        target = total
        counter = 0
        for j in range(i, len(sort)):
            while sort[j] <= target:
                target -= sort[j]
                # print(sort[j])
                # print(target)
                counter += 1
        if target == 0:
            box.append(counter)
        else:
            box.append(-1)

    '''
    for i in range(len(sort)):
        while sort[i] <= total:
            total = total - sort[i]
            counter += 1

    if total == 0:
        return counter
        # box.append(counter)
        # else:
    return -1
    # box.append(-1)
    '''

    # res = min(box)
    res = sorted(list(set(box)))
    print(res)
    if len(res) == 1:
        return res[0]
    else:
        if res[0] == -1:
            return res[1]
        return res[0]
    # if res > 0:
        # return res
    # return -1
    '''
