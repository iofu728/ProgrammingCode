'''
5630. 删除子数组的最大得分 显示英文描述 
通过的用户数12
尝试过的用户数16
用户总通过次数12
用户总提交次数18
题目难度Medium
给你一个正整数数组 nums ，请你从中删除一个含有 若干不同元素 的子数组。删除子数组的 得分 就是子数组各元素之 和 。

返回 只删除一个 子数组可获得的 最大得分 。

如果数组 b 是数组 a 的一个连续子序列，即如果它等于 a[l],a[l+1],...,a[r] ，那么它就是 a 的一个子数组。

 

示例 1：

输入：nums = [4,2,4,5,6]
输出：17
解释：最优子数组是 [2,4,5,6]
示例 2：

输入：nums = [5,2,1,2,5,2,1,2,5]
输出：8
解释：最优子数组是 [5,2,1] 或 [1,2,5]
 

提示：

1 <= nums.length <= 105
1 <= nums[i] <= 104
'''
from collections import Counter
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left, right = 0, -1
        res, tmp_max = 0, 0
        c = Counter()
        N = len(nums)
        while left <= right + 1 < N:
            while right + 1 < N and c[nums[right + 1]] == 0:
                right += 1
                tmp_max += nums[right]
                c[nums[right]] += 1
            if tmp_max > res:
                res = tmp_max
            
            tmp_max -= nums[left]
            c[nums[left]] -= 1
            left += 1
            # print(left, right)
        return res
        