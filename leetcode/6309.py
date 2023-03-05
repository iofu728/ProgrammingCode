# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2023-03-05 12:27:09
# @Last Modified by:   gunjianpan
# @Last Modified time: 2023-03-05 12:27:23

"""
6309. 分割数组使乘积互质 显示英文描述 
通过的用户数0
尝试过的用户数11
用户总通过次数0
用户总提交次数14
题目难度Medium
给你一个长度为 n 的整数数组 nums ，下标从 0 开始。

如果在下标 i 处 分割 数组，其中 0 <= i <= n - 2 ，使前 i + 1 个元素的乘积和剩余元素的乘积互质，则认为该分割 有效 。

例如，如果 nums = [2, 3, 3] ，那么在下标 i = 0 处的分割有效，因为 2 和 9 互质，而在下标 i = 1 处的分割无效，因为 6 和 3 不互质。在下标 i = 2 处的分割也无效，因为 i == n - 1 。
返回可以有效分割数组的最小下标 i ，如果不存在有效分割，则返回 -1 。

当且仅当 gcd(val1, val2) == 1 成立时，val1 和 val2 这两个值才是互质的，其中 gcd(val1, val2) 表示 val1 和 val2 的最大公约数。

 

示例 1：



输入：nums = [4,7,8,15,3,5]
输出：2
解释：上表展示了每个下标 i 处的前 i + 1 个元素的乘积、剩余元素的乘积和它们的最大公约数的值。
唯一一个有效分割位于下标 2 。
示例 2：



输入：nums = [4,7,15,8,3,5]
输出：-1
解释：上表展示了每个下标 i 处的前 i + 1 个元素的乘积、剩余元素的乘积和它们的最大公约数的值。
不存在有效分割。
 

提示：

n == nums.length
1 <= n <= 104
1 <= nums[i] <= 106
"""


class Solution:
    def findValidSplit(self, nums: List[int]) -> int:
        def count_primes_py(n):
            """
            求n以内的所有质数个数（纯python代码）
            """
            # 最小的质数是 2
            if n < 2:
                return 0

            isPrime = [1] * n
            isPrime[0] = isPrime[1] = 0  # 0和1不是质数，先排除掉

            # 埃式筛，把不大于根号 n 的所有质数的倍数剔除
            for i in range(2, int(n**0.5) + 1):
                if isPrime[i]:
                    isPrime[i * i : n : i] = [0] * ((n - 1 - i * i) // i + 1)
            return [ii for ii, jj in enumerate(isPrime) if jj == 1]

        @cache
        def split(n):
            res = set()
            for ii in y:
                if n % ii == 0:
                    res.add(ii)
                while n > 1 and n % ii == 0:
                    n //= ii
                if n == 1:
                    break
            if n != 1:
                res.add(n)
            return res

        N, M = len(nums), max(nums)
        y = count_primes_py(1000)
        # print(y)
        c = [split(ii) for ii in nums]
        g = defaultdict(int)
        # print(c)
        # print(3)
        for jj, ii in enumerate(c):
            for k in ii:
                g[k] = jj
        now = c[0]
        idx = 0
        # print(2)
        while idx < N - 1:
            tmp = idx
            for k in now:
                tmp = max(g[k], tmp)
            if tmp == idx:
                return idx
            for ii in range(idx + 1, tmp + 1):
                now = now.union(c[ii])
            idx = tmp
        return -1
