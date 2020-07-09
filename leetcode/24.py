# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-07-09 00:02:21
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-07-09 00:02:59

"""
24. Swap Nodes in Pairs Medium
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
Accepted 467,900 Submissions 936,482
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        root = front = ListNode(0)
        root.next = head
        while head and head.next:
            tmp = head.next
            head.next = head.next.next
            tmp.next = head
            front.next = tmp
            head = tmp.next.next
            front = front.next.next
            # print(head)
        return root.next
