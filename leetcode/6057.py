# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2022-05-08 12:41:33
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-05-08 12:42:13

"""
6057. 统计值等于子树平均值的节点数 显示英文描述 
通过的用户数1
尝试过的用户数1
用户总通过次数1
用户总提交次数1
题目难度Medium
给你一棵二叉树的根节点 root ，找出并返回满足要求的节点数，要求节点的值等于其 子树 中值的 平均值 。

注意：

n 个元素的平均值可以由 n 个元素 求和 然后再除以 n ，并 向下舍入 到最近的整数。
root 的 子树 由 root 和它的所有后代组成。
 

示例 1：


输入：root = [4,8,5,0,1,null,6]
输出：5
解释：
对值为 4 的节点：子树的平均值 (4 + 8 + 5 + 0 + 1 + 6) / 6 = 24 / 6 = 4 。
对值为 5 的节点：子树的平均值 (5 + 6) / 2 = 11 / 2 = 5 。
对值为 0 的节点：子树的平均值 0 / 1 = 0 。
对值为 1 的节点：子树的平均值 1 / 1 = 1 。
对值为 6 的节点：子树的平均值 6 / 1 = 6 。
示例 2：


输入：root = [1]
输出：1
解释：对值为 1 的节点：子树的平均值 1 / 1 = 1。
 

提示：

树中节点数目在范围 [1, 1000] 内
0 <= Node.val <= 1000
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def dfs(h):
            if h is None:
                return [0, 0]
            l = dfs(h.left)
            r = dfs(h.right)
            a, b = l[0] + r[0] + h.val, l[1] + r[1] + 1
            if a // b == h.val:
                self.res += 1
            return [a, b]
        self.res = 0
        dfs(root)
        return self.res