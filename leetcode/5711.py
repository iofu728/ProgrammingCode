# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2021-03-21 13:25:03
# @Last Modified by:   gunjianpan
# @Last Modified time: 2021-03-21 13:25:18

'''
5711. 有界数组中指定下标处的最大值 显示英文描述 
通过的用户数801
尝试过的用户数1630
用户总通过次数809
用户总提交次数5012
题目难度Medium
给你三个正整数 n、index 和 maxSum 。你需要构造一个同时满足下述所有条件的数组 nums（下标 从 0 开始 计数）：

nums.length == n
nums[i] 是 正整数 ，其中 0 <= i < n
abs(nums[i] - nums[i+1]) <= 1 ，其中 0 <= i < n-1
nums 中所有元素之和不超过 maxSum
nums[index] 的值被 最大化
返回你所构造的数组中的 nums[index] 。

注意：abs(x) 等于 x 的前提是 x >= 0 ；否则，abs(x) 等于 -x 。

 

示例 1：

输入：n = 4, index = 2,  maxSum = 6
输出：2
解释：数组 [1,1,2,1] 和 [1,2,2,1] 满足所有条件。不存在其他在指定下标处具有更大值的有效数组。
示例 2：

输入：n = 6, index = 1,  maxSum = 10
输出：3
 

提示：

1 <= n <= maxSum <= 109
0 <= index < n
'''

class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        l, r = 0, maxSum + 1
        while l + 1 < r:
            mid = l + r >> 1
            a = max(0, mid - index)
            b = max(0, mid - (n - 1- index))
            if ((a + mid) * (mid - a + 1) + (b + mid) * (mid - b + 1) <= (maxSum + mid - n) * 2):
                l = mid
            else:
                r = mid
        return r
