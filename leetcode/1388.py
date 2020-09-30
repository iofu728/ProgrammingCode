# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-30 22:08:05
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-30 22:11:55

"""
1388. Pizza With 3n Slices Hard
There is a pizza with 3n slices of varying size, you and your friends will take slices of pizza as follows:

You will pick any pizza slice.
Your friend Alice will pick next slice in anti clockwise direction of your pick. 
Your friend Bob will pick next slice in clockwise direction of your pick.
Repeat until there are no more slices of pizzas.
Sizes of Pizza slices is represented by circular array slices in clockwise direction.

Return the maximum possible sum of slice sizes which you can have.

 

Example 1:



Input: slices = [1,2,3,4,5,6]
Output: 10
Explanation: Pick pizza slice of size 4, Alice and Bob will pick slices with size 3 and 5 respectively. Then Pick slices with size 6, finally Alice and Bob will pick slice of size 2 and 1 respectively. Total = 4 + 6.
Example 2:



Input: slices = [8,9,8,6,1,1]
Output: 16
Output: Pick pizza slice of size 8 in each turn. If you pick slice with size 9 your partners will pick slices of size 8.
Example 3:

Input: slices = [4,1,2,5,8,3,1,9,7]
Output: 21
Example 4:

Input: slices = [3,1,2]
Output: 3
 

Constraints:

1 <= slices.length <= 500
slices.length % 3 == 0
1 <= slices[i] <= 1000
Accepted 4,404 Submissions 9,793
"""


class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        def once(s: list):
            N = len(s)
            M = (N + 1) // 3
            dp = [[0] * (M + 1) for _ in range(N + 1)]
            for ii in range(1, N + 1):
                for jj in range(1, M + 1):
                    dp[ii][jj] = max(
                        dp[ii - 1][jj],
                        (dp[ii - 2][jj - 1] if ii - 2 >= 0 else 0) + s[ii - 1],
                    )
            return dp[N][M]

        return max(once(slices[1:]), once(slices[:-1]))
