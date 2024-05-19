# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2024-05-19 11:36:24
# @Last Modified by:   gunjianpan
# @Last Modified time: 2024-05-19 11:36:34

"""
100310. 特殊数组 I 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Easy
如果数组的每一对相邻元素都是两个奇偶性不同的数字，则该数组被认为是一个 特殊数组 。

Aging 有一个整数数组 nums。如果 nums 是一个 特殊数组 ，返回 true，否则返回 false。

 

示例 1：

输入：nums = [1]

输出：true

解释：

只有一个元素，所以答案为 true。

示例 2：

输入：nums = [2,1,4]

输出：true

解释：

只有两对相邻元素： (2,1) 和 (1,4)，它们都包含了奇偶性不同的数字，因此答案为 true。

示例 3：

输入：nums = [4,3,1,6]

输出：false

解释：

nums[1] 和 nums[2] 都是奇数。因此答案为 false。

 

提示：

1 <= nums.length <= 100
1 <= nums[i] <= 100
"""
class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        pre = nums[0] % 2
        for ii in nums[1:]:
            now = ii % 2
            if now == pre:
                return False
            pre = now
        return True