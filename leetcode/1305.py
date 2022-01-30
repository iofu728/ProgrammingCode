# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2022-01-26 20:53:26
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-01-26 20:53:50

"""
1305. 两棵二叉搜索树中的所有元素
给你 root1 和 root2 这两棵二叉搜索树。

请你返回一个列表，其中包含 两棵树 中的所有整数并按 升序 排序。.

 

示例 1：



输入：root1 = [2,1,4], root2 = [1,0,3]
输出：[0,1,1,2,3,4]
示例 2：

输入：root1 = [0,-10,10], root2 = [5,1,7,0,2]
输出：[-10,0,0,1,2,5,7,10]
示例 3：

输入：root1 = [], root2 = [5,1,7,0,2]
输出：[0,1,2,5,7]
示例 4：

输入：root1 = [0,-10,10], root2 = []
输出：[-10,0,10]
示例 5：



输入：root1 = [1,null,8], root2 = [8,1]
输出：[1,1,8,8]
 

提示：

每棵树最多有 5000 个节点。
每个节点的值在 [-10^5, 10^5] 之间。
通过次数16,319提交次数21,809
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def dfs(node, a):
            if node is None:
                return
            dfs(node.left, a)
            a.append(node.val)
            dfs(node.right, a)

        v1, v2 = [], []
        dfs(root1, v1)
        dfs(root2, v2)
        res = []
        l, r = 0, 0
        N, M = len(v1), len(v2)
        while l < N or r < M:
            if l < N and (r == M or v1[l] <= v2[r]):
                res.append(v1[l])
                l += 1
            else:
                res.append(v2[r])
                r += 1
        return res
