"""
3591. 检查元素频次是否为质数
已解答
简单
premium lock icon
相关企业
提示
给你一个整数数组 nums。

如果数组中任一元素的 频次 是 质数，返回 true；否则，返回 false。

元素 x 的 频次 是它在数组中出现的次数。

质数是一个大于 1 的自然数，并且只有两个因数：1 和它本身。

 

示例 1：

输入： nums = [1,2,3,4,5,4]

输出： true

解释：

数字 4 的频次是 2，而 2 是质数。

示例 2：

输入： nums = [1,2,3,4,5]

输出： false

解释：

所有元素的频次都是 1。

示例 3：

输入： nums = [2,2,2,4,4]

输出： true

解释：

数字 2 和 4 的频次都是质数。

 

提示：

1 <= nums.length <= 100
0 <= nums[i] <= 100
"""
MX = 200
isprime = [True] * (MX+1)
isprime[0] = isprime[1] = False
primes = []
for num in range(2, MX+1):
    if isprime[num]:
        primes.append(num)
    for p in primes:
        if num * p > MX:
            break
        isprime[num * p] = False
        if num % p == 0:
            break

class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        c = Counter(nums)
        for i, j in c.items():
            if isprime[j] == True:
                return True
        return False
        