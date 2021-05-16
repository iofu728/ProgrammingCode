'''
5762. Number of Ways to Rearrange Sticks With K Sticks Visible My SubmissionsBack to Contest
User Accepted: 295
User Tried: 495
Total Accepted: 336
Total Submissions: 883
Difficulty: Hard
There are n uniquely-sized sticks whose lengths are integers from 1 to n. You want to arrange the sticks such that exactly k sticks are visible from the left. A stick is visible from the left if there are no longer sticks to the left of it.

For example, if the sticks are arranged [1,3,2,5,4], then the sticks with lengths 1, 3, and 5 are visible from the left.
Given n and k, return the number of such arrangements. Since the answer may be large, return it modulo 109 + 7.

 

Example 1:

Input: n = 3, k = 2
Output: 3
Explanation: [1,3,2], [2,3,1], and [2,1,3] are the only arrangements such that exactly 2 sticks are visible.
The visible sticks are underlined.
Example 2:

Input: n = 5, k = 5
Output: 1
Explanation: [1,2,3,4,5] is the only arrangement such that all 5 sticks are visible.
The visible sticks are underlined.
Example 3:

Input: n = 20, k = 11
Output: 647427950
Explanation: There are 647427950 (mod 109 + 7) ways to rearrange the sticks such that exactly 11 sticks are visible.
 

Constraints:

1 <= n <= 1000
1 <= k <= n
'''

from functools import lru_cache
class Solution:
    MOD = 10 ** 9 + 7
    def rearrangeSticks(self, n: int, k: int) -> int:
        N = 1005
        kk, mm = [[0] * (N + 1) for _ in range(N + 1)], [[0] * (N + 1) for _ in range(N + 1)]

        def dp(a, b):
            # print(a, b)
            if a == 0:
                return int(b == 0)
            if a == 1:
                return 1 if b == 1 else 0
            if a < 0 or b <= 0 or a < b:
                return 0
            if b in [a]:
                return 1
            if kk[a][b]:
                return mm[a][b]
            res = dp(a - 1, b - 1) + (a - 1) * dp(a - 1, b)
            kk[a][b] = 1
            mm[a][b] = res
            return res
            
            
            # for ii in range(1, a + 1):
            #     res += dp(a - ii, b - 1) * rec(a - 1, ii - 1)
            #     # aa.append((dp(a - ii, b - 1),  rec(a - 1, ii - 1)))
            #     if b - 1 > a - ii or a - ii < 0:
            #         break
            # print(a, b, aa, res)
            return res
                
            
        return dp(n, k) % self.MOD
  