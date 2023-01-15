"""
6293. 统计好子数组的数目 显示英文描述 
通过的用户数876
尝试过的用户数1362
用户总通过次数892
用户总提交次数2127
题目难度Medium
给你一个整数数组 nums 和一个整数 k ，请你返回 nums 中 好 子数组的数目。

一个子数组 arr 如果有 至少 k 对下标 (i, j) 满足 i < j 且 arr[i] == arr[j] ，那么称它是一个 好 子数组。

子数组 是原数组中一段连续 非空 的元素序列。

 

示例 1：

输入：nums = [1,1,1,1,1], k = 10
输出：1
解释：唯一的好子数组是这个数组本身。
示例 2：

输入：nums = [3,1,4,3,2,2,4], k = 2
输出：4
解释：总共有 4 个不同的好子数组：
- [3,1,4,3,2,2] 有 2 对。
- [3,1,4,3,2,2,4] 有 3 对。
- [1,4,3,2,2,4] 有 2 对。
- [4,3,2,2,4] 有 2 对。
 

提示：

1 <= nums.length <= 105
1 <= nums[i], k <= 109
"""
class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        l, r = 0, 0
        now = 0
        c = defaultdict(int)
        res = 0
        while l < len(nums):
            while r < len(nums) and now < k:
                now += c[nums[r]]
                c[nums[r]] += 1
                r += 1
            if now < k:
                break
            res += len(nums) - r + 1
            c[nums[l]] -= 1
            now -= c[nums[l]]
            l += 1
        return res

        
                