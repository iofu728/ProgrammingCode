# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-03-24 19:14:19
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-03-24 20:27:59

"""
215. Kth Largest Element in an Array Medium

Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

## Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5

## Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.

Accepted 545,232 Submissions 1,032,378
"""
import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        N = len(nums)
        def partion(left: int, right: int, privot: int) -> int:
            p = nums[privot]
            nums[privot], nums[right] = nums[right], nums[privot]
            result = left

            for ii in range(left, right):
                if nums[ii] < p:
                    nums[result], nums[ii] = nums[ii], nums[result]
                    result += 1
            nums[right], nums[result] = nums[result], nums[right]
            return result

        left, right, privot = 0, N - 1, 0
        while left <= right and left < N and right >= 0:
            # print(nums, left, right, privot)
            if left == right:
                return nums[left]
            privot = random.randint(left, right)
            # print(privot)
            privot = partion(left, right, privot)
            if privot == N - k:
                return nums[privot]
            if privot < N - k:
                left = privot + 1
            else:
                right = privot - 1
    

    
