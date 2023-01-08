'''
6279. 数组乘积中的不同质因数数目 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Medium
给你一个正整数数组 nums ，对 nums 所有元素求积之后，找出并返回乘积中 不同质因数 的数目。

注意：

质数 是指大于 1 且仅能被 1 及自身整除的数字。
如果 val2 / val1 是一个整数，则整数 val1 是另一个整数 val2 的一个因数。
 

示例 1：

输入：nums = [2,4,3,7,10,6]
输出：4
解释：
nums 中所有元素的乘积是：2 * 4 * 3 * 7 * 10 * 6 = 10080 = 25 * 32 * 5 * 7 。
共有 4 个不同的质因数，所以返回 4 。
示例 2：

输入：nums = [2,4,8,16]
输出：1
解释：
nums 中所有元素的乘积是：2 * 4 * 8 * 16 = 1024 = 210 。
共有 1 个不同的质因数，所以返回 1 。
 

提示：

1 <= nums.length <= 104
2 <= nums[i] <= 1000
'''
class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        def get_x(x):
            c = defaultdict(int)
            while x > 1:
                for ii in res:
                    if x % ii == 0:
                        c[ii] += 1
                        x //= ii
            return c
        res = [2, 3, 5]
        for ii in range(7, 1001):
            flag = True
            for jj in res:
                if ii % jj == 0:
                    flag = False
                    break
            if flag:
                res.append(ii)
        c = set()
        for ii in nums:
            y = get_x(ii)
            for ii in y:
                c.add(ii)
        # print(c)
        return len(c)
        

class PrimeTable:
    def __init__(self, n:int) -> None:
        self.n = n
        self.primes = []
        self.min_div = [0] * (n+1)
        self.min_div[1] = 1

        mu = [0] * (n+1)
        phi = [0] * (n+1)
        mu[1] = 1
        phi[1] = 1

        for i in range(2, n+1):
            if not self.min_div[i]:
                self.primes.append(i)
                self.min_div[i] = i
                mu[i] = -1
                phi[i] = i-1
            for p in self.primes:
                if i * p > n: break
                self.min_div[i*p] = p
                if i % p == 0:
                    phi[i*p] = phi[i] * p
                    break
                else:
                    mu[i*p] = -mu[i]
                    phi[i*p] = phi[i] * (p - 1)

    def is_prime(self, x:int):
        if x < 2: return False
        if x <= self.n: return self.min_div[x] == x
        for i in range(2, int(math.sqrt(x))+1):
            if x % i == 0: return False
        return True

    def prime_factorization(self, x:int):
        for p in range(2, int(math.sqrt(x))+1):
            if x <= self.n: break
            if x % p == 0:
                cnt = 0
                while x % p == 0: cnt += 1; x //= p
                yield p, cnt
        while (1 < x and x <= self.n):
            p, cnt = self.min_div[x], 0
            while x % p == 0: cnt += 1; x //= p
            yield p, cnt
        if x >= self.n and x > 1:
            yield x, 1

    def get_factors(self, x:int):
        factors = [1]
        for p, b in self.prime_factorization(x):
            n = len(factors)
            for j in range(1, b+1):
                for d in factors[:n]:
                    factors.append(d * (p ** j))
        return factors

pt = PrimeTable(1000)
class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        tmp = set()
        for x in nums:
            for v, d in pt.prime_factorization(x):
                tmp.add(v)
        return len(tmp)