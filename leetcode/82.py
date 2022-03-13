# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2022-03-09 21:43:06
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-03-09 21:47:11

"""
82. 删除排序链表中的重复元素 II
给定一个已排序的链表的头 head ， 删除原始链表中所有重复数字的节点，只留下不同的数字 。返回 已排序的链表 。

 

示例 1：


输入：head = [1,2,3,3,4,4,5]
输出：[1,2,5]
示例 2：


输入：head = [1,1,1,2,3]
输出：[2,3]
 

提示：

链表中节点数目在范围 [0, 300] 内
-100 <= Node.val <= 100
题目数据保证链表已经按升序 排列
通过次数226,771提交次数425,661
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = h = ListNode(0)
        while head:
            now = head.val
            idx = 0
            while head.next:
                if head.next.val != now:
                    break
                head = head.next
                idx += 1
            # print(head.val, idx)
            if not idx:
                h.next = head
                h = h.next
            head = head.next
        h.next = None
        return res.next
