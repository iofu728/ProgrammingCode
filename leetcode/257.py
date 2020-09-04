# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-04 12:16:58
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-04 12:17:53

"""
257. Binary Tree Paths Easy
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
Accepted 332,688 Submissions 642,761
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def dfs(head: TreeNode, res: list):
            if head.left is None and head.right is None:
                ans.append(res + [head.val])
                return
            if head.left:
                dfs(head.left, res + [head.val])
            if head.right:
                dfs(head.right, res + [head.val])

        ans = []
        if root is None:
            return []
        dfs(root, [])
        return ["->".join([str(jj) for jj in ii]) for ii in ans]
