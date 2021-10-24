# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2021-10-24 00:23:53
# @Last Modified by:   gunjianpan
# @Last Modified time: 2021-10-24 00:24:27

"""
638. Shopping Offers
Medium

875

579

Add to List

Share
In LeetCode Store, there are n items to sell. Each item has a price. However, there are some special offers, and a special offer consists of one or more different kinds of items with a sale price.

You are given an integer array price where price[i] is the price of the ith item, and an integer array needs where needs[i] is the number of pieces of the ith item you want to buy.

You are also given an array special where special[i] is of size n + 1 where special[i][j] is the number of pieces of the jth item in the ith offer and special[i][n] (i.e., the last integer in the array) is the price of the ith offer.

Return the lowest price you have to pay for exactly certain items as given, where you could make optimal use of the special offers. You are not allowed to buy more items than you want, even if that would lower the overall price. You could use any of the special offers as many times as you want.

 

Example 1:

Input: price = [2,5], special = [[3,0,5],[1,2,10]], needs = [3,2]
Output: 14
Explanation: There are two kinds of items, A and B. Their prices are $2 and $5 respectively. 
In special offer 1, you can pay $5 for 3A and 0B
In special offer 2, you can pay $10 for 1A and 2B. 
You need to buy 3A and 2B, so you may pay $10 for 1A and 2B (special offer #2), and $4 for 2A.
Example 2:

Input: price = [2,3,4], special = [[1,1,0,4],[2,2,1,9]], needs = [1,2,1]
Output: 11
Explanation: The price of A is $2, and $3 for B, $4 for C. 
You may pay $4 for 1A and 1B, and $9 for 2A ,2B and 1C. 
You need to buy 1A ,2B and 1C, so you may pay $4 for 1A and 1B (special offer #1), and $3 for 1B, $4 for 1C. 
You cannot add more items, though only $9 for 2A ,2B and 1C.
 

Constraints:

n == price.length
n == needs.length
1 <= n <= 6
0 <= price[i] <= 10
0 <= needs[i] <= 10
1 <= special.length <= 100
special[i].length == n + 1
0 <= special[i][j] <= 50
Accepted 41,911 Submissions 77,512
"""
from functools import lru_cache


class Solution:
    def shoppingOffers(
        self, price: List[int], special: List[List[int]], needs: List[int]
    ) -> int:
        @lru_cache(None)
        def dfs(wait):
            res = sum(ii * jj for ii, jj in zip(wait, price))
            for sp in x:
                p = sp[-1]
                x_wait = []
                for ii, jj in zip(sp[:-1], wait):
                    if ii > jj:
                        break
                    x_wait.append(jj - ii)
                if len(x_wait) == N:
                    res = min(res, dfs(tuple(x_wait)) + p)
            return res

        N = len(price)
        x = []
        for sp in special:
            if (
                sum(sp[:-1]) > 0
                and sum([ii * jj for ii, jj in zip(sp[:-1], price)]) > sp[-1]
                and not any(ii > jj for ii, jj in zip(sp[:-1], needs))
            ):
                x.append(sp)
        return dfs(tuple(needs))
