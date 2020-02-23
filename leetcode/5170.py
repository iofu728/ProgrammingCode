# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-02-23 11:47:15
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-02-23 11:48:00

"""
5170. Validate Binary Tree Nodes
User Accepted:2744
User Tried:2910
Total Accepted:2818
Total Submissions:4003
Difficulty:Medium
You have n binary tree nodes numbered from 0 to n - 1 where node i has two children leftChild[i] and rightChild[i], return true if and only if all the given nodes form exactly one valid binary tree.

If node i has no left child then leftChild[i] will equal -1, similarly for the right child.

Note that the nodes have no values and that we only use the node numbers in this problem.

 

Example 1:



Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]
Output: true
Example 2:



Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]
Output: false
Example 3:



Input: n = 2, leftChild = [1,0], rightChild = [-1,-1]
Output: false
Example 4:



Input: n = 6, leftChild = [1,-1,-1,4,-1,-1], rightChild = [2,-1,-1,5,-1,-1]
Output: false
 

Constraints:

1 <= n <= 10^4
leftChild.length == rightChild.length == n
-1 <= leftChild[i], rightChild[i] <= n - 1
"""


class Solution:
    def validateBinaryTreeNodes(
        self, n: int, leftChild: List[int], rightChild: List[int]
    ) -> bool:
        father_num = self.get_father_num(n, leftChild, rightChild)
        no_father = [ii for ii in father_num if ii == 0]
        more_than_one_father = [ii for ii in father_num if ii > 1]
        if len(no_father) != 1:
            return False
        return len(more_than_one_father) == 0

    def get_father_num(
        self, n: int, leftChild: List[int], rightChild: List[int]
    ) -> list:
        father = {ii: [] for ii in range(n)}
        for fa, (left, right) in enumerate(zip(leftChild, rightChild)):
            if left != -1:
                father[left].append(fa)
            if right != -1:
                father[right].append(fa)
        father_num = [len(v) for k, v in father.items()]
        return father_num

