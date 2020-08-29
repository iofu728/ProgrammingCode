# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-08-29 20:21:42
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-08-29 20:22:34

"""
919. Complete Binary Tree Inserter Medium
A complete binary tree is a binary tree in which every level, except possibly the last, is completely filled, and all nodes are as far left as possible.

Write a data structure CBTInserter that is initialized with a complete binary tree and supports the following operations:

CBTInserter(TreeNode root) initializes the data structure on a given tree with head node root;
CBTInserter.insert(int v) will insert a TreeNode into the tree with value node.val = v so that the tree remains complete, and returns the value of the parent of the inserted TreeNode;
CBTInserter.get_root() will return the head node of the tree.
 

Example 1:

Input: inputs = ["CBTInserter","insert","get_root"], inputs = [[[1]],[2],[]]
Output: [null,1,[1,2]]
Example 2:

Input: inputs = ["CBTInserter","insert","insert","get_root"], inputs = [[[1,2,3,4,5,6]],[7],[8],[]]
Output: [null,3,4,[1,2,3,4,5,6,7,8]]

Note:

The initial given tree is complete and contains between 1 and 1000 nodes.
CBTInserter.insert is called at most 10000 times per test case.
Every value of a given or inserted node is between 0 and 5000.

Accepted 16,989 Submissions 29,594
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class CBTInserter:
    def __init__(self, root: TreeNode):
        self.root = root
        self.deque = deque()
        q = deque([root])
        while q:
            tmp = q.popleft()
            if not tmp.left or not tmp.right:
                self.deque.append(tmp)
            if tmp.left:
                q.append(tmp.left)
            if tmp.right:
                q.append(tmp.right)

    def insert(self, v: int) -> int:
        tmp = self.deque[0]
        self.deque.append(TreeNode(v))
        if not tmp.left:
            tmp.left = self.deque[-1]
        else:
            tmp.right = self.deque[-1]
            self.deque.popleft()
        return tmp.val

    def get_root(self) -> TreeNode:
        return self.root


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()
