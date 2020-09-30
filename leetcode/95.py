# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-28 21:36:36
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-28 21:47:43

"""
95. Unique Binary Search Trees II Medium
Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

Example:

Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
 

Constraints:

0 <= n <= 8
Accepted 204,251 Submissions 495,849
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def dfs(pre: list):
            if len(pre) <= 1:
                if len(pre) == 1:
                    return [TreeNode(pre[0])]
                return [None]
            res = []
            for ii in range(len(pre)):
                for left in dfs(pre[:ii]):
                    for right in dfs(pre[ii + 1 :]):
                        tmp = TreeNode(pre[ii])
                        tmp.left = left
                        tmp.right = right
                        res.append(tmp)
            # print(pre, res)
            return res

        if n == 0:
            return None
        return dfs(list(range(1, n + 1)))
