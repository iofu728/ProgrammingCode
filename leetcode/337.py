# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-03 19:04:43
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-03 19:08:53

"""
337. House Robber III Medium
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:

Input: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \ 
     3   1

Output: 7 
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:

Input: [3,4,5,1,3,null,1]

     3
    / \
   4   5
  / \   \ 
 1   3   1

Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.
Accepted 164,897 Submissions 325,153
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def rob(self, root: TreeNode) -> int:
        def dfs(r: TreeNode):
            if r is None:
                return 0, 0
            left = dfs(r.left)
            right = dfs(r.right)
            v1 = left[1] + right[1] + r.val
            v2 = max(left) + max(right)
            return v1, v2

        return max(dfs(root))
