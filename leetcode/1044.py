# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-03-28 01:17:56
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-03-28 12:04:37

"""
1044. Longest Duplicate Substring Hard

Given a string S, consider all duplicated substrings: (contiguous) substrings of S that occur 2 or more times.  (The occurrences may overlap.)

Return any duplicated substring that has the longest possible length.  (If S does not have a duplicated substring, the answer is "".)

## Example 1:
Input: "banana"
Output: "ana"

## Example 2:
Input: "abcd"
Output: ""

## Note:
2 <= S.length <= 10^5
S consists of lowercase English letters.
Accepted 7,134 Submissions 28,026
"""
## Binary Search
class Solution:
    def longestDupSubstring(self, S: str) -> str:
        N = len(S)
        a, mod = 26, 2 ** 32
        nums = [ord(ii) - ord("a") for ii in S]

        def search(L: int):
            before = 0
            for ii in nums[:L]:
                before = (before * a + ii) % mod
            have_map = {before}
            al = pow(a, L, mod)
            for b in range(1, N - L + 1):
                now = (before * a - nums[b - 1] * al + nums[b + L - 1]) % mod
                if now in have_map:
                    return S[b : b + L]
                have_map.add(now)
                before = now
            return False

        left, right = 0, N
        while left != right:
            mid = left + (right - left) // 2
            if search(mid) != False:
                left = mid + 1
            else:
                right = mid
        result = search(left - 1)
        return "" if result == False or left == 0 else result


## N * N
class Solution:
    def longestDupSubstring(self, S: str) -> str:
        N = len(S)
        dp = [[0 for _ in range(N)] for _ in range(N)]
        result, left, right = 0, 0, 0
        for ii in range(N - 1, -1, -1):
            for jj in range(N - 1, -1, -1):
                if ii == jj:
                    continue
                if S[ii] == S[jj]:
                    if ii < N - 1 and jj < N - 1:
                        dp[ii][jj] = dp[ii + 1][jj + 1] + 1
                    else:
                        dp[ii][jj] = 1
                if dp[ii][jj] > result:
                    result = dp[ii][jj]
                    left, right = ii, ii + dp[ii][jj]
                    # print(ii, jj, result)
        # print(dp)
        return S[left:right]
