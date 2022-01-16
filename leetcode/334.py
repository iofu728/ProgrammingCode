# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2022-01-12 18:46:16
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-01-12 18:46:31

"""
334. Increasing Triplet Subsequence
Medium

3398

194

Add to List

Share
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

 

Example 1:

Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.
Example 2:

Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.
Example 3:

Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
 

Constraints:

1 <= nums.length <= 5 * 105
-231 <= nums[i] <= 231 - 1
 

Follow up: Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?
Accepted
247,424
Submissions
599,637
"""
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        N = len(nums)
        tmp = [nums[0]]
        for ii in range(1, N):
            ii = nums[ii]
            if ii > tmp[-1]:
                tmp.append(ii)
                if len(tmp) >= 3:
                    return True
            else:
                x = bisect.bisect_left(tmp, ii)
                tmp[x] = ii
        return False