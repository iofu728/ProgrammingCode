# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2024-09-15 12:44:27
# @Last Modified by:   gunjianpan
# @Last Modified time: 2024-09-15 12:44:37

"""
100380. 最高乘法得分 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Medium
给你一个大小为 4 的整数数组 a 和一个大小 至少为 4 的整数数组 b。

你需要从数组 b 中选择四个下标 i0, i1, i2, 和 i3，并满足 i0 < i1 < i2 < i3。你的得分将是 a[0] * b[i0] + a[1] * b[i1] + a[2] * b[i2] + a[3] * b[i3] 的值。

返回你能够获得的 最大 得分。

 

示例 1：

输入： a = [3,2,5,6], b = [2,-6,4,-5,-3,2,-7]

输出： 26

解释：
选择下标 0, 1, 2 和 5。得分为 3 * 2 + 2 * (-6) + 5 * 4 + 6 * 2 = 26。

示例 2：

输入： a = [-1,4,5,-2], b = [-5,-1,-3,-2,-4]

输出： -1

解释：
选择下标 0, 1, 3 和 4。得分为 (-1) * (-5) + 4 * (-1) + 5 * (-2) + (-2) * (-4) = -1。

 

提示：

a.length == 4
4 <= b.length <= 105
-105 <= a[i], b[i] <= 105

"""
class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:

        n = len(b)
        
        # 初始化四个数组，分别表示选择1个、2个、3个和4个数时的最大得分
        dp1 = [float('-inf')] * n
        dp2 = [float('-inf')] * n
        dp3 = [float('-inf')] * n
        dp4 = [float('-inf')] * n
        
        # 遍历数组b
        for i in range(n):
            # 更新选择4个数的最大得分
            if i >= 3:
                dp4[i] = max(dp4[i-1], dp3[i-1] + a[3] * b[i])
            
            # 更新选择3个数的最大得分
            if i >= 2:
                dp3[i] = max(dp3[i-1], dp2[i-1] + a[2] * b[i])
            
            # 更新选择2个数的最大得分
            if i >= 1:
                dp2[i] = max(dp2[i-1], dp1[i-1] + a[1] * b[i])
            
            # 更新选择1个数的最大得分
            dp1[i] = max(dp1[i-1] if i > 0 else float('-inf'), a[0] * b[i])
        
        # 返回选择4个数的最大得分
        return dp4[-1]