'''
5632. 检查边长度限制的路径是否存在 显示英文描述 
通过的用户数48
尝试过的用户数55
用户总通过次数48
用户总提交次数73
题目难度Hard
给你一个 n 个点组成的无向图边集 edgeList ，其中 edgeList[i] = [ui, vi, disi] 表示点 ui 和点 vi 之间有一条长度为 disi 的边。请注意，两个点之间可能有 超过一条边 。

给你一个查询数组queries ，其中 queries[j] = [pj, qj, limitj] ，你的任务是对于每个查询 queries[j] ，判断是否存在从 pj 到 qj 的路径，且这条路径上的每一条边都 严格小于 limitj 。

请你返回一个 布尔数组 answer ，其中 answer.length == queries.length ，当 queries[j] 的查询结果为 true 时， answer 第 j 个值为 true ，否则为 false 。

 

示例 1：


输入：n = 3, edgeList = [[0,1,2],[1,2,4],[2,0,8],[1,0,16]], queries = [[0,1,2],[0,2,5]]
输出：[false,true]
解释：上图为给定的输入数据。注意到 0 和 1 之间有两条重边，分别为 2 和 16 。
对于第一个查询，0 和 1 之间没有小于 2 的边，所以我们返回 false 。
对于第二个查询，有一条路径（0 -> 1 -> 2）两条边都小于 5 ，所以这个查询我们返回 true 。
示例 2：


输入：n = 5, edgeList = [[0,1,10],[1,2,5],[2,3,9],[3,4,13]], queries = [[0,4,14],[1,4,13]]
输出：[true,false]
解释：上图为给定数据。
 

提示：

2 <= n <= 105
1 <= edgeList.length, queries.length <= 105
edgeList[i].length == 3
queries[j].length == 3
0 <= ui, vi, pj, qj <= n - 1
ui != vi
pj != qj
1 <= disi, limitj <= 109
两个点之间可能有 多条 边。
'''

from collections import defaultdict

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        g = defaultdict(dict)
        for ii, jj, kk in edgeList:
            if jj in g[ii]:
                g[ii][jj] = min(g[ii][jj], kk)
            else:
                g[ii][jj] = kk
            if ii in g[jj]:
                g[jj][ii] = min(g[jj][ii], kk)
            else:
                g[jj][ii] = kk
        self.n, self.g = n, g
        # print(self.g)
        self.ok = defaultdict(dict)
        self.no_ok = {}
        return [self.query(ii, jj, kk) for ii, jj, kk in queries]
                
    def query(self, b, e, limit):
        if e in self.g[b] and self.g[b][e] < limit:
            return True
        if e in self.ok[b] and limit >= self.ok[b][e]:
            return True
        if (b, e) in self.no_ok and self.no_ok[(b, e)] >= limit:
            return False
        flag = [False] * self.n
        queue = [(b, 0)]
        while queue:
            now, now_t = queue.pop(0)
            flag[now] = True
            for ii, jj in self.g[now].items():
                if jj < limit and flag[ii] == False:
                    if ii == e:
                        return True
                    queue.append((ii, max(now_t, jj)))
                    if ii in self.ok[b]:
                        self.ok[b][ii] = min(max(now_t, jj), self.ok[b][ii])
                    else:
                        self.ok[b][ii] = max(now_t, jj)
                    self.ok[ii][b] = self.ok[b][ii]
            # print(queue, now)
        self.no_ok[(b, e)] = limit
        self.no_ok[(e, b)] = limit
        return False
            
     
from collections import defaultdict

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        def get_father(r, p):
            q =  r[p]
            while p != r[p]:
                p = r[p]
            while q != p:
                tmp = r[q]
                r[q] = p
                q = tmp
            return p
            
        ra = list(range(n))
        N, M = len(edgeList), len(queries)
        ans = [0] * M
        q = [[ii] + jj for ii, jj in enumerate(queries)]
        q.sort(key=lambda i: i[-1])
        edgeList.sort(key=lambda i:i[-1])
        
        idx = 0
        for ii in range(M):
            while idx < N and edgeList[idx][-1] < q[ii][-1]:
                a, b = edgeList[idx][:-1]
                fa = get_father(ra, a)
                fb = get_father(ra, b)
                if fa != fb:
                    ra[fa] = fb
                idx += 1
            a, b = q[ii][1:-1]
            fa = get_father(ra, a)
            fb = get_father(ra, b)
            ans[q[ii][0]] =  fa == fb
        return ans
