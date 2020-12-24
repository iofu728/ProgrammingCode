# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-12-24 21:37:46
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-12-24 21:45:12

"""
135. Candy Hard
There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?

Example 1:

Input: [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
Example 2:

Input: [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
             The third child gets 1 candy because it satisfies the above two conditions.
Accepted 144,373 Submissions 443,168
"""


class Solution:
    def candy(self, ratings: List[int]) -> int:
        N = len(ratings)
        left = [1] * N
        for ii in range(1, N):
            if ratings[ii] > ratings[ii - 1]:
                left[ii] = left[ii - 1] + 1
        res, right = left[-1], left[-1]
        for ii in range(N - 2, -1, -1):
            if ratings[ii] > ratings[ii + 1]:
                right += 1
            else:
                right = 1
            res += max(right, left[ii])
        return res