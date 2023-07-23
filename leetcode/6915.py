# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2023-07-23 17:08:56
# @Last Modified by:   gunjianpan
# @Last Modified time: 2023-07-23 17:09:07

"""
6915. 合并后数组中的最大元素 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Medium
给你一个下标从 0 开始、由正整数组成的数组 nums 。

你可以在数组上执行下述操作 任意 次：

选中一个同时满足 0 <= i < nums.length - 1 和 nums[i] <= nums[i + 1] 的整数 i 。将元素 nums[i + 1] 替换为 nums[i] + nums[i + 1] ，并从数组中删除元素 nums[i] 。
返回你可以从最终数组中获得的 最大 元素的值。

 

示例 1：

输入：nums = [2,3,7,9,3]
输出：21
解释：我们可以在数组上执行下述操作：
- 选中 i = 0 ，得到数组 nums = [5,7,9,3] 。
- 选中 i = 1 ，得到数组 nums = [5,16,3] 。
- 选中 i = 0 ，得到数组 nums = [21,3] 。
最终数组中的最大元素是 21 。可以证明我们无法获得更大的元素。
示例 2：

输入：nums = [5,3,3]
输出：11
解释：我们可以在数组上执行下述操作：
- 选中 i = 1 ，得到数组 nums = [5,6] 。
- 选中 i = 0 ，得到数组 nums = [11] 。
最终数组中只有一个元素，即 11 。
 

提示：

1 <= nums.length <= 105
1 <= nums[i] <= 106
"""
class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        res = 0
        while nums:
            if len(nums) == 1:
                y = nums.pop()
                res = max(res, y)
            else:
                y1, y2 = nums[-2], nums[-1]
                if y2 < y1:
                    res = max(res, y2)
                    nums.pop()
                else:
                    nums.pop()
                    nums.pop()
                    nums.append(y1 + y2)
        return res
            