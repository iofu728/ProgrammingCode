# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2021-08-15 13:41:53
# @Last Modified by:   gunjianpan
# @Last Modified time: 2021-08-15 13:42:09

"""
5832. 构造元素不等于两相邻元素平均值的数组 显示英文描述 
通过的用户数43
尝试过的用户数58
用户总通过次数43
用户总提交次数61
题目难度Medium
给你一个 下标从 0 开始 的数组 nums ，数组由若干 互不相同的 整数组成。你打算重新排列数组中的元素以满足：重排后，数组中的每个元素都 不等于 其两侧相邻元素的 平均值 。

更公式化的说法是，重新排列的数组应当满足这一属性：对于范围 1 <= i < nums.length - 1 中的每个 i ，(nums[i-1] + nums[i+1]) / 2 不等于 nums[i] 均成立 。

返回满足题意的任一重排结果。

 

示例 1：

输入：nums = [1,2,3,4,5]
输出：[1,2,4,5,3]
解释：
i=1, nums[i] = 2, 两相邻元素平均值为 (1+4) / 2 = 2.5
i=2, nums[i] = 4, 两相邻元素平均值为 (2+5) / 2 = 3.5
i=3, nums[i] = 5, 两相邻元素平均值为 (4+3) / 2 = 3.5
示例 2：

输入：nums = [6,2,0,9,7]
输出：[9,7,6,2,0]
解释：
i=1, nums[i] = 7, 两相邻元素平均值为 (9+6) / 2 = 7.5
i=2, nums[i] = 6, 两相邻元素平均值为 (7+2) / 2 = 4.5
i=3, nums[i] = 2, 两相邻元素平均值为 (6+0) / 2 = 3
 

提示：

3 <= nums.length <= 105
0 <= nums[i] <= 105
"""


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        N = len(nums)
        nums = sorted(nums)
        res = [0] * N
        for ii in range((N + 1) // 2):
            res[ii * 2] = nums[ii]
        for ii in range(N // 2):
            res[ii * 2 + 1] = nums[N - 1 - ii]
        return res
