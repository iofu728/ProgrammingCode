# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2022-03-06 11:06:40
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-03-06 11:06:54

"""
6018. 根据描述创建二叉树 显示英文描述 
通过的用户数5
尝试过的用户数5
用户总通过次数5
用户总提交次数5
题目难度Medium
给你一个二维整数数组 descriptions ，其中 descriptions[i] = [parenti, childi, isLefti] 表示 parenti 是 childi 在 二叉树 中的 父节点，二叉树中各节点的值 互不相同 。此外：

如果 isLefti == 1 ，那么 childi 就是 parenti 的左子节点。
如果 isLefti == 0 ，那么 childi 就是 parenti 的右子节点。
请你根据 descriptions 的描述来构造二叉树并返回其 根节点 。

测试用例会保证可以构造出 有效 的二叉树。

 

示例 1：



输入：descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
输出：[50,20,80,15,17,19]
解释：根节点是值为 50 的节点，因为它没有父节点。
结果二叉树如上图所示。
示例 2：



输入：descriptions = [[1,2,1],[2,3,0],[3,4,1]]
输出：[1,2,null,null,3,4]
解释：根节点是值为 1 的节点，因为它没有父节点。 
结果二叉树如上图所示。 
 

提示：

1 <= descriptions.length <= 104
descriptions[i].length == 3
1 <= parenti, childi <= 105
0 <= isLefti <= 1
descriptions 所描述的二叉树是一棵有效二叉树
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        g, outer, nodes, gg, x = {}, defaultdict(set), set(), {}, defaultdict(set)
        for ii, jj, kk in descriptions:
            nodes.add(ii)
            nodes.add(jj)
            outer[ii].add(jj)
            x[jj].add(ii)
            # ins[jj] += 1
            if ii not in g:
                g[ii] = [0, 0]
            if kk == 0:
                g[ii][1] = jj
            else:
                g[ii][0] = jj
        q = deque([ii for ii in nodes if len(outer[ii]) == 0])
        tmp = None
        while q:
            head = q.popleft()
            tmp = TreeNode(head)
            if head in g and g[head][0] != 0:
                tmp.left = gg[g[head][0]]
            if head in g and g[head][1] != 0:
                tmp.right = gg[g[head][1]]
            gg[head] = tmp
            for ii in x[head]:
                outer[ii].remove(head)
                if len(outer[ii]) == 0:
                    q.append(ii)
        return tmp
