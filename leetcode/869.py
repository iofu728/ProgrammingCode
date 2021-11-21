# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2021-10-28 00:07:33
# @Last Modified by:   gunjianpan
# @Last Modified time: 2021-10-28 00:07:39


class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        t = collections.Counter(str(n))
        idx = 1
        while idx < n * 10:
            tmp = collections.Counter(str(idx))
            if tmp == t:
                return True
            idx <<= 1
        return False