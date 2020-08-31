# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-08-31 18:19:46
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-08-31 18:20:21

"""
1373. Maximum Sum BST in Binary Tree Hard
Given a binary tree root, the task is to return the maximum sum of all keys of any sub-tree which is also a Binary Search Tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:



Input: root = [1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]
Output: 20
Explanation: Maximum sum in a valid Binary search tree is obtained in root node with key equal to 3.
Example 2:



Input: root = [4,3,null,1,2]
Output: 2
Explanation: Maximum sum in a valid Binary search tree is obtained in a single root node with key equal to 2.
Example 3:

Input: root = [-4,-2,-5]
Output: 0
Explanation: All values are negatives. Return an empty BST.
Example 4:

Input: root = [2,1,3]
Output: 6
Example 5:

Input: root = [5,4,8,3,null,6,3]
Output: 7
 

Constraints:

The given binary tree will have between 1 and 40000 nodes.
Each node's value is between [-4 * 10^4 , 4 * 10^4].
Accepted 8,453 Submissions 21,264
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: TreeNode) -> int:
        def dfs(now: TreeNode):
            # print(now.val)
            if now.left is None and now.right is None:
                self.res = max(self.res, now.val)
                return (now.val, now.val, now.val)
            res = now.val
            now_min, now_max = now.val, now.val
            valid = True
            if now.left:
                l_v, l_min, l_max = dfs(now.left)
                if l_max >= now.val or l_v is False:
                    valid = False
                else:
                    res += l_v
                    now_min = l_min
            if now.right:
                r_v, r_min, r_max = dfs(now.right)
                if r_min <= now.val or r_v is False:
                    valid = False
                else:
                    res += r_v
                    now_max = r_max
            if valid is False:
                return (False, now_min, now_max)
            self.res = max(self.res, res)
            return (res, now_min, now_max)

        self.res = 0
        dfs(root)
        return self.res

