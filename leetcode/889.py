# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-10-23 22:53:38
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-10-23 22:54:31

"""
889. Construct Binary Tree from Preorder and Postorder Traversal Medium
Return any binary tree that matches the given preorder and postorder traversals.

Values in the traversals pre and post are distinct positive integers.

 

Example 1:

Input: pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
Output: [1,2,3,4,5,6,7]
 

Note:

1 <= pre.length == post.length <= 30
pre[] and post[] are both permutations of 1, 2, ..., pre.length.
It is guaranteed an answer exists. If there exists multiple answers, you can return any of them.
Accepted 41,746 Submissions 62,647
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        if not pre:
            return None
        now = TreeNode(pre[0])
        if len(pre) == 1:
            return now
        idx = post.index(pre[1]) + 1
        now.left = self.constructFromPrePost(pre[1 : idx + 1], post[:idx])
        now.right = self.constructFromPrePost(pre[idx + 1 :], post[idx:-1])
        return now
