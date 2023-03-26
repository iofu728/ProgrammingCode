# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2023-03-26 13:16:11
# @Last Modified by:   gunjianpan
# @Last Modified time: 2023-03-26 13:16:24

"""
6356. 收集树中金币 显示英文描述 
通过的用户数9
尝试过的用户数26
用户总通过次数9
用户总提交次数49
题目难度Hard
给你一个 n 个节点的无向无根树，节点编号从 0 到 n - 1 。给你整数 n 和一个长度为 n - 1 的二维整数数组 edges ，其中 edges[i] = [ai, bi] 表示树中节点 ai 和 bi 之间有一条边。再给你一个长度为 n 的数组 coins ，其中 coins[i] 可能为 0 也可能为 1 ，1 表示节点 i 处有一个金币。

一开始，你需要选择树中任意一个节点出发。你可以执行下述操作任意次：

收集距离当前节点距离为 2 以内的所有金币，或者
移动到树中一个相邻节点。
你需要收集树中所有的金币，并且回到出发节点，请你返回最少经过的边数。

如果你多次经过一条边，每一次经过都会给答案加一。

 

示例 1：



输入：coins = [1,0,0,0,0,1], edges = [[0,1],[1,2],[2,3],[3,4],[4,5]]
输出：2
解释：从节点 2 出发，收集节点 0 处的金币，移动到节点 3 ，收集节点 5 处的金币，然后移动回节点 2 。
示例 2：



输入：coins = [0,0,0,1,1,0,0,1], edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[5,6],[5,7]]
输出：2
解释：从节点 0 出发，收集节点 4 和 3 处的金币，移动到节点 2 处，收集节点 7 处的金币，移动回节点 0 。
 

提示：

n == coins.length
1 <= n <= 3 * 104
0 <= coins[i] <= 1
edges.length == n - 1
edges[i].length == 2
0 <= ai, bi < n
ai != bi
edges 表示一棵合法的树。
"""


class Solution:
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        sum_coins = sum(coins)
        if sum_coins <= 1 or len(coins) <= 5:
            return 0
        neighbour = collections.defaultdict(set)
        for a, b in edges:
            neighbour[a].add(b)
            neighbour[b].add(a)

        leaf_1 = set()
        leaf_0 = []
        set_leaf0 = set()
        for t in neighbour:
            if len(neighbour[t]) == 1:
                if coins[t] == 1:
                    leaf_1.add(t)
                else:
                    leaf_0.append(t)
                    set_leaf0.add(t)

        while len(leaf_0):
            tt = leaf_0.pop(0)
            for ft in neighbour[tt]:
                neighbour[ft].remove(tt)
                if len(neighbour[ft]) <= 1 and not ft in set_leaf0:
                    if coins[ft] == 1:
                        leaf_1.add(ft)
                    else:
                        set_leaf0.add(ft)
                        leaf_0.append(ft)

        n_leaf2 = set()
        for t in neighbour:
            if t in leaf_1 or t in set_leaf0:
                continue
            t_neighbour = len(neighbour[t])
            t_n_leaf1 = len([tt for tt in neighbour[t] if tt in leaf_1])
            if t_n_leaf1 >= t_neighbour - 1:
                n_leaf2.add(t)
        nodes = len(neighbour) - len(set_leaf0) - len(leaf_1) - len(n_leaf2)
        # print(set_leaf0)
        # print(leaf_1)
        # print(n_leaf2)
        return max(2 * (nodes - 1), 0)
