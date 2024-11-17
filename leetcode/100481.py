# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2024-11-17 12:37:32
# @Last Modified by:   gunjianpan
# @Last Modified time: 2024-11-17 12:37:42

"""
100481. 零数组变换 I 显示英文描述 
通过的用户数4
尝试过的用户数7
用户总通过次数4
用户总提交次数7
题目难度Medium
给定一个长度为 n 的整数数组 nums 和一个二维数组 queries，其中 queries[i] = [li, ri]。

对于每个查询 queries[i]：

在 nums 的下标范围 [li, ri] 内选择一个下标子集。
将选中的每个下标对应的元素值减 1。
零数组 是指所有元素都等于 0 的数组。

如果在按顺序处理所有查询后，可以将 nums 转换为 零数组 ，则返回 true，否则返回 false。

数组的 子集 是对数组元素的选择（可能为空）。

 

示例 1：

输入： nums = [1,0,1], queries = [[0,2]]

输出： true

解释：

对于 i = 0：
选择下标子集 [0, 2] 并将这些下标处的值减 1。
数组将变为 [0, 0, 0]，这是一个零数组。
示例 2：

输入： nums = [4,3,2,1], queries = [[1,3],[0,2]]

输出： false

解释：

对于 i = 0： 
选择下标子集 [1, 2, 3] 并将这些下标处的值减 1。
数组将变为 [4, 2, 1, 0]。
对于 i = 1：
选择下标子集 [0, 1, 2] 并将这些下标处的值减 1。
数组将变为 [3, 1, 0, 0]，这不是一个零数组。
 

提示：

1 <= nums.length <= 105
0 <= nums[i] <= 105
1 <= queries.length <= 105
queries[i].length == 2
0 <= li <= ri < nums.length

"""
class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        new = []
        now = 0
        dp = {}
        for i, j in queries:
            dp[i] = dp.get(i, 0) + 1
            dp[j + 1] = dp.get(j + 1, 0) - 1
        last = 0
        for i, j in sorted(dp.items(), key=lambda i:(i[0])):
            for ii in range(last, i):
                # print(ii, now, nums[ii])
                if nums[ii] > now:
                    print()
                    return False
            last = i
            now += j
        for ii in range(last, len(nums)):
            # print(ii, now, nums[ii])
            if nums[ii] > now:
                return False
        return True
            
            
        
        
        