'''
6280. 范围内最接近的两个质数 显示英文描述 
通过的用户数327
尝试过的用户数404
用户总通过次数345
用户总提交次数619
题目难度Medium
给你两个正整数 left 和 right ，请你找到两个整数 num1 和 num2 ，它们满足：

left <= nums1 < nums2 <= right  。
nums1 和 nums2 都是 质数 。
nums2 - nums1 是满足上述条件的质数对中的 最小值 。
请你返回正整数数组 ans = [nums1, nums2] 。如果有多个整数对满足上述条件，请你返回 nums1 最小的质数对。如果不存在符合题意的质数对，请你返回 [-1, -1] 。

如果一个整数大于 1 ，且只能被 1 和它自己整除，那么它是一个质数。

 

示例 1：

输入：left = 10, right = 19
输出：[11,13]
解释：10 到 19 之间的质数为 11 ，13 ，17 和 19 。
质数对的最小差值是 2 ，[11,13] 和 [17,19] 都可以得到最小差值。
由于 11 比 17 小，我们返回第一个质数对。
示例 2：

输入：left = 4, right = 6
输出：[-1,-1]
解释：给定范围内只有一个质数，所以题目条件无法被满足。
 

提示：

1 <= left <= right <= 106
'''
class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        if right <= 2:
            return [-1, -1]
        
        n = right + 1
        res = [True] * (n)

        for i in range(3, int(n ** 0.5) + 1, 2):
            res[i * i::2 * i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
        res =  [i for i in range(3, n, 2) if res[i] and left <= i]
        if 2 >= left:
            res = [2] + res
        if len(res) < 2:
            return [-1, -1]
        ans = float("inf")
        q = None
        # print(res)
        for ii in range(1, len(res)):
            a, b = res[ii - 1], res[ii]
            if b - a < ans:
                ans = b - a
                q = [a, b]
        return q

def euler_flag_prime(n):
    # 欧拉线性筛素数
    # 说明：返回小于等于 n 的所有素数
    flag = [False for _ in range(n + 1)]
    prime_numbers = []
    for num in range(2, n + 1):
        if not flag[num]:
            prime_numbers.append(num)
        for prime in prime_numbers:
            if num * prime > n:
                break
            flag[num * prime] = True
            if num % prime == 0:  # 这句是最有意思的地方  下面解释
                break
    return prime_numbers


class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        primes = euler_flag_prime(right)
        primes = [x for x in primes if x>=left]
        ans = []
        m = len(primes)
        for i in range(m-1):
            x,y = primes[i], primes[i+1]
            if not ans or y-x<ans[1]-ans[0]:
                ans = [x,y]
        return ans if ans else [-1, -1]