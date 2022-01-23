# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2022-01-23 12:03:56
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-01-23 12:03:57

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        a = [ii for ii in nums if ii > 0]
        b = [ii for ii in nums if ii < 0]
        return [a[ii // 2] if ii >> 1 << 1 == ii else b[ii // 2] for ii in range(len(nums))]