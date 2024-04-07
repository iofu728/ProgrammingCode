'''
100277. 使数组中位数等于 K 的最少操作数 显示英文描述
通过的用户数3
尝试过的用户数5
用户总通过次数3
用户总提交次数6
题目难度Medium
给你一个整数数组 nums 和一个 非负 整数 k 。

一次操作中，你可以选择任一下标 i ，然后将 nums[i] 加 1 或者减 1 。

请你返回将 nums 中位数 变为 k 所需要的 最少 操作次数。

一个数组的 中位数 指的是数组按 非递减 顺序排序后最中间的元素。如果数组长度为偶数，我们选择中间两个数的较大值为中位数。



示例 1：

输入：nums = [2,5,6,8,5], k = 4

输出：2

解释：我们将 nums[1] 和 nums[4] 减 1 得到 [2, 4, 6, 8, 4] 。现在数组的中位数等于 k 。所以答案为 2 。

示例 2：

输入：nums = [2,5,6,8,5], k = 7

输出：3

解释：我们将 nums[1] 增加 1 两次，并且将 nums[2] 增加 1 一次，得到 [2, 7, 7, 8, 5] 。结果数组的中位数等于 k 。所以答案为 3 。

示例 3：

输入：nums = [1,2,3,4,5,6], k = 4

输出：0

解释：数组中位数已经等于 k 了，所以不需要进行任何操作。



提示：

1 <= nums.length <= 2 * 105
1 <= nums[i] <= 109
1 <= k <= 109
'''
class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        N = len(nums)
        idx = N // 2
        res = 0
        # print(idx)
        nums = sorted(nums)
        if nums[idx] == k:
            return res
        elif nums[idx] > k:
            while idx >= 0:
                # print(idx, nums[idx] - k)
                if nums[idx] >= k:
                    res += nums[idx] - k
                    idx -= 1
                else:
                    break
        else:
            while idx < N:
                if nums[idx] <= k:
                    res += k - nums[idx]
                    idx += 1
                else:
                    break
        return res
