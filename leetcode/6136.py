# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2022-08-07 14:18:47
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-08-07 14:19:03

"""
6136. 算术三元组的数目 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Easy
给你一个下标从 0 开始、严格递增 的整数数组 nums 和一个正整数 diff 。如果满足下述全部条件，则三元组 (i, j, k) 就是一个 算术三元组 ：

i < j < k ，
nums[j] - nums[i] == diff 且
nums[k] - nums[j] == diff
返回不同 算术三元组 的数目。

 

示例 1：

输入：nums = [0,1,4,6,7,10], diff = 3
输出：2
解释：
(1, 2, 4) 是算术三元组：7 - 4 == 3 且 4 - 1 == 3 。
(2, 4, 5) 是算术三元组：10 - 7 == 3 且 7 - 4 == 3 。
示例 2：

输入：nums = [4,5,6,7,8,9], diff = 2
输出：2
解释：
(0, 2, 4) 是算术三元组：8 - 6 == 2 且 6 - 4 == 2 。
(1, 3, 5) 是算术三元组：9 - 7 == 2 且 7 - 5 == 2 。
 

提示：

3 <= nums.length <= 200
0 <= nums[i] <= 200
1 <= diff <= 50
nums 严格 递增
"""


class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        c = Counter(nums)
        res = 0
        for a1, b1 in c.items():
            a2 = diff + a1
            a3 = 2 * diff + a1
            res += b1 * c.get(a2, 0) * c.get(a3, 0)
        return res
