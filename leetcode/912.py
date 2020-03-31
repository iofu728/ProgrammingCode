# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-03-31 21:00:03
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-03-31 21:22:56

"""
912. Sort an Array Medium
Given an array of integers nums, sort the array in ascending order.

## Example 1:
Input: nums = [5,2,3,1]
Output: [1,2,3,5]

## Example 2:
Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]

## Constraints:
1 <= nums.length <= 50000
-50000 <= nums[i] <= 50000

Accepted 57,473 Submissions 91,676
"""


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def paration(left: int, right: int) -> int:
            privot = random.randint(left, right)
            nums[right], nums[privot] = nums[privot], nums[right]
            jj = left - 1
            for ii in range(left, right):
                if nums[ii] < nums[right]:
                    jj += 1
                    nums[ii], nums[jj] = nums[jj], nums[ii]
            jj += 1
            nums[jj], nums[right] = nums[right], nums[jj]
            return jj

        def quicksort(left, right):
            if left >= right:
                return
            mid = paration(left, right)
            quicksort(left, mid - 1)
            quicksort(mid + 1, right)

        quicksort(0, len(nums) - 1)
        return nums
