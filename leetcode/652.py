# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-07-25 23:17:25
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-07-25 23:18:55

"""
652. Find Duplicate Subtrees Medium
Given a binary tree, return all duplicate subtrees. For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with same node values.

Example 1:

        1
       / \
      2   3
     /   / \
    4   2   4
       /
      4
The following are two duplicate subtrees:

      2
     /
    4
and

    4
Therefore, you need to return above trees' root in the form of a list.
Accepted 63,062 Submissions 126,243
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import Counter, defaultdict


class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        trees = defaultdict()
        trees.default_factory = trees.__len__
        count = Counter()
        ans = []

        def dfs(node):
            if not node:
                return
            idx = trees[node.val, dfs(node.left), dfs(node.right)]
            count[idx] += 1
            if count[idx] == 2:
                ans.append(node)
            return idx

        dfs(root)
        return ans
