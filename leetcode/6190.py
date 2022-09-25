# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2022-09-25 12:18:26
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-09-25 12:18:36

"""
6190. 找到所有好下标 显示英文描述 
通过的用户数1
尝试过的用户数1
用户总通过次数1
用户总提交次数1
题目难度Medium
给你一个大小为 n 下标从 0 开始的整数数组 nums 和一个正整数 k 。

对于 k <= i < n - k 之间的一个下标 i ，如果它满足以下条件，我们就称它为一个 好 下标：

下标 i 之前 的 k 个元素是 非递增的 。
下标 i 之后 的 k 个元素是 非递减的 。
按 升序 返回所有好下标。

 

示例 1：

输入：nums = [2,1,1,1,3,4,1], k = 2
输出：[2,3]
解释：数组中有两个好下标：
- 下标 2 。子数组 [2,1] 是非递增的，子数组 [1,3] 是非递减的。
- 下标 3 。子数组 [1,1] 是非递增的，子数组 [3,4] 是非递减的。
注意，下标 4 不是好下标，因为 [4,1] 不是非递减的。
示例 2：

输入：nums = [2,1,1,2], k = 2
输出：[]
解释：数组中没有好下标。
 

提示：

n == nums.length
3 <= n <= 105
1 <= nums[i] <= 106
1 <= k <= n / 2
"""
class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        N = len(nums)
        a, b = [0] * N, [0] * N
        b[-1] = N - 1
        for ii in range(1, N):
            if nums[ii - 1] >= nums[ii]:
                a[ii] = a[ii - 1]
            else:
                a[ii] = ii
        for ii in range(N - 2, -1, -1):
            if nums[ii + 1] >= nums[ii]:
                b[ii] = b[ii + 1]
            else:
                b[ii] = ii
        # print(a, b)
        res = []
        for ii in range(1, N - 1):
            # print(ii - 1 - a[ii - 1], b[ii + 1] - (ii + 1))
            if ii - 1 - a[ii - 1] + 1 >= k and b[ii + 1] - (ii + 1) + 1 >= k:
                res.append(ii)
        return res