# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2022-08-07 14:19:09
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-08-07 14:19:13

class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        g = defaultdict(list)
        for ii, jj in edges:
            g[ii].append(jj)
            g[jj].append(ii)
        q = deque([0])
        restricted = set(restricted)
        res = set()
        while q:
            h = q.popleft()
            if h in restricted:
                continue
            res.add(h)
            for ii in g[h]:
                if ii not in restricted and ii not in res:
                    q.append(ii)
        return len(res)
                    
        