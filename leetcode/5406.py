# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-05-10 10:51:40
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-05-10 11:03:10

"""
5406. 收集树上所有苹果的最少时间 显示英文描述 
通过的用户数60
尝试过的用户数70
用户总通过次数60
用户总提交次数80
题目难度Medium
给你一棵有 n 个节点的无向树，节点编号为 0 到 n-1 ，它们中有一些节点有苹果。通过树上的一条边，需要花费 1 秒钟。你从 节点 0 出发，请你返回最少需要多少秒，可以收集到所有苹果，并回到节点 0 。

无向树的边由 edges 给出，其中 edges[i] = [fromi, toi] ，表示有一条边连接 from 和 toi 。除此以外，还有一个布尔数组 hasApple ，其中 hasApple[i] = true 代表节点 i 有一个苹果，否则，节点 i 没有苹果。

示例 1：

输入：n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,true,false,true,true,false]
输出：8 
解释：上图展示了给定的树，其中红色节点表示有苹果。一个能收集到所有苹果的最优方案由绿色箭头表示。
示例 2：

输入：n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,true,false,false,true,false]
输出：6
解释：上图展示了给定的树，其中红色节点表示有苹果。一个能收集到所有苹果的最优方案由绿色箭头表示。
示例 3：

输入：n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,false,false,false,false,false]
输出：0
 

提示：

1 <= n <= 10^5
edges.length == n-1
edges[i].length == 2
0 <= fromi, toi <= n-1
fromi < toi
hasApple.length == n
"""


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        father = {jj if ii < jj else ii: ii if ii < jj else jj for ii, jj in edges}
        need = set()
        for idx, ii in enumerate(hasApple):
            if ii == False:
                continue
            now = idx
            need.add(now)
            while now != 0:
                now = father[now]
                need.add(now)
        # print(need)
        return max(len(need) - 1, 0) * 2
