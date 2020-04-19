# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-04-19 12:03:57
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-04-19 12:14:49

"""
1420. Build Array Where You Can Find The Maximum Exactly K Comparisons
User Accepted:568
User Tried:711
Total Accepted:603
Total Submissions:895
Difficulty:Hard
Given three integers n, m and k. Consider the following algorithm to find the maximum element of an array of positive integers:


You should build the array arr which has the following properties:

arr has exactly n integers.
1 <= arr[i] <= m where (0 <= i < n).
After applying the mentioned algorithm to arr, the value search_cost is equal to k.
Return the number of ways to build the array arr under the mentioned conditions. As the answer may grow large, the answer must be computed modulo 10^9 + 7.

Example 1:

Input: n = 2, m = 3, k = 1
Output: 6
Explanation: The possible arrays are [1, 1], [2, 1], [2, 2], [3, 1], [3, 2] [3, 3]
Example 2:

Input: n = 5, m = 2, k = 3
Output: 0
Explanation: There are no possible arrays that satisify the mentioned conditions.
Example 3:

Input: n = 9, m = 1, k = 1
Output: 1
Explanation: The only possible array is [1, 1, 1, 1, 1, 1, 1, 1, 1]
Example 4:

Input: n = 50, m = 100, k = 25
Output: 34549172
Explanation: Don't forget to compute the answer modulo 1000000007
Example 5:

Input: n = 37, m = 17, k = 7
Output: 418930126
 

Constraints:

1 <= n <= 50
1 <= m <= 100
0 <= k <= n
"""
import itertools


class Solution:
    MOD = 10 ** 9 + 7

    def numOfArrays(self, n: int, m: int, k: int) -> int:
        def cal_res(ks: list):
            tmp = 1
            no_zeros = [(ii, jj) for ii, jj in enumerate(ks) if jj]
            for nums in wait:
                for ii, jj in no_zeros:
                    # if ii == 0:
                    #     tmp *= ((nums[0] - 1) * jj)
                    # else:
                    tmp *= nums[ii - 1] ** jj
            # print(nums, ks, tmp)
            return tmp

        if k > m:
            return 0
        self.res = 0
        wait = list(itertools.combinations(range(1, m + 1), k))
        # print(wait)
        need = n - k

        def dfs(ks: list):
            # print(nums, ks)
            sum_ks = sum(ks)
            if len(ks) > k + 1 or (len(ks) == k + 1 and sum(ks) != need):
                return
            if sum_ks == need:
                self.res += cal_res(ks)
                self.res %= self.MOD
                return
            if len(ks) == k:
                dfs(ks + [need - sum_ks])
                return
            for ii in range(need - sum_ks + 1):
                dfs(ks + [ii])

        dfs([0])
        return self.res


class Solution:
    MOD = 10 ** 9 + 7

    def numOfArrays(self, n: int, m: int, k: int) -> int:

        dp = [[[0] * (k + 1) for _ in range(m + 1)] for _ in range(n)]

        for i in range(1, m + 1):
            dp[0][i][1] = 1

        for i in range(1, n):
            for j in range(1, m + 1):
                for pre in range(1, m + 1):
                    if pre >= j:
                        for kk in range(k + 1):
                            dp[i][pre][kk] += dp[i - 1][pre][kk]
                    else:
                        for kk in range(1, k + 1):
                            dp[i][j][kk] += dp[i - 1][pre][kk - 1]
        res = 0
        for i in range(m + 1):
            res += dp[-1][i][k]
        return res % self.MOD
