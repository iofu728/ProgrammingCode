# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2022-08-07 14:19:24
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-08-07 14:27:23

"""
6137. 检查数组是否存在有效划分 显示英文描述 
通过的用户数4
尝试过的用户数4
用户总通过次数4
用户总提交次数5
题目难度Medium
给你一个下标从 0 开始的整数数组 nums ，你必须将数组划分为一个或多个 连续 子数组。

如果获得的这些子数组中每个都能满足下述条件 之一 ，则可以称其为数组的一种 有效 划分：

子数组 恰 由 2 个相等元素组成，例如，子数组 [2,2] 。
子数组 恰 由 3 个相等元素组成，例如，子数组 [4,4,4] 。
子数组 恰 由 3 个连续递增元素组成，并且相邻元素之间的差值为 1 。例如，子数组 [3,4,5] ，但是子数组 [1,3,5] 不符合要求。
如果数组 至少 存在一种有效划分，返回 true ，否则，返回 false 。

 

示例 1：

输入：nums = [4,4,4,5,6]
输出：true
解释：数组可以划分成子数组 [4,4] 和 [4,5,6] 。
这是一种有效划分，所以返回 true 。
示例 2：

输入：nums = [1,1,1,2]
输出：false
解释：该数组不存在有效划分。
 

提示：

2 <= nums.length <= 105
1 <= nums[i] <= 106
"""


class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        @lru_cache(None)
        def dfs(x):
            if x >= N:
                self.res = True
                return
            if x == N - 1:
                return
            if self.res:
                return
            end = x
            flag = 2
            if nums[x] == nums[x + 1]:
                flag = 0
                while end + 1 < N and nums[x] == nums[end + 1]:
                    end += 1
                if end - x > 1:
                    dfs(end)
                dfs(end + 1)
            elif nums[x] + 1 == nums[x + 1]:
                flag = 1
                # print(x)
                while end + 1 < N and nums[end + 1] == nums[end] + 1:
                    end += 1
                if (end - x + 1) % 3 == 0:
                    dfs(end + 1)
                elif end - x + 1 > 3:
                    dfs(end + 1 - (end - x + 1) % 3)
            # print(x, end, flag)

        N = len(nums)
        self.res = False
        dfs(0)
        return self.res
