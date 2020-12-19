# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-11-05 21:05:36
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-11-05 21:11:27

class Solution:
    def nextValue(self, chars, currentValue):
        N, M = len(chars), len(currentValue)
        char2id = {jj: ii for ii, jj in enumerate(chars)}
        pre = 1
        res = []
        for ii in range(M - 1, -1, -1):
            now = char2id[currentValue[ii]] + pre
            pre = now // N
            now = now % N
            res.append(chars[now])
        if pre:
            res.append(chars[pre])
        return ''.join(res[::-1])
        
