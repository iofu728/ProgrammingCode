# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-07-30 22:32:20
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-07-30 22:32:59

"""
552. Student Attendance Record II Hard
Given a positive integer n, return the number of all possible attendance records with length n, which will be regarded as rewardable. The answer may be very large, return it after mod 109 + 7.

A student attendance record is a string that only contains the following three characters:

'A' : Absent.
'L' : Late.
'P' : Present.
A record is regarded as rewardable if it doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

Example 1:
Input: n = 2
Output: 8 
Explanation:
There are 8 records with length 2 will be regarded as rewardable:
"PP" , "AP", "PA", "LP", "PL", "AL", "LA", "LL"
Only "AA" won't be regarded as rewardable owing to more than one absent times. 
Note: The value of n won't exceed 100,000.

Accepted 23,562 Submissions 64,409
"""
class Solution:
    MOD = 10 ** 9 + 7

    def checkRecord(self, n: int) -> int:
        dp = [0] * max(n + 1, 3)
        dp[0] = 1
        dp[1] = 2
        dp[2] = 4
        for ii in range(3, n + 1):
            dp[ii] = (dp[ii - 1] + dp[ii - 2] + dp[ii - 3]) % self.MOD

        res = 0
        for ii in range(1, n // 2 + 1):
            res += (dp[ii - 1] * dp[n - ii]) % self.MOD
        res *= 2
        if n % 2 == 1:
            res += dp[n // 2] ** 2
        return (res + dp[n]) % self.MOD
