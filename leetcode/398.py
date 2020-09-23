# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-23 19:44:39
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-23 19:45:40

"""
398. Random Pick Index
Medium
Given an array of integers with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.

Note:
The array size can be very large. Solution that uses too much extra space will not pass the judge.

Example:

int[] nums = new int[] {1,2,3,3,3};
Solution solution = new Solution(nums);

// pick(3) should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
solution.pick(3);

// pick(1) should return 0. Since in the array only nums[0] is equal to 1.
solution.pick(1);
Accepted 97,562 Submissions 172,742
"""
import random


class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        num = 0
        pre = 0
        for idx, ii in enumerate(self.nums):
            if ii != target:
                continue
            num += 1
            if random.random() * num <= 1:
                pre = idx
        return pre


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
