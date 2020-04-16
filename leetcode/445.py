# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-04-14 12:21:45
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-04-14 12:22:42

"""
445. Add Two Numbers II Medium
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
Accepted 138,703 Submissions 260,738
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1, s2 = [], []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        res, pre = None, 0
        while s1 or s2 or pre:
            num1 = 0 if not s1 else s1.pop()
            num2 = 0 if not s2 else s2.pop()
            now = num1 + num2 + pre
            pre = now // 10
            now %= 10
            now_node = ListNode(now)
            now_node.next = res
            res = now_node
        return res
