# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2022-08-21 14:06:04
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-08-21 14:06:17

"""
6155. 找出数组的第 K 大和 显示英文描述 
通过的用户数2
尝试过的用户数11
用户总通过次数2
用户总提交次数20
题目难度Hard
给你一个整数数组 nums 和一个 正 整数 k 。你可以选择数组的任一 子序列 并且对其全部元素求和。

数组的 第 k 大和 定义为：可以获得的第 k 个 最大 子序列和（子序列和允许出现重复）

返回数组的 第 k 大和 。

子序列是一个可以由其他数组删除某些或不删除元素排生而来的数组，且派生过程不改变剩余元素的顺序。

注意：空子序列的和视作 0 。

 

示例 1：

输入：nums = [2,4,-2], k = 5
输出：2
解释：所有可能获得的子序列和列出如下，按递减顺序排列：
- 6、4、4、2、2、0、0、-2
数组的第 5 大和是 2 。
示例 2：

输入：nums = [1,-2,3,4,-10,12], k = 16
输出：10
解释：数组的第 16 大和是 10 。
 

提示：

n == nums.length
1 <= n <= 105
-109 <= nums[i] <= 109
1 <= k <= min(2000, 2n)
"""
class Solution:
    def kSum(self, nums: List[int], kk: int) -> int:
        a, b, c = sorted([ii for ii in nums if ii > 0]), [0 for jj in nums if jj == 0], sorted([jj for jj in nums if jj < 0], reverse=True)
        kkk = min(kk + 20, 2000)
        def get_max(m, k):
            res = []
            q = [(0, -1)]
            while len(res) < kkk and q:
                x, y = heapq.heappop(q)
                res.append(k - x)
                if y + 1 < len(m):
                    heapq.heappush(q, (x + m[y + 1], y + 1))
                    if y > -1:
                        heapq.heappush(q, (x - m[y] + m[y + 1], y + 1))
            return res
        def get_min(m):
            res = []
            q = [(0, -1)]
            while len(res) < kkk and q:
                x, y = heapq.heappop(q)
                res.append(-x)
                if y + 1 < len(m):
                    heapq.heappush(q, (x - m[y + 1], y + 1))
                    if y > -1:
                        heapq.heappush(q, (x + m[y] - m[y + 1], y + 1))
            return res
        a, c = get_max(a, sum(a)), get_min(c)
        
        idx = 0
        q = []
        b = pow(2, len(b))
        # print(a, c, b)
        for ii, jj in enumerate(a):
            heapq.heappush(q, (-jj, ii, 0))
        # print(q)
        while q:
            x, y, z = heapq.heappop(q)
            idx += b
            # print(x, y, z, idx)
            if idx >= kk:
                return -x
            if z + 1 < len(c):
                heapq.heappush(q, (x - c[z + 1] + c[z], y, z + 1))
        return 0
        
            
        