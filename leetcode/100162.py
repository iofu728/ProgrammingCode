# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2024-01-14 15:16:56
# @Last Modified by:   gunjianpan
# @Last Modified time: 2024-01-14 15:17:05

"""
100162. 最大频率元素计数 显示英文描述 
通过的用户数2621
尝试过的用户数2648
用户总通过次数2661
用户总提交次数3444
题目难度Easy
给你一个由 正整数 组成的数组 nums 。

返回数组 nums 中所有具有 最大 频率的元素的 总频率 。

元素的 频率 是指该元素在数组中出现的次数。

 

示例 1：

输入：nums = [1,2,2,3,1,4]
输出：4
解释：元素 1 和 2 的频率为 2 ，是数组中的最大频率。
因此具有最大频率的元素在数组中的数量是 4 。
示例 2：

输入：nums = [1,2,3,4,5]
输出：5
解释：数组中的所有元素的频率都为 1 ，是最大频率。
因此具有最大频率的元素在数组中的数量是 5 。
 

提示：

1 <= nums.length <= 100
1 <= nums[i] <= 100
"""
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        c = Counter(nums)
        y = max(c.values())
        return sum([j for i, j in c.items() if j == y])