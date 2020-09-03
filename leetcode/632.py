# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-03 16:46:38
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-03 16:48:09

"""
632. Smallest Range Covering Elements from K Lists Hard
You have k lists of sorted integers in non-decreasing order. Find the smallest range that includes at least one number from each of the k lists.

We define the range [a, b] is smaller than range [c, d] if b - a < d - c or a < c if b - a == d - c.

 

Example 1:

Input: nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
Output: [20,24]
Explanation: 
List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
List 2: [0, 9, 12, 20], 20 is in range [20,24].
List 3: [5, 18, 22, 30], 22 is in range [20,24].
Example 2:

Input: nums = [[1,2,3],[1,2,3],[1,2,3]]
Output: [1,1]
Example 3:

Input: nums = [[10,10],[11,11]]
Output: [10,11]
Example 4:

Input: nums = [[10],[11]]
Output: [10,11]
Example 5:

Input: nums = [[1],[2],[3],[4],[5],[6],[7]]
Output: [1,7]
 

Constraints:

nums.length == k
1 <= k <= 3500
1 <= nums[i].length <= 50
-105 <= nums[i][j] <= 105
nums[i] is sorted in non-decreasing order.
Accepted 39,362 Submissions 74,712
"""
import heapq


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        res_max, res_min = 10 ** 9 + 7, -(10 ** 9) - 7
        max_v = max([ii[0] for ii in nums])
        N = len(nums)
        queue = [(nums[ii][0], ii, 0) for ii in range(N)]
        heapq.heapify(queue)
        while True:
            min_v, row, idx = heapq.heappop(queue)
            if max_v - min_v < res_max - res_min:
                res_max, res_min = max_v, min_v
            if idx == len(nums[row]) - 1:
                break
            heapq.heappush(queue, (nums[row][idx + 1], row, idx + 1))
            max_v = max(max_v, nums[row][idx + 1])
        return [res_min, res_max]

