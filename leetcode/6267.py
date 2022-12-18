'''
6267. 添加边使所有节点度数都为偶数 显示英文描述 
通过的用户数12
尝试过的用户数31
用户总通过次数12
用户总提交次数41
题目难度Hard
给你一个有 n 个节点的 无向 图，节点编号为 1 到 n 。再给你整数 n 和一个二维整数数组 edges ，其中 edges[i] = [ai, bi] 表示节点 ai 和 bi 之间有一条边。图不一定连通。

你可以给图中添加 至多 两条额外的边（也可以一条边都不添加），使得图中没有重边也没有自环。

如果添加额外的边后，可以使得图中所有点的度数都是偶数，返回 true ，否则返回 false 。

点的度数是连接一个点的边的数目。

 

示例 1：



输入：n = 5, edges = [[1,2],[2,3],[3,4],[4,2],[1,4],[2,5]]
输出：true
解释：上图展示了添加一条边的合法方案。
最终图中每个节点都连接偶数条边。
示例 2：



输入：n = 4, edges = [[1,2],[3,4]]
输出：true
解释：上图展示了添加两条边的合法方案。
示例 3：



输入：n = 4, edges = [[1,2],[1,3],[1,4]]
输出：false
解释：无法添加至多 2 条边得到一个符合要求的图。
 

提示：

3 <= n <= 105
2 <= edges.length <= 105
edges[i].length == 2
1 <= ai, bi <= n
ai != bi
图中不会有重边
'''
class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        c = defaultdict(int)
        g = defaultdict(set)
        for ii, jj in edges:
            c[ii] += 1
            c[jj] += 1
            g[ii].add(jj)
            g[jj].add(ii)
        nodes = [ii for ii, jj in c.items() if jj % 2 == 1]
        # print(nodes)
        if len(nodes) not in [0, 2, 4]:
            return False
        if len(nodes) == 2 and nodes[1] in g[nodes[0]] and not any(ii not in g[nodes[0]] and ii not in g[nodes[1]] for ii in c.keys() if ii not in nodes):
            return False
        if len(nodes) == 4 and (any(all([nodes[ii] in g[nodes[i]] for ii in range(4) if ii != i]) for i in range(4)) or any(all(nodes[ii] in g[nodes[jj]] for ii in range(4) for jj in range(4) if ii != i and jj != i and jj != ii) for i in range(4))):
            return False
        # print(nodes, [([nodes[ii] in g[nodes[i]] for ii in range(4) if ii != i]) for i in range(4)])
        return True