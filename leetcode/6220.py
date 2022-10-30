# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2022-10-30 11:09:18
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-10-30 11:09:33

"""
6220. 可被三整除的偶数的平均值 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Easy
给你一个由正整数组成的整数数组 nums ，返回其中可被 3 整除的所有偶数的平均值。

注意：n 个元素的平均值等于 n 个元素 求和 再除以 n ，结果 向下取整 到最接近的整数。

 

示例 1：

输入：nums = [1,3,6,10,12,15]
输出：9
解释：6 和 12 是可以被 3 整除的偶数。(6 + 12) / 2 = 9 。
示例 2：

输入：nums = [1,2,4,7,10]
输出：0
解释：不存在满足题目要求的整数，所以返回 0 。
 

提示：

1 <= nums.length <= 1000
1 <= nums[i] <= 1000
"""
class Solution:
    def averageValue(self, nums: List[int]) -> int:
        x = [ii for ii in nums if ii % 3 == 0 and ii % 2 == 0]
        
        return sum(x) // len(x) if len(x) else 0