# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2021-11-28 11:31:16
# @Last Modified by:   gunjianpan
# @Last Modified time: 2021-11-28 11:31:28

"""
5939. 半径为 k 的子数组平均值 显示英文描述 
User Accepted:0
User Tried:0
Total Accepted:0
Total Submissions:0
Difficulty:Medium
给你一个下标从 0 开始的数组 nums ，数组中有 n 个整数，另给你一个整数 k 。

半径为 k 的子数组平均值 是指：nums 中一个以下标 i 为 中心 且 半径 为 k 的子数组中所有元素的平均值，即下标在 i - k 和 i + k 范围（含 i - k 和 i + k）内所有元素的平均值。如果在下标 i 前或后不足 k 个元素，那么 半径为 k 的子数组平均值 是 -1 。

构建并返回一个长度为 n 的数组 avgs ，其中 avgs[i] 是以下标 i 为中心的子数组的 半径为 k 的子数组平均值 。

x 个元素的 平均值 是 x 个元素相加之和除以 x ，此时使用截断式 整数除法 ，即需要去掉结果的小数部分。

例如，四个元素 2、3、1 和 5 的平均值是 (2 + 3 + 1 + 5) / 4 = 11 / 4 = 3.75，截断后得到 3 。
 

示例 1：



输入：nums = [7,4,3,9,1,8,5,2,6], k = 3
输出：[-1,-1,-1,5,4,4,-1,-1,-1]
解释：
- avg[0]、avg[1] 和 avg[2] 是 -1 ，因为在这几个下标前的元素数量都不足 k 个。
- 中心为下标 3 且半径为 3 的子数组的元素总和是：7 + 4 + 3 + 9 + 1 + 8 + 5 = 37 。
  使用截断式 整数除法，avg[3] = 37 / 7 = 5 。
- 中心为下标 4 的子数组，avg[4] = (4 + 3 + 9 + 1 + 8 + 5 + 2) / 7 = 4 。
- 中心为下标 5 的子数组，avg[5] = (3 + 9 + 1 + 8 + 5 + 2 + 6) / 7 = 4 。
- avg[6]、avg[7] 和 avg[8] 是 -1 ，因为在这几个下标后的元素数量都不足 k 个。
示例 2：

输入：nums = [100000], k = 0
输出：[100000]
解释：
- 中心为下标 0 且半径 0 的子数组的元素总和是：100000 。
  avg[0] = 100000 / 1 = 100000 。
示例 3：

输入：nums = [8], k = 100000
输出：[-1]
解释：
- avg[0] 是 -1 ，因为在下标 0 前后的元素数量均不足 k 。
 

提示：

n == nums.length
1 <= n <= 105
0 <= nums[i], k <= 105
"""
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        N = len(nums)
        M = 2 * k + 1
        if N <= 2 * k:
            return [-1] * N
        pre = sum(nums[0:2 * k + 1])
        # print(pre, nums[0:2 * k + 1])
        res = [-1] * k
        res.append(pre // M)
        for ii in range(k + 1, N - k):
            pre -= nums[ii - k - 1]
            pre += nums[ii + k]
            res.append(pre // M)
        res.extend([-1] * k)
        return res
            
        