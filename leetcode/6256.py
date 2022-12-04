
'''
6256. 将节点分成尽可能多的组 显示英文描述 
通过的用户数1
尝试过的用户数2
用户总通过次数1
用户总提交次数4
题目难度Hard
给你一个正整数 n ，表示一个 无向 图中的节点数目，节点编号从 1 到 n 。

同时给你一个二维整数数组 edges ，其中 edges[i] = [ai, bi] 表示节点 ai 和 bi 之间有一条 双向 边。注意给定的图可能是不连通的。

请你将图划分为 m 个组（编号从 1 开始），满足以下要求：

图中每个节点都只属于一个组。
图中每条边连接的两个点 [ai, bi] ，如果 ai 属于编号为 x 的组，bi 属于编号为 y 的组，那么 |y - x| = 1 。
请你返回最多可以将节点分为多少个组（也就是最大的 m ）。如果没办法在给定条件下分组，请你返回 -1 。

 

示例 1：



输入：n = 6, edges = [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]
输出：4
解释：如上图所示，
- 节点 5 在第一个组。
- 节点 1 在第二个组。
- 节点 2 和节点 4 在第三个组。
- 节点 3 和节点 6 在第四个组。
所有边都满足题目要求。
如果我们创建第五个组，将第三个组或者第四个组中任何一个节点放到第五个组，至少有一条边连接的两个节点所属的组编号不符合题目要求。
示例 2：

输入：n = 3, edges = [[1,2],[2,3],[3,1]]
输出：-1
解释：如果我们将节点 1 放入第一个组，节点 2 放入第二个组，节点 3 放入第三个组，前两条边满足题目要求，但第三条边不满足题目要求。
没有任何符合题目要求的分组方式。
 

提示：

1 <= n <= 500
1 <= edges.length <= 104
edges[i].length == 2
1 <= ai, bi <= n
ai != bi
两个点之间至多只有一条边。
'''
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, a):
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a

    def merge(self, a, b):
        self.parent[self.find(b)] = self.find(a)

class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        path = defaultdict(list)
        union = UnionFind(n+1)
        for x, y in edges:
            union.merge(x, y)
            path[x].append(y)
            path[y].append(x)
        ans = [-1] *(n+1)
        for i in range(1, n+1):
            if ans[i] == -1:
                ans[i] = 0
                q = deque([i])
                while q:
                    p = q.popleft()
                    for newp in path[p]:
                        if ans[newp] == -1:
                            ans[newp] = 1 - ans[p]
                            q.append(newp)
                        elif ans[newp] + ans[p] != 1: return -1
        visited = defaultdict(int)
        for i in range(1, n+1):
            ans[i] = 0
            q = deque([i])
            v = {i}
            cnt = 0
            while q:
                cnt += 1
                for _ in range(len(q)):
                    p = q.popleft()
                    for newp in path[p]:
                        if newp not in v:
                            v.add(newp)
                            q.append(newp)
            visited[union.find(i)] = max(visited[union.find(i)], cnt)
        return sum(visited.values())