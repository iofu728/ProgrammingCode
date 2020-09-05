# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-04 21:28:26
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-04 21:29:39

"""
1330. Reverse Subarray To Maximize Array Value Hard
You are given an integer array nums. The value of this array is defined as the sum of |nums[i]-nums[i+1]| for all 0 <= i < nums.length-1.

You are allowed to select any subarray of the given array and reverse it. You can perform this operation only once.

Find maximum possible value of the final array.

Example 1:

Input: nums = [2,3,1,5,4]
Output: 10
Explanation: By reversing the subarray [3,1,5] the array becomes [2,5,1,3,4] whose value is 10.
Example 2:

Input: nums = [2,4,9,24,2,1,10]
Output: 68
 

Constraints:

1 <= nums.length <= 3*10^4
-10^5 <= nums[i] <= 10^5
Accepted 2,254 Submissions 6,398
"""


class Solution:
    def maxValueAfterReverse(self, nums: List[int]) -> int:
        N = len(nums)
        pairs = [(min(ii, jj), max(ii, jj)) for ii, jj in zip(nums[:-1], nums[1:])]
        sum_list = [jj - ii for ii, jj in pairs]
        a = max([ii for ii, _ in pairs])
        b = min([jj for _, jj in pairs])
        res = 0
        for ii in range(1, N):
            res = max(res, abs(nums[ii] - nums[0]) - abs(nums[ii - 1] - nums[ii]))
            res = max(res, abs(nums[ii - 1] - nums[-1]) - abs(nums[ii] - nums[ii - 1]))
        return sum(sum_list) + max(2 * (a - b), res)
