# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-07-04 22:48:32
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-07-04 22:49:40

"""
31. Next Permutation Medium
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

Accepted 368,498 Submissions 1,138,076
"""


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        if N <= 1:
            return nums
        a, b = N - 2, N - 1
        while a >= 0 and nums[a + 1] <= nums[a]:
            a -= 1
        if a >= 0:
            while b >= 0 and nums[b] <= nums[a]:
                b -= 1
            nums[a], nums[b] = nums[b], nums[a]
        l, r = a + 1, N - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1
        return nums
