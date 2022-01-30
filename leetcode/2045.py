# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2022-01-24 21:24:22
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-01-24 21:24:31

class Solution:
    INF = 10 ** 9 + 7
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        g = defaultdict(list)
        for ii, jj in edges:
            g[ii - 1].append(jj - 1)
            g[jj - 1].append(ii - 1)
        queue, flag = [(0, 0)], [[self.INF] * 2 for _ in range(n)]
        flag[0][0] = 0
        while queue and flag[n - 1][1] == self.INF:
            d, head = heapq.heappop(queue)
            # print(d, head)
            for ii in g[head]:
                if d + 1 < flag[ii][0]:
                    flag[ii][0] = d + 1
                    heapq.heappush(queue, (d + 1, ii))
                elif flag[ii][1] > d + 1 > flag[ii][0]:
                    flag[ii][1] = d + 1
                    heapq.heappush(queue, (d + 1, ii))
        res = 0
        for ii in range(flag[n - 1][1]):
            if res % (2 * change) >= change:
                res += change * 2 - res % (2 * change)
            res += time
        return res
