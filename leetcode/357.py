# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2022-04-11 15:20:37
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-04-11 15:20:39

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        res = 1
        while n:
            tmp = 9
            for ii in range(9, 9 - n + 1, -1):
                tmp *= ii
            res += tmp
            n -= 1
        return res