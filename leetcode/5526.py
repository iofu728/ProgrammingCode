# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-27 13:11:25
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-27 13:12:04

from itertools import combinations

class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        res = 0
        for i in range(len(requests), 0, -1):
            combins = combinations(requests, i)
            # print(combins)
            for combin in combins:
                c_in = [ele[0] for ele in combin]
                c_out = [ele[1] for ele in combin]
                c_in.sort()
                c_out.sort()
                # print(c_in, c_out)
                if c_in == c_out:
                    res = i
                    return res
        return res
        
        

# from collections import defaultdict
# class Solution:
#     def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
#         def dfs(b, now, pre, done):
#             if now != b and b in g[now]:
#                 tmp.append(pre + [[b, g[now][b]]])
#             self.t += 1
#             for k, v in g[now].items():
#                 if k not in done and v:
#                     done.add(k)
#                     dfs(b, k, pre + [[k, v]], done)
#                     done.remove(k)
#         def is_ok(b, pre, num):
#             if not num:
#                 return False
#             p = b
#             for kk in pre:
#                 if g[p][kk] < num:
#                     # print(p, kk, g[p][kk])
#                     return False
#                 p = kk
#             return True
#         g = {ii: defaultdict(int) for ii in range(n)}
#         res = 0
#         for ii, jj in requests:
#             if ii == jj:
#                 res += 1
#                 continue
#             g[ii][jj] += 1
#         self.t = 0
#         for ii in range(n):
#             tmp = []
#             dfs(ii, ii, [], set([ii]))
#             tmps = []
#             for jj in tmp:
#                 min_t = min([mm for _, mm in jj])
#                 tmps.append([[mm for mm, _ in jj], min_t])
#             # print(tmps)
#             for i, j in sorted(tmps, key=lambda i:-i[1] * len(i[0])):
#                 if is_ok(ii, i, j):
#                     res += len(i) * j
#                     # print(res, ii, i, j)
#                     pre = ii
#                     for kk in i:
#                         g[pre][kk] -= j
#                         pre = kk
#         return res
            