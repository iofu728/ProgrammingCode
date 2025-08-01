"""
100578. 中位数之和的最大值
已解答
中等
premium lock icon
相关企业
提示
给你一个整数数组 nums，其长度可以被 3 整除。

你需要通过多次操作将数组清空。在每一步操作中，你可以从数组中选择任意三个元素，计算它们的 中位数 ，并将这三个元素从数组中移除。

奇数长度数组的 中位数 定义为数组按非递减顺序排序后位于中间的元素。

返回通过所有操作得到的 中位数之和的最大值 。

 

示例 1：

输入： nums = [2,1,3,2,1,3]

输出： 5

解释：

第一步，选择下标为 2、4 和 5 的元素，它们的中位数是 3。移除这些元素后，nums 变为 [2, 1, 2]。
第二步，选择下标为 0、1 和 2 的元素，它们的中位数是 2。移除这些元素后，nums 变为空数组。
因此，中位数之和为 3 + 2 = 5。

示例 2：

输入： nums = [1,1,10,10,10,10]

输出： 20

解释：

第一步，选择下标为 0、2 和 3 的元素，它们的中位数是 10。移除这些元素后，nums 变为 [1, 10, 10]。
第二步，选择下标为 0、1 和 2 的元素，它们的中位数是 10。移除这些元素后，nums 变为空数组。
因此，中位数之和为 10 + 10 = 20。

 

提示：

1 <= nums.length <= 5 * 105
nums.length % 3 == 0
1 <= nums[i] <= 109
"""
class Solution:
    def maximumMedianSum(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(nums)
        res = 0
        idx = n - 2
        for ii in range(n // 3):
            res += nums[idx]
            idx -= 2
        return res
        