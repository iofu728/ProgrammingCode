"""
473. Matchsticks to Square
Medium

1611

125

Add to List

Share
You are given an integer array matchsticks where matchsticks[i] is the length of the ith matchstick. You want to use all the matchsticks to make one square. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.

Return true if you can make this square and false otherwise.

 

Example 1:


Input: matchsticks = [1,1,2,2,2]
Output: true
Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.
Example 2:

Input: matchsticks = [3,3,3,3,4]
Output: false
Explanation: You cannot find a way to form a square with all the matchsticks.
 

Constraints:

1 <= matchsticks.length <= 15
1 <= matchsticks[i] <= 108
Accepted
77,718
Submissions
192,843
"""
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        t = sum(matchsticks)
        if t % 4:
            return False
        q = t // 4
        dp = [-1] * (1 << len(matchsticks))
        dp[0] = 0
        for s in range(1, len(dp)):
            for k, v in enumerate(matchsticks):
                if s & (1 << k) == 0:
                    continue
                s1 = s & ~(1 << k)
                if dp[s1] >= 0 and dp[s1] + v <= q:
                    dp[s] = (dp[s1] + v) % q
                    break
        return dp[-1] == 0
