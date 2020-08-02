# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-08-02 18:44:13
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-08-02 18:45:03

"""
1437. Check If All 1's Are at Least Length K Places Away Medium
Given an array nums of 0s and 1s and an integer k, return True if all 1's are at least k places away from each other, otherwise return False.

Example 1:

Input: nums = [1,0,0,0,1,0,0,1], k = 2
Output: true
Explanation: Each of the 1s are at least 2 places away from each other.
Example 2:

Input: nums = [1,0,0,1,0,1], k = 2
Output: false
Explanation: The second 1 and third 1 are only one apart from each other.
Example 3:

Input: nums = [1,1,1,1,1], k = 0
Output: true
Example 4:

Input: nums = [0,1,0,1], k = 1
Output: true

Constraints:

1 <= nums.length <= 10^5
0 <= k <= nums.length
nums[i] is 0 or 1
Accepted 16,803 Submissions 26,495
"""
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        pre = -(10 ** 9) - 7
        for ii, jj in enumerate(nums):
            if jj == 1:
                # print(ii, jj, pre)
                if ii - pre <= k:
                    print(ii, pre)
                    return False
                pre = ii
        return True
