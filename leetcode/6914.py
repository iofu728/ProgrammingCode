# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2023-08-13 11:21:15
# @Last Modified by:   gunjianpan
# @Last Modified time: 2023-08-13 11:21:24

"""
6914. 翻倍以链表形式表示的数字 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Medium
给你一个 非空 链表的头节点 head ，表示一个不含前导零的非负数整数。

将链表 翻倍 后，返回头节点 head 。

 

示例 1：


输入：head = [1,8,9]
输出：[3,7,8]
解释：上图中给出的链表，表示数字 189 。返回的链表表示数字 189 * 2 = 378 。
示例 2：


输入：head = [9,9,9]
输出：[1,9,9,8]
解释：上图中给出的链表，表示数字 999 。返回的链表表示数字 999 * 2 = 1998 。
 

提示：

链表中节点的数目在范围 [1, 104] 内
0 <= Node.val <= 9
生成的输入满足：链表表示一个不含前导零的数字，除了数字 0 本身。
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
sys.set_int_max_str_digits(0)
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        num = 0
        root = head
        while head:
            num = num * 10 + head.val
            head = head.next
        y = str(num * 2)
        res = head = ListNode(0)
        for ii in y:
            head.next = ListNode(int(ii))
            head = head.next
        return res.next
        
        