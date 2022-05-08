"""
581. Shortest Unsorted Continuous Subarray
Medium

5086

205

Add to List

Share
Given an integer array nums, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order.

Return the shortest such subarray and output its length.

 

Example 1:

Input: nums = [2,6,4,8,10,9,15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Example 2:

Input: nums = [1,2,3,4]
Output: 0
Example 3:

Input: nums = [1]
Output: 0
 

Constraints:

1 <= nums.length <= 104
-105 <= nums[i] <= 105
 

Follow up: Can you solve it in O(n) time complexity?
Accepted
221,004
Submissions
643,133
"""


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        N = len(nums)
        x, y = float('-inf'), float("inf")
        l, r = -1, -1
        for ii in range(N):
            if nums[ii] < x:
                r = ii
            else:
                x = nums[ii]
            if nums[N - ii - 1] > y:
                l = N - ii - 1
            else:
                y = nums[N - ii - 1]
        return 0 if r == -1 else r - l + 1
