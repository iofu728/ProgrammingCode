# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-07-11 12:06:19
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-07-11 12:07:22

"""
817. Linked List Components Medium
We are given head, the head node of a linked list containing unique integer values.

We are also given the list G, a subset of the values in the linked list.

Return the number of connected components in G, where two values are connected if they appear consecutively in the linked list.

Example 1:

Input: 
head: 0->1->2->3
G = [0, 1, 3]
Output: 2
Explanation: 
0 and 1 are connected, so [0, 1] and [3] are the two connected components.
Example 2:

Input: 
head: 0->1->2->3->4
G = [0, 3, 1, 4]
Output: 2
Explanation: 
0 and 1 are connected, 3 and 4 are connected, so [0, 1] and [3, 4] are the two connected components.
Note:

If N is the length of the linked list given by head, 1 <= N <= 10000.
The value of each node in the linked list will be in the range [0, N - 1].
1 <= G.length <= 10000.
G is a subset of all values in the linked list.
Accepted 43,143 Submissions 75,526
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        head_len, now = 0, 0
        t = head
        while t:
            if t.val in G:
                if now == 0:
                    head_len += 1
                now += 1
            else:
                now = 0
            t = t.next
        return head_len
