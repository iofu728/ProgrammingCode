# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-03-25 22:48:00
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-03-25 22:48:56

"""
23. Merge k Sorted Lists Hard

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

## Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6

Accepted 570,196 Submissions 1,480,004
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from queue import PriorityQueue


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = p = ListNode(0)
        q = PriorityQueue()
        for idx, l in enumerate(lists):
            if l:
                q.put((l.val, idx, l))
        while not q.empty():
            front, idx, node = q.get()
            p.next = ListNode(front)
            p = p.next
            node = node.next
            if node:
                q.put((node.val, idx, node))
        return head.next
