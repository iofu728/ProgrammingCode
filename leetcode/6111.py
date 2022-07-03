# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2022-07-03 11:27:57
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-07-03 11:28:18

"""
6111. 螺旋矩阵 IV 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Medium
给你两个整数：m 和 n ，表示矩阵的维数。

另给你一个整数链表的头节点 head 。

请你生成一个大小为 m x n 的螺旋矩阵，矩阵包含链表中的所有整数。链表中的整数从矩阵 左上角 开始、顺时针 按 螺旋 顺序填充。如果还存在剩余的空格，则用 -1 填充。

返回生成的矩阵。

 

示例 1：


输入：m = 3, n = 5, head = [3,0,2,6,8,1,7,9,4,2,5,5,0]
输出：[[3,0,2,6,8],[5,0,-1,-1,1],[5,2,4,9,7]]
解释：上图展示了链表中的整数在矩阵中是如何排布的。
注意，矩阵中剩下的空格用 -1 填充。
示例 2：


输入：m = 1, n = 4, head = [0,1,2]
输出：[[0,1,2,-1]]
解释：上图展示了链表中的整数在矩阵中是如何从左到右排布的。 
注意，矩阵中剩下的空格用 -1 填充。
 

提示：

1 <= m, n <= 105
1 <= m * n <= 105
链表中节点数目在范围 [1, m * n] 内
0 <= Node.val <= 1000
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        res = [[-1] * n for ii in range(m)]
        K = min(m // 2, n // 2)
        for k in range(K + 1):
            x, y = k, k
            xx = x
            for yy in range(y, n - k):
                if head is None:
                    break
                # print("!", xx, yy, head.val)
                res[xx][yy] = head.val
                head = head.next
            yy = n - k - 1
            for xx in range(x + 1, m - k):
                if head is None:
                    break
                # print("@", xx, yy, head.val)
                res[xx][yy] = head.val
                head = head.next
            xx = m - k -1
            for yy in range(n - k - 2, y - 1, -1):
                if head is None:
                    break
                # print("#", xx, yy, head.val)
                res[xx][yy] = head.val
                head = head.next
            yy = y
            for xx in range(m - k - 2, x, -1):
                if head is None:
                    break
                # print("$", xx, yy, head.val)
                res[xx][yy] = head.val
                head = head.next
            if head is None:
                break
        return res
            
                