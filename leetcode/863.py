# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-12-21 23:43:27
# @Last Modified by:   gunjianpan
# @Last Modified time: 2021-07-28 00:13:13

"""
863. All Nodes Distance K in Binary Tree Medium
We are given a binary tree (with root node root), a target node, and an integer value K.

Return a list of the values of all nodes that have a distance K from the target node.  The answer can be returned in any order.

 

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2

Output: [7,4,1]

Explanation: 
The nodes that are a distance 2 from the target node (with value 5)
have values 7, 4, and 1.



Note that the inputs "root" and "target" are actually TreeNodes.
The descriptions of the inputs above are just serializations of these objects.
 

Note:

The given tree is non-empty.
Each node in the tree has unique values 0 <= node.val <= 500.
The target node is a node in the tree.
0 <= K <= 1000.
Accepted 106,824 Submissions 186,768
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        g = defaultdict(list)
        queue = [root]
        while queue:
            top = queue.pop(0)
            if top.left:
                g[top.val].append(top.left.val)
                g[top.left.val].append(top.val)
                queue.append(top.left)
            if top.right:
                g[top.val].append(top.right.val)
                g[top.right.val].append(top.val)
                queue.append(top.right)
        queue = [(target.val, 0)]
        res, have = [], set()
        while queue:
            top, h = queue.pop(0)
            if h > k:
                break
            have.add(top)
            if h == k:
                res.append(top)
            for ii in g[top]:
                if ii not in have:
                    queue.append((ii, h + 1))
        return res
