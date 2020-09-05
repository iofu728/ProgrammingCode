# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-05 22:20:38
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-05 22:21:15

"""
540. Single Element in a Sorted Array Medium
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.

Follow up: Your solution should run in O(log n) time and O(1) space.

 

Example 1:

Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:

Input: nums = [3,3,7,7,10,11,11]
Output: 10
 

Constraints:

1 <= nums.length <= 10^5
0 <= nums[i] <= 10^5
Accepted 157,803 Submissions 272,446
"""
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1:
            return nums[0]
        if nums[0] != nums[1]:
            return nums[0]
        if nums[-1] != nums[-2]:
            return nums[-1]
        left, right = 0, N - 1
        while left <= right:
            mid = (left + right) >> 1
            print(left, right, mid, nums[left], nums[right], nums[mid])
            if not mid:
                left += 1
            if mid == N - 1:
                right -= 1
            if mid >> 1 << 1 == mid:
                if nums[mid] not in [nums[mid - 1], nums[mid + 1]]:
                    left = mid
                    break
                if nums[mid] == nums[mid - 1]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] == nums[mid + 1]:
                    right = mid - 1
                else:
                    left = mid + 1
        print(left, right)
        return nums[left]
