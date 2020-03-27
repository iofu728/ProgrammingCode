# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-03-27 12:45:47
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-03-27 13:02:49

"""
914. X of a Kind in a Deck of Cards Easy

In a deck of cards, each card has an integer written on it.

Return true if and only if you can choose X >= 2 such that it is possible to split the entire deck into 1 or more groups of cards, where:

Each group has exactly X cards.
All the cards in each group have the same integer.

## Example 1:
Input: deck = [1,2,3,4,4,3,2,1]
Output: true
Explanation: Possible partition [1,1],[2,2],[3,3],[4,4].

## Example 2:
Input: deck = [1,1,1,2,2,2,3,3]
Output: false´
Explanation: No possible partition.

## Example 3:
Input: deck = [1]
Output: false
Explanation: No possible partition.

## Example 4:
Input: deck = [1,1]
Output: true
Explanation: Possible partition [1,1].

## Example 5:
Input: deck = [1,1,2,2,2,2]
Output: true
Explanation: Possible partition [1,1],[2,2],[2,2].

## Constraints:
1 <= deck.length <= 10^4
0 <= deck[i] < 10^4
Accepted 31,782 Submissions 93,306
"""
from collections import Counter


class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        def gcd(a: int, b: int):
            if a < b:
                b, a = a, b
            while b:
                a, b = b, a % b
            return a

        counter_map = Counter(deck)
        min_counter = min(counter_map.values())
        if min_counter < 2:
            return False
        t = {k: gcd(v, min_counter) for k, v in counter_map.items()}
        min_gcd = min(t.values())
        if min_gcd < 2:
            return False

        for k, v in t.items():
            if v % min_gcd:
                return False
        return True
