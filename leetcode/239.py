# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-08-26 01:36:40
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-08-26 01:37:54

"""
239. Sliding Window Maximum Hard

Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

Follow up:
Could you solve it in linear time?

Example:

Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7] 
Explanation: 

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
 

Constraints:

1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
1 <= k <= nums.length
Accepted 286,837 Submissions 663,859
"""
import heapq


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        N = len(nums)
        res, have = [], []
        for ii, jj in enumerate(nums[:k]):
            heapq.heappush(have, (-jj, ii))
        for ii in range(N - k + 1):
            x, y = heapq.heappop(have)
            while y < ii:
                x, y = heapq.heappop(have)
            res.append(-1 * x)
            heapq.heappush(have, (x, y))
            next_id = ii + k
            if next_id < N:
                heapq.heappush(have, (-nums[next_id], next_id))
        return res
