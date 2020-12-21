# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-12-21 23:43:27
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-12-21 23:44:06

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
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        def dfs(now, previous):
            if now is None or self.done is True:
                return
            # previous.append(now)
            if target.val == now.val:
                self.previous = previous + [now]
                self.done = True
                return
            dfs(now.left, previous + [now])
            dfs(now.right, previous + [now])
        def dfs2(now, need):
            if need < 0 or now is None:
                return
            if need == 0 and (now != target or K == 0):
                self.res.append(now.val)
                return

            if now.left not in self.previous:
                dfs2(now.left, need - 1)
            if now.right not in self.previous:
                dfs2(now.right, need - 1)
            
        self.done = False
        self.previous = []
        self.res = []
        dfs(root, [])
        for ii in range(min(K + 1, len(self.previous))):
            # print(self.previous[-1 * (ii + 1)], K - ii)
            dfs2(self.previous[-1 * (ii + 1)], K - ii)
        return self.res