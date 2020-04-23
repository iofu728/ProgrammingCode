# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-04-21 16:37:17
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-04-21 18:48:34

"""
1248. Count Number of Nice Subarrays Medium
Given an array of integers nums and an integer k. A subarray is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays.

Example 1:

Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].
Example 2:

Input: nums = [2,4,6], k = 1
Output: 0
Explanation: There is no odd numbers in the array.
Example 3:

Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16

Constraints:

1 <= nums.length <= 50000
1 <= nums[i] <= 10^5
1 <= k <= nums.length
Accepted 11,351 Submissions 20,679
"""


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        N = len(nums)
        odds = [ii for ii, jj in enumerate(nums) if jj >> 1 << 1 != jj]
        res, M = 0, len(odds)
        # print(odds)
        for ii in range(M - k + 1):
            a = odds[ii] - (odds[ii - 1] if ii else -1)
            b = (odds[ii + k] if ii + k < M else N) - odds[ii + k - 1]
            # print(a, b, ii, k, ii + k, N, M)
            res += a * b
        return res
