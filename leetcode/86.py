# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-06 16:11:02
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-06 16:11:39

"""
86. Partition List Medium
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5
Accepted 225,372 Submissions 538,223
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        before = before_root = ListNode(0)
        after = after_root = ListNode(0)
        while head:
            # print(head.val)
            if head.val < x:
                before.next = head
                before = before.next
            else:
                after.next = head
                after = after.next
            head = head.next
        after.next = None
        before.next = after_root.next
        return before_root.next
