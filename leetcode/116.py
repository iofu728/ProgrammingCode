# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-15 12:25:02
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-15 12:25:46

"""
116. Populating Next Right Pointers in Each Node Medium
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

 

Follow up:

You may only use constant extra space.
Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.
 

Example 1:



Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
 

Constraints:

The number of nodes in the given tree is less than 4096.
-1000 <= node.val <= 1000
Accepted 387,590 Submissions 844,057
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
import heapq


class Solution:
    def connect(self, root: "Node") -> "Node":
        origin = root
        if root is None:
            return root
        pre = {}
        queue, idx = [], 1
        heapq.heappush(queue, (0, 0, root))
        while queue:
            _, h, head = heapq.heappop(queue)
            if h in pre:
                pre[h].next = head
            pre[h] = head
            if head.left:
                heapq.heappush(queue, (idx, h + 1, head.left))
                idx += 1
            if head.right:
                heapq.heappush(queue, (idx, h + 1, head.right))
                idx += 1
        return origin
