# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2022-04-17 15:31:31
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-04-17 15:31:33

class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        def cacl(n):
            res = 0
            for ii in dist:
                if res != int(res):
                    res = math.ceil(res)
                res += ii / n
            return res <= hour
        N = len(dist)
        if N - 1 >= hour:
            return -1
        l, r = 1, max(dist) * 100
        while l < r:
            m = (l + r) // 2
            if cacl(m):
                r = m
            else:
                l = m + 1
        return l