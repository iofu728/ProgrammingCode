"""
6017. 向数组中追加 K 个整数 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Medium
给你一个整数数组 nums 和一个整数 k 。请你向 nums 中追加 k 个 未 出现在 nums 中的、互不相同 的 正 整数，并使结果数组的元素和 最小 。

返回追加到 nums 中的 k 个整数之和。

 

示例 1：

输入：nums = [1,4,25,10,25], k = 2
输出：5
解释：在该解法中，向数组中追加的两个互不相同且未出现的正整数是 2 和 3 。
nums 最终元素和为 1 + 4 + 25 + 10 + 25 + 2 + 3 = 70 ，这是所有情况中的最小值。
所以追加到数组中的两个整数之和是 2 + 3 = 5 ，所以返回 5 。
示例 2：

输入：nums = [5,6], k = 6
输出：25
解释：在该解法中，向数组中追加的两个互不相同且未出现的正整数是 1 、2 、3 、4 、7 和 8 。
nums 最终元素和为 5 + 6 + 1 + 2 + 3 + 4 + 7 + 8 = 36 ，这是所有情况中的最小值。
所以追加到数组中的两个整数之和是 1 + 2 + 3 + 4 + 7 + 8 = 25 ，所以返回 25 。
 

提示：

1 <= nums.length <= 105
1 <= nums[i], k <= 109

"""


class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        N = len(nums)
        nums = set(nums)
        res = 0
        for ii in range(1, N + 1):
            if ii not in nums:
                res += ii
                k -= 1
                if k == 0:
                    return res
        # print(k)
        res += (N + 1 + N + k) * k // 2
        l, r = N + 1, N + k
        for ii in sorted(nums):
            if l <= ii <= r:
                res -= ii
                r += 1
                res += r
        return res