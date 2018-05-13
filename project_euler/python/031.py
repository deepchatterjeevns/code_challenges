# coding=utf-8

"""http://projecteuler.net/problem=031

Coin sums

In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:
1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:
1x£1 + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p
How many different ways can £2 be made using any number of coins?

Solution by jontsai <hello@jontsai.com>
"""
from utils import *

EXPECTED_ANSWER = 73682

COINS = [
    200,
    100,
    50,
    20,
    10,
    5,
    2,
    1,
]

# basic algorithm
# start with the largest coin
# gradually use one-less of the current coin

COIN_SUMS_MEMO = {}
def coin_sums(amount, coin_index):
    key = '%s:%s' % (amount, coin_index,)

    if key in COIN_SUMS_MEMO:
        num_ways = COIN_SUMS_MEMO[key]
    elif amount == 0:
        num_ways = 1
    else:
        coin = COINS[coin_index]
        num_ways = 0
        if coin <= amount:
            num_ways += coin_sums(amount - coin, coin_index)
        if coin_index + 1 < len(COINS):
            num_ways += coin_sums(amount, coin_index + 1)

        COIN_SUMS_MEMO[key] = num_ways
    return num_ways

answer = coin_sums(200, 0)

print 'Expected: %s, Answer: %s' % (EXPECTED_ANSWER, answer)
