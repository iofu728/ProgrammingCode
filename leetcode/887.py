# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-03-25 14:18:03
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-03-25 21:41:36

"""
887. Super Egg Drop Hard
You are given K eggs, and you have access to a building with N floors from 1 to N. 

Each egg is identical in function, and if an egg breaks, you cannot drop it again.

You know that there exists a floor F with 0 <= F <= N such that any egg dropped at a floor higher than F will break, and any egg dropped at or below floor F will not break.

Each move, you may take an egg (if you have an unbroken one) and drop it from any floor X (with 1 <= X <= N). 

Your goal is to know with certainty what the value of F is.

What is the minimum number of moves that you need to know with certainty what F is, regardless of the initial value of F?

## Example 1:
Input: K = 1, N = 2
Output: 2

### Explanation: 
Drop the egg from floor 1.  If it breaks, we know with certainty that F = 0.
Otherwise, drop the egg from floor 2.  If it breaks, we know with certainty that F = 1.
If it didn't break, then we know with certainty F = 2.
Hence, we needed 2 moves in the worst case to know what F is with certainty.

## Example 2:
Input: K = 2, N = 6
Output: 3

## Example 3:
Input: K = 3, N = 14
Output: 4

## Note:
1 <= K <= 100
1 <= N <= 10000

Accepted 13,809 Submissions 52,264
"""


class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        dp = [0 for ii in range(K + 2)]
        ans = 0
        while dp[K] < N:
            for i in range(K, 0, -1):
                ## dp[i]: last time no breaking
                ## dp[i - 1]: last time breaking
                dp[i] = dp[i] + dp[i - 1] + 1
            ans += 1
        return ans


class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]
        for i in range(0, N + 1):
            dp[i][1] = i
        for j in range(2, K + 1):
            for i in range(1, N + 1):
                # dp[i][j] = i
                left, right = 1, i - 1
                while left + 1 < right and left < i and right > 0:
                    # print(left, right)
                    middle = (left + right) // 2
                    t1 = dp[middle - 1][j - 1]
                    t2 = dp[i - middle][j]
                    if t1 == t2:
                        left = right = middle
                        break
                    elif t1 > t2:
                        right = middle
                    else:
                        left = middle

                dp[i][j] = min(
                    max(dp[left - 1][j - 1], dp[i - left][j]) + 1,
                    max(dp[right - 1][j - 1], dp[i - right][j]) + 1,
                )
                print(i, j, left, right, dp[i][j], dp)
                # for k in range(1, i):

        return dp[N][K]
