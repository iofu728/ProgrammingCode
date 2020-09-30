# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-30 20:18:09
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-30 20:19:20

"""
228. Summary Ranges Medium
You are given a sorted unique integer array nums.

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
 

Example 1:

Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
Example 2:

Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"
Example 3:

Input: nums = []
Output: []
Example 4:

Input: nums = [-1]
Output: ["-1"]
Example 5:

Input: nums = [0]
Output: ["0"]
 

Constraints:

0 <= nums.length <= 20
-231 <= nums[i] <= 231 - 1
All the values of nums are unique.
Accepted 173,651 Submissions 435,827
"""


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        N = len(nums)
        if not N:
            return []
        b = [0] + [ii for ii in range(1, N) if nums[ii] != nums[ii - 1] + 1]
        e = [ii for ii in range(N - 1) if nums[ii + 1] != nums[ii] + 1] + [N - 1]
        res = []
        for ii, jj in zip(b, e):
            tmp = (
                str(nums[ii])
                if nums[ii] == nums[jj]
                else "{}->{}".format(nums[ii], nums[jj])
            )
            res.append(tmp)
        return res
