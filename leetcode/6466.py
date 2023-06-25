# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2023-06-25 11:10:11
# @Last Modified by:   gunjianpan
# @Last Modified time: 2023-06-25 11:10:25

"""
6466. 美丽下标对的数目 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Easy
给你一个下标从 0 开始的整数数组 nums 。如果下标对 i、j 满足 0 ≤ i < j < nums.length ，如果 nums[i] 的 第一个数字 和 nums[j] 的 最后一个数字 互质 ，则认为 nums[i] 和 nums[j] 是一组 美丽下标对 。

返回 nums 中 美丽下标对 的总数目。

对于两个整数 x 和 y ，如果不存在大于 1 的整数可以整除它们，则认为 x 和 y 互质 。换而言之，如果 gcd(x, y) == 1 ，则认为 x 和 y 互质，其中 gcd(x, y) 是 x 和 k 最大公因数 。

 

示例 1：

输入：nums = [2,5,1,4]
输出：5
解释：nums 中共有 5 组美丽下标对：
i = 0 和 j = 1 ：nums[0] 的第一个数字是 2 ，nums[1] 的最后一个数字是 5 。2 和 5 互质，因此 gcd(2,5) == 1 。
i = 0 和 j = 2 ：nums[0] 的第一个数字是 2 ，nums[1] 的最后一个数字是 1 。2 和 5 互质，因此 gcd(2,1) == 1 。
i = 1 和 j = 2 ：nums[0] 的第一个数字是 5 ，nums[1] 的最后一个数字是 1 。2 和 5 互质，因此 gcd(5,1) == 1 。
i = 1 和 j = 3 ：nums[0] 的第一个数字是 5 ，nums[1] 的最后一个数字是 4 。2 和 5 互质，因此 gcd(5,4) == 1 。
i = 2 和 j = 3 ：nums[0] 的第一个数字是 1 ，nums[1] 的最后一个数字是 4 。2 和 5 互质，因此 gcd(1,4) == 1 。
因此，返回 5 。
示例 2：

输入：nums = [11,21,12]
输出：2
解释：共有 2 组美丽下标对：
i = 0 和 j = 1 ：nums[0] 的第一个数字是 1 ，nums[1] 的最后一个数字是 1 。gcd(1,1) == 1 。
i = 0 和 j = 2 ：nums[0] 的第一个数字是 1 ，nums[1] 的最后一个数字是 2 。gcd(1,2) == 1 。
因此，返回 2 。
 

提示：

2 <= nums.length <= 100
1 <= nums[i] <= 9999
nums[i] % 10 != 0
"""
class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        def gcd(a, b):
            if b != 0:
                return gcd(b, a % b)
            return a
        N = len(nums)
        res = 0
        for ii in range(N):
            x = int(str(nums[ii])[0])
            for jj in range(ii + 1, N):
                y = int(str(nums[jj])[-1])
                if gcd(x, y) == 1:
                    res += 1
        return res