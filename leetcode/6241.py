class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        c = Counter(nums)
        res = 0
        y = list(c.keys())
        N = len(y)
        for ii in range(N):
            for jj in range(ii + 1, N):
                for kk in range(jj + 1, N):
                    res += c[y[ii]] * c[y[jj]] * c[y[kk]]
        return res