"""
6103. 从树中删除边的最小分数 显示英文描述 
通过的用户数10
尝试过的用户数17
用户总通过次数10
用户总提交次数20
题目难度Hard
存在一棵无向连通树，树中有编号从 0 到 n - 1 的 n 个节点， 以及 n - 1 条边。

给你一个下标从 0 开始的整数数组 nums ，长度为 n ，其中 nums[i] 表示第 i 个节点的值。另给你一个二维整数数组 edges ，长度为 n - 1 ，其中 edges[i] = [ai, bi] 表示树中存在一条位于节点 ai 和 bi 之间的边。

删除树中两条 不同 的边以形成三个连通组件。对于一种删除边方案，定义如下步骤以计算其分数：

分别获取三个组件 每个 组件中所有节点值的异或值。
最大 异或值和 最小 异或值的 差值 就是这一种删除边方案的分数。
例如，三个组件的节点值分别是：[4,5,7]、[1,9] 和 [3,3,3] 。三个异或值分别是 4 ^ 5 ^ 7 = 6、1 ^ 9 = 8 和 3 ^ 3 ^ 3 = 3 。最大异或值是 8 ，最小异或值是 3 ，分数是 8 - 3 = 5 。
返回在给定树上执行任意删除边方案可能的 最小 分数。

 

示例 1：


输入：nums = [1,5,5,4,11], edges = [[0,1],[1,2],[1,3],[3,4]]
输出：9
解释：上图展示了一种删除边方案。
- 第 1 个组件的节点是 [1,3,4] ，值是 [5,4,11] 。异或值是 5 ^ 4 ^ 11 = 10 。
- 第 2 个组件的节点是 [0] ，值是 [1] 。异或值是 1 = 1 。
- 第 3 个组件的节点是 [2] ，值是 [5] 。异或值是 5 = 5 。
分数是最大异或值和最小异或值的差值，10 - 1 = 9 。
可以证明不存在分数比 9 小的删除边方案。
示例 2：


输入：nums = [5,5,2,4,4,2], edges = [[0,1],[1,2],[5,2],[4,3],[1,3]]
输出：0
解释：上图展示了一种删除边方案。
- 第 1 个组件的节点是 [3,4] ，值是 [4,4] 。异或值是 4 ^ 4 = 0 。
- 第 2 个组件的节点是 [1,0] ，值是 [5,5] 。异或值是 5 ^ 5 = 0 。
- 第 3 个组件的节点是 [2,5] ，值是 [2,2] 。异或值是 2 ^ 2 = 0 。
分数是最大异或值和最小异或值的差值，0 - 0 = 0 。
无法获得比 0 更小的分数 0 。
 

提示：

n == nums.length
3 <= n <= 1000
1 <= nums[i] <= 108
edges.length == n - 1
edges[i].length == 2
0 <= ai, bi < n
ai != bi
edges 表示一棵有效的树
"""
class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        @lru_cache(None)
        def dfs(h):
            res = nums[h]
            for ii in k[h]:
                res ^= dfs(ii)
            return res
        @lru_cache(None)
        def kk(h):
            res = set()
            for ii in k[h]:
                res = res.union(kk(ii))
                res.add(ii)
            return res
        N = len(nums)
        g = defaultdict(list)
        k = defaultdict(set)
        for ii, jj in edges:
            g[ii].append(jj)
            g[jj].append(ii)
        root = [ii for ii, jj in g.items() if len(jj) == max([len(i) for i in g.values()])][0]
        q = deque([root])
        done = set([root])
        while q:
            h = q.popleft()
            for ii in g[h]:
                if ii not in done:
                    done.add(ii)
                    k[h].add(ii)
                    q.append(ii)
        res = float("inf")
        # print(k)
        # print([dfs(ii) for ii in range(N)])
        # print([kk(ii) for ii in range(N)])
            
        for ii in range(N - 1):
            a, b = edges[ii]
            if a in k[b]:
                a, b = b, a
            s2 = dfs(b)
            s1 = dfs(root) ^ s2
            # print(ii, a, b, s1, s2)
            for jj in range(ii + 1, N - 1):
                c, d = edges[jj]
                if c in k[d]:
                    c, d = d, c
                # print(jj, c, d, d in kk(b), b in kk(d))
                ss1, ss2 = s1, s2
                if d in kk(b):
                    ss3 = dfs(d)
                    ss2 = ss2 ^ ss3
                elif b in kk(d):
                    ss3 = dfs(d)
                    ss3 = ss3 ^ ss2
                    ss1 = ss1 ^ ss3
                else:
                    ss3 = dfs(d)
                    ss1 = ss1 ^ ss3
                # print(ii, jj, a, b, c, d, ss1, ss2, ss3)
                s = sorted([ss1, ss2, ss3])
                res = min(res, s[-1] - s[0])
        return res
 