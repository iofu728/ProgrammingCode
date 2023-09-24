# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2023-09-24 12:47:50
# @Last Modified by:   gunjianpan
# @Last Modified time: 2023-09-24 12:48:06

"""
100047. 统计树中的合法路径数目 显示英文描述 
通过的用户数11
尝试过的用户数17
用户总通过次数11
用户总提交次数26
题目难度Hard
给你一棵 n 个节点的无向树，节点编号为 1 到 n 。给你一个整数 n 和一个长度为 n - 1 的二维整数数组 edges ，其中 edges[i] = [ui, vi] 表示节点 ui 和 vi 在树中有一条边。

请你返回树中的 合法路径数目 。

如果在节点 a 到节点 b 之间 恰好有一个 节点的编号是质数，那么我们称路径 (a, b) 是 合法的 。

注意：

路径 (a, b) 指的是一条从节点 a 开始到节点 b 结束的一个节点序列，序列中的节点 互不相同 ，且相邻节点之间在树上有一条边。
路径 (a, b) 和路径 (b, a) 视为 同一条 路径，且只计入答案 一次 。
 

示例 1：



输入：n = 5, edges = [[1,2],[1,3],[2,4],[2,5]]
输出：4
解释：恰好有一个质数编号的节点路径有：
- (1, 2) 因为路径 1 到 2 只包含一个质数 2 。
- (1, 3) 因为路径 1 到 3 只包含一个质数 3 。
- (1, 4) 因为路径 1 到 4 只包含一个质数 2 。
- (2, 4) 因为路径 2 到 4 只包含一个质数 2 。
只有 4 条合法路径。
示例 2：



输入：n = 6, edges = [[1,2],[1,3],[2,4],[3,5],[3,6]]
输出：6
解释：恰好有一个质数编号的节点路径有：
- (1, 2) 因为路径 1 到 2 只包含一个质数 2 。
- (1, 3) 因为路径 1 到 3 只包含一个质数 3 。
- (1, 4) 因为路径 1 到 4 只包含一个质数 2 。
- (1, 6) 因为路径 1 到 6 只包含一个质数 3 。
- (2, 4) 因为路径 2 到 4 只包含一个质数 2 。
- (3, 6) 因为路径 3 到 6 只包含一个质数 3 。
只有 6 条合法路径。
 

提示：

1 <= n <= 105
edges.length == n - 1
edges[i].length == 2
1 <= ui, vi <= n
输入保证 edges 形成一棵合法的树。
"""
class Solution:
    def countPaths(self, n: int, edges: List[List[int]]) -> int:
        neighbour = collections.defaultdict(set)
        for a, b in edges :
            neighbour[a].add(b)
            neighbour[b].add(a)
        
        def check_p(input_num) :
            if input_num == 1 :
                return False
            ps = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397]
            for pt in ps :
                if pt**2 > input_num :
                    break
                if input_num % pt == 0 :
                    return False
            return True
        
        self.to_ret = 0
        def visit(node=1, ft = -1) :
            is_p = check_p(node)
            to_ret = {0:1, 1:0}
            for sont in neighbour[node] :
                if sont == ft :
                    continue
                rett = visit(sont, node)
                if is_p :
                    self.to_ret += to_ret[0] * rett[0]
                else :
                    self.to_ret += to_ret[0] * rett[1] + to_ret[1] * rett[0]
                to_ret[0] += rett[0]
                to_ret[1] += rett[1]
                
            if is_p :
                to_ret[1] = to_ret[0]
                to_ret[0] = 0
            return to_ret
        visit()
        return self.to_ret
                
