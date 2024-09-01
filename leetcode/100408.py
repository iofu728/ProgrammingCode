# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2024-09-01 12:47:37
# @Last Modified by:   gunjianpan
# @Last Modified time: 2024-09-01 12:48:25

"""
100408. 查询子数组最大异或值 显示英文描述 
通过的用户数1
尝试过的用户数4
用户总通过次数1
用户总提交次数4
题目难度Hard
给你一个由 n 个整数组成的数组 nums，以及一个大小为 q 的二维整数数组 queries，其中 queries[i] = [li, ri]。

对于每一个查询，你需要找出 nums[li..ri] 中任意 子数组 的 最大异或值。

数组的异或值 需要对数组 a 反复执行以下操作，直到只剩一个元素，剩下的那个元素就是 异或值：

对于除最后一个下标以外的所有下标 i，同时将 a[i] 替换为 a[i] XOR a[i + 1] 。
移除数组的最后一个元素。
返回一个大小为 q 的数组 answer，其中 answer[i] 表示查询 i 的答案。

 

示例 1：

输入： nums = [2,8,4,32,16,1], queries = [[0,2],[1,4],[0,5]]

输出： [12,60,60]

解释：

在第一个查询中，nums[0..2] 的子数组分别是 [2], [8], [4], [2, 8], [8, 4], 和 [2, 8, 4]，它们的异或值分别为 2, 8, 4, 10, 12, 和 6。查询的答案是 12，所有异或值中的最大值。

在第二个查询中，nums[1..4] 的子数组中最大的异或值是子数组 nums[1..4] 的异或值，为 60。

在第三个查询中，nums[0..5] 的子数组中最大的异或值是子数组 nums[1..4] 的异或值，为 60。

示例 2：

输入： nums = [0,7,3,2,8,5,1], queries = [[0,3],[1,5],[2,4],[2,6],[5,6]]

输出： [7,14,11,14,5]

解释：

下标	nums[li..ri]	最大异或值子数组	子数组最大异或值
0	[0, 7, 3, 2]	[7]	7
1	[7, 3, 2, 8, 5]	[7, 3, 2, 8]	14
2	[3, 2, 8]	[3, 2, 8]	11
3	[3, 2, 8, 5, 1]	[2, 8, 5, 1]	14
4	[5, 1]	[5]	5
 

提示：

1 <= n == nums.length <= 2000
0 <= nums[i] <= 231 - 1
1 <= q == queries.length <= 105
queries[i].length == 2
queries[i] = [li, ri]
0 <= li <= ri <= n - 1
"""
class Solution:
    def maximumSubarrayXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        f = [[0] * n for _ in range(n)]
        g = [[0] * n for _ in range(n)]
        for i in range(n-1, -1, -1):
            f[i][i] = g[i][i] = nums[i]
            maxi = nums[i]
            for j in range(i+1, n):
                f[i][j] = f[i][j-1] ^ f[i+1][j]
                maxi = max(maxi, f[i][j])
                g[i][j] = max(g[i+1][j], maxi)
        res = []
        for x,y in queries:
            res.append(g[x][y])
        return res
