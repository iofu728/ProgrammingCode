"""
6340. 统计上升四元组 显示英文描述 
通过的用户数1
尝试过的用户数11
用户总通过次数1
用户总提交次数11
题目难度Hard
给你一个长度为 n 下标从 0 开始的整数数组 nums ，它包含 1 到 n 的所有数字，请你返回上升四元组的数目。

如果一个四元组 (i, j, k, l) 满足以下条件，我们称它是上升的：

0 <= i < j < k < l < n 且
nums[i] < nums[k] < nums[j] < nums[l] 。
 

示例 1：

输入：nums = [1,3,2,4,5]
输出：2
解释：
- 当 i = 0 ，j = 1 ，k = 2 且 l = 3 时，有 nums[i] < nums[k] < nums[j] < nums[l] 。
- 当 i = 0 ，j = 1 ，k = 2 且 l = 4 时，有 nums[i] < nums[k] < nums[j] < nums[l] 。
没有其他的四元组，所以我们返回 2 。
示例 2：

输入：nums = [1,2,3,4]
输出：0
解释：只存在一个四元组 i = 0 ，j = 1 ，k = 2 ，l = 3 ，但是 nums[j] < nums[k] ，所以我们返回 0 。
 

提示：

4 <= nums.length <= 4000
1 <= nums[i] <= nums.length
nums 中所有数字 互不相同 ，nums 是一个排列
"""
class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        N = len(nums)
        small = [[]]
        bigger = [[] for _ in range(N)]
        tmp = []
        for jj, ii in enumerate(nums):
            # idx = bisect.bisect_left(tmp, ii)
            # small[jj] = idx
            bisect.insort(tmp, ii)
            small.append(tmp.copy())
        tmp = []
        for jj in range(N - 1, -1, -1):
            # idx = bisect.bisect_left(tmp, -nums[jj])
            # bigger[jj] = idx
            bisect.insort(tmp, -nums[jj])
            bigger[jj] = tmp.copy()
        
        # print(small)
        # print(bigger)
        res = 0
        for ii in range(1, N - 2):
            for jj in range(ii + 1, N - 1):
                if nums[ii] > nums[jj]:
                    idx1 = bisect.bisect_left(small[ii], nums[jj])
                    idx2 = bisect.bisect_left(bigger[jj], -nums[ii])
                    # print(ii, jj, idx1, idx2)
                    res += idx1 * idx2
        return res
        