"""
6247. 从链表中移除节点 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Medium
给你一个链表的头节点 head 。

对于列表中的每个节点 node ，如果其右侧存在一个具有 严格更大 值的节点，则移除 node 。

返回修改后链表的头节点 head 。

 

示例 1：



输入：head = [5,2,13,3,8]
输出：[13,8]
解释：需要移除的节点是 5 ，2 和 3 。
- 节点 13 在节点 5 右侧。
- 节点 13 在节点 2 右侧。
- 节点 8 在节点 3 右侧。
示例 2：

输入：head = [1,1,1,1]
输出：[1,1,1,1]
解释：每个节点的值都是 1 ，所以没有需要移除的节点。
 

提示：

给定列表中的节点数目在范围 [1, 105] 内
1 <= Node.val <= 105
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = ListNode(10 ** 9 + 7)
        root.next = head
        now = head
        res = [root]
        while now is not None:
            while res and res[-1].val < now.val:
                fa = res.pop()
                res[-1].next = now
            
            res.append(now)
            now = now.next
        return root.next
            