# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-08-28 10:31:55
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-08-28 10:32:41

"""
1493. Longest Subarray of 1's After Deleting One Element Medium
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array.

Return 0 if there is no such subarray.

Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
Example 2:

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
Example 3:

Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.
Example 4:

Input: nums = [1,1,0,0,1,1,1,0,1]
Output: 4
Example 5:

Input: nums = [0,0,0]
Output: 0

Constraints:

1 <= nums.length <= 10^5
nums[i] is either 0 or 1.
Accepted 12,494 Submissions 21,028
"""
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        N = len(nums)
        b = ([0] if nums[0] == 1 else []) + [
            ii for ii in range(1, N) if nums[ii] == 1 and nums[ii - 1] == 0
        ]
        e = [ii for ii in range(N - 1) if nums[ii] == 1 and nums[ii + 1] == 0] + (
            [N - 1] if nums[N - 1] == 1 else []
        )
        print(b, e)
        pairs = [(ii, jj) for ii, jj in zip(b, e)]
        M = len(pairs)
        if not M:
            return 0
        len_list = (
            [
                pairs[0][1]
                - pairs[0][0]
                + (1 if pairs[0][0] != 0 or pairs[0][1] != N - 1 else 0)
            ]
        ) + [
            pairs[ii][1] - pairs[ii - 1][0]
            if pairs[ii][0] - pairs[ii - 1][1] == 2
            else pairs[ii][1] - pairs[ii][0] + 1
            for ii in range(1, M)
        ]
        print(len_list)
        return max(len_list)
