'''
6266. 使用质因数之和替换后可以取到的最小值 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Medium
给你一个正整数 n 。

请你将 n 的值替换为 n 的 质因数 之和，重复这一过程。

注意，如果 n 能够被某个质因数多次整除，则在求和时，应当包含这个质因数同样次数。
返回 n 可以取到的最小值。

 

示例 1：

输入：n = 15
输出：5
解释：最开始，n = 15 。
15 = 3 * 5 ，所以 n 替换为 3 + 5 = 8 。
8 = 2 * 2 * 2 ，所以 n 替换为 2 + 2 + 2 = 6 。
6 = 2 * 3 ，所以 n 替换为 2 + 3 = 5 。
5 是 n 可以取到的最小值。
示例 2：

输入：n = 3
输出：3
解释：最开始，n = 3 。
3 是 n 可以取到的最小值。
 

提示：

2 <= n <= 105

'''
class Solution:
    def smallestValue(self, n: int) -> int:
        @lru_cache(None)
        def get_v(n):
            # print(n)
            res = 0
            while n > 1:
                for ii in isPrimes:
                    if n % ii == 0:
                        n //= ii
                        res += ii
            return res
            
        isPrimes = [1] * (n + 1)
        isPrimes[0] = 0
        isPrimes[1] = 0
        res = 0
        for i in range(2, n):
            j = i
            while i * j < n:
                isPrimes[i * j] = 0
                j += 1
        isPrimes = [ii for ii in range(n + 1) if isPrimes[ii]]
        # print(isPrimes)
        pre = n
        while True:
            now = get_v(pre)
            if pre <= now:
                break
            pre = now
        return pre
