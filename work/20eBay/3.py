# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-10-17 20:04:21
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-10-17 20:08:47


class Solution:
    def findfriends(self, M):
        def dfs(now: int):
            flag[now] = 1
            for ii in range(N):
                if ii == now or flag[ii] or M[now][ii] == 0:
                    continue
                dfs(ii)

        N = len(M)
        flag = [0] * N
        res = 0
        for ii in range(N):
            if flag[ii] == 0:
                res += 1
                dfs(ii)
        return res

