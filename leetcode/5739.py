# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2021-04-25 10:32:10
# @Last Modified by:   gunjianpan
# @Last Modified time: 2021-04-25 10:55:05
"""
5739. 最高频元素的频数 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Medium
元素的 频数 是该元素在一个数组中出现的次数。

给你一个整数数组 nums 和一个整数 k 。在一步操作中，你可以选择 nums 的一个下标，并将该下标对应元素的值增加 1 。

执行最多 k 次操作后，返回数组中最高频元素的 最大可能频数 。

 

示例 1：

输入：nums = [1,2,4], k = 5
输出：3
解释：对第一个元素执行 3 次递增操作，对第二个元素执 2 次递增操作，此时 nums = [4,4,4] 。
4 是数组中最高频元素，频数是 3 。
示例 2：

输入：nums = [1,4,8,13], k = 5
输出：2
解释：存在多种最优解决方案：
- 对第一个元素执行 3 次递增操作，此时 nums = [4,4,8,13] 。4 是数组中最高频元素，频数是 2 。
- 对第二个元素执行 4 次递增操作，此时 nums = [1,8,8,13] 。8 是数组中最高频元素，频数是 2 。
- 对第三个元素执行 5 次递增操作，此时 nums = [1,4,13,13] 。13 是数组中最高频元素，频数是 2 。
示例 3：

输入：nums = [3,9,6], k = 2
输出：1
 

提示：

1 <= nums.length <= 105
1 <= nums[i] <= 105
1 <= k <= 105
"""


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        N = len(nums)
        nums = sorted(nums)
        sums = [0]
        for ii in range(N):
            sums.append(sums[-1] + nums[ii])
        # print(sums)
        res = 1
        for ii in range(1, N):
            jj = ii - res
            while jj >= -1 and sums[ii + 1] - sums[jj + 1] + k >= (ii - jj) * nums[ii]:
                res = ii - jj
                # print(ii, jj)
                jj -= 1
        return res