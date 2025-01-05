"""
100525. 最长乘积等价子数组 显示英文描述 
通过的用户数60
尝试过的用户数90
用户总通过次数60
用户总提交次数99
题目难度容易
给你一个由 正整数 组成的数组 。nums

如果一个数组 满足 ，则称其为 乘积等价数组 ，其中：arrprod(arr) == lcm(arr) * gcd(arr)

prod(arr) 表示 中所有元素的乘积。arr
gcd(arr) 表示 中所有元素的最大公因数 (GCD)。arr
lcm(arr) 表示 中所有元素的最小公倍数 (LCM)。arr
返回数组 的 最长 乘积等价子数组 的长度。nums

子数组 是数组中连续的、非空的元素序列。

术语 表示 和 的 最大公因数 。gcd(a, b)ab

术语 表示 和 的 最小公倍数 。lcm(a, b)ab

 

示例 1：

输入： nums = [1,2,1,2,1,1,1]

输出： 5

解释： 

最长的乘积等价子数组是 ，其中 ， ，以及 。[1, 2, 1, 1, 1]prod([1, 2, 1, 1, 1]) = 2gcd([1, 2, 1, 1, 1]) = 1lcm([1, 2, 1, 1, 1]) = 2

示例 2：

输入： nums = [2,3,4,5,6]

输出： 3

解释： 

最长的乘积等价子数组是 。[3, 4, 5]

示例 3：

输入： nums = [1,2,3,1,4,5,1]

输出： 5

 

提示：

2 <= nums.length <= 100
1 <= nums[i] <= 10

"""
class Solution:
    def maxLength(self, nums: List[int]) -> int:
        def gcdarr(i, j):
            res = nums[i]
            for ii in range(i + 1, j):
                res = math.gcd(res, nums[ii])
            return res
        def lcmarr(i, j):
            res = nums[i]
            for ii in range(i + 1, j):
                res = math.lcm(res, nums[ii])
            return res
        def prodarr(i, j):
            res = nums[i]
            for ii in range(i + 1, j):
                res = res * nums[ii]
            return res
        N = len(nums)
        for l in range(N, -1, -1):
            for x in range(0, N - l + 1):
                if prodarr(x, x + l) == gcdarr(x, x + l) * lcmarr(x, x + l):
                    return l
        