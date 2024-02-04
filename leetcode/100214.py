class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        res = 0
        idx = 0
        for ii in nums:
            idx += ii
            if idx == 0:
                res += 1
        return res

