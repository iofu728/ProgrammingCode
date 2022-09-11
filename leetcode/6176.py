# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2022-09-11 12:43:02
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-09-11 12:43:23

"""
6176. 出现最频繁的偶数元素 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Easy
给你一个整数数组 nums ，返回出现最频繁的偶数元素。

如果存在多个满足条件的元素，只需要返回 最小 的一个。如果不存在这样的元素，返回 -1 。

 

示例 1：

输入：nums = [0,1,2,2,4,4,1]
输出：2
解释：
数组中的偶数元素为 0、2 和 4 ，在这些元素中，2 和 4 出现次数最多。
返回最小的那个，即返回 2 。
示例 2：

输入：nums = [4,4,4,9,2,4]
输出：4
解释：4 是出现最频繁的偶数元素。
示例 3：

输入：nums = [29,47,21,41,13,37,25,7]
输出：-1
解释：不存在偶数元素。
 

提示：

1 <= nums.length <= 2000
0 <= nums[i] <= 105
"""
class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        c = Counter([ii for ii in nums if ii >> 1 << 1 == ii])
        if len(c) == 0:
            return -1
        m = max(c.values())
        for ii in sorted(c.keys()):
            if c[ii] == m:
                return ii