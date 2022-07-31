"""
6134. 找到离给定两个节点最近的节点 显示英文描述 
通过的用户数21
尝试过的用户数38
用户总通过次数21
用户总提交次数43
题目难度Medium
给你一个 n 个节点的 有向图 ，节点编号为 0 到 n - 1 ，每个节点 至多 有一条出边。

有向图用大小为 n 下标从 0 开始的数组 edges 表示，表示节点 i 有一条有向边指向 edges[i] 。如果节点 i 没有出边，那么 edges[i] == -1 。

同时给你两个节点 node1 和 node2 。

请你返回一个从 node1 和 node2 都能到达节点的编号，使节点 node1 和节点 node2 到这个节点的距离 较大值最小化。如果有多个答案，请返回 最小 的节点编号。如果答案不存在，返回 -1 。

注意 edges 可能包含环。

 

示例 1：



输入：edges = [2,2,3,-1], node1 = 0, node2 = 1
输出：2
解释：从节点 0 到节点 2 的距离为 1 ，从节点 1 到节点 2 的距离为 1 。
两个距离的较大值为 1 。我们无法得到一个比 1 更小的较大值，所以我们返回节点 2 。
示例 2：



输入：edges = [1,2,-1], node1 = 0, node2 = 2
输出：2
解释：节点 0 到节点 2 的距离为 2 ，节点 2 到它自己的距离为 0 。
两个距离的较大值为 2 。我们无法得到一个比 2 更小的较大值，所以我们返回节点 2 。
 

提示：

n == edges.length
2 <= n <= 105
-1 <= edges[i] < n
edges[i] != i
0 <= node1, node2 < n
"""


class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        res = 0
        a, b, a_d, b_d = node1, node2, set([node1]), set([node2])
        while a != b:
            # print(a, b)
            a = edges[a] if a is not None else None
            b = edges[b] if b is not None else None
            if a == -1:
                a = None
            if b == -1:
                b = None
            # print(a, b, a_d, b_d)
            if a is not None and (a in b_d or a == b):
                if b is not None and b in a_d and b < a:
                    return b
                return a
            elif b is not None and b in a_d:
                if a is not None and a in b_d and b > a:
                    return a
                return b
            if a in a_d:
                a = None
            else:
                a_d.add(a)
            if b in b_d:
                b = None
            else:
                b_d.add(b)
            res += 1
        return a if a is not None and a == b else -1
