# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-27 00:22:24
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-27 00:22:31

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        def dfs(head: TreeNode):
            if not self.res is None:
                return [False, False]
            if head is None:
                return [False, False]
            if head.left is None and head.right is None:
                return [head.val == p.val, head.val == q.val]
            l1, l2 = dfs(head.left)
            r1, r2 = dfs(head.right)
            l = l1 or r1 or head.val == p.val
            r = l2 or r2 or head.val == q.val
            # print(l, r, head.val)
            if l and r:
                if self.res is None:
                    self.res = head
            return [l, r]

        self.res = None
        dfs(root)
        return self.res
