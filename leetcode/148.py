# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-03-22 22:29:13
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-03-22 22:29:57

"""
148. Sort List Medium

Sort a linked list in O(n log n) time using constant space complexity.

## Example 1:

Input: 4->2->1->3
Output: 1->2->3->4

## Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5

Accepted 237,725 Submissions 596,942
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not (head and head.next):
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
        middle = slow.next
        slow.next = None
        left, right = self.sortList(head), self.sortList(middle)
        res = h = ListNode(0)
        while left and right:
            if left.val < right.val:
                h.next = left
                left = left.next
            else:
                h.next = right
                right = right.next
            h = h.next
        h.next = left if left else right
        return res.next
