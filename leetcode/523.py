# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2021-06-02 15:00:47
# @Last Modified by:   gunjianpan
# @Last Modified time: 2021-06-02 15:00:53
import bisect
from collections import defaultdict


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        N, last, sums, sums_map = len(nums), 0, [0], defaultdict(list)
        for jj, ii in enumerate(nums):
            last = (last + ii) % k
            sums_map[last].append(jj + 1)
            sums.append(last)
        for ii in range(N + 1):
            ks = sums_map[sums[ii]]
            idx = bisect.bisect_right(ks, ii + 1)
            if idx < len(ks):
                return True
        # print(sums, sums_map)
        return False
