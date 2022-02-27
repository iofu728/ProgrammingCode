class Solution:
    MOD = 10 ** 9 + 7

    def numberOfGoodSubsets(self, nums: List[int]) -> int:
        c = Counter(nums)
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        N, M = len(c), len(primes)
        dp = [0] * (1 << M)
        dp[0] = pow(2, c[1], self.MOD)
        for ii, jj in c.items():
            if ii == 1:
                continue
            subset, check = 0, True
            for idx, p in enumerate(primes):
                if ii % (p * p) == 0:
                    check = False
                    break
                if ii % p == 0:
                    subset |= 1 << idx
            if not check:
                continue
            for mask in range((1 << M) - 1, 0, -1):
                if (mask & subset) == subset:
                    dp[mask] = (dp[mask] + dp[mask ^ subset] * jj) % self.MOD
        return sum(dp[1:]) % self.MOD
