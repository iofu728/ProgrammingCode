# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-03-22 15:47:23
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-03-22 18:07:29

"""
61. Rotate List Medium

Given a linked list, rotate the list to the right by k places, where k is non-negative.

## Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL

## Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL

Accepted 245,128 Submissions 844,645
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None or k == 0:
            return head
        L = head
        link_num = 1
        while head.next is not None:
            link_num += 1
            head = head.next
        if link_num == 1 or k % link_num == 0:
            return L
        R = head
        shift_num = link_num - k % link_num - 1
        H = L
        idx = 0
        while idx < shift_num:
            H = H.next
            idx += 1
        M = H.next
        H.next = None
        R.next = L
        return M