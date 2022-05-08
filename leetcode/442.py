# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2022-05-08 10:27:37
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-05-08 10:27:40

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        for ii in range(len(nums)):
            while nums[ii] != nums[nums[ii] - 1]:
                nums[nums[ii] - 1], nums[ii] = nums[ii], nums[nums[ii] - 1]
        return [num for ii, num in enumerate(nums) if num - 1 != ii]
