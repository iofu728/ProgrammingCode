'''
class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        
        res = 0
        N = len(nums)
        for ii in range(N):
            if k % nums[ii] != 0:
                continue
            tmp = nums[ii]
            if tmp == k:
                res += 1
            for jj in range(ii + 1, N):
                if k % nums[jj] != 0:
                    break
                t = math.gcd(tmp, nums[jj])
                tmp = (tmp // t) * (nums[jj] // t) * t
                if tmp == k:
                    # print(ii, jj)
                    res += 1
                elif tmp > k:
                    break
        return res
        
'''
class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        
        res = 0
        N = len(nums)
        for ii in range(N):
            if k % nums[ii] != 0:
                continue
            tmp = nums[ii]
            if tmp == k:
                res += 1
            for jj in range(ii + 1, N):
                if k % nums[jj] != 0:
                    break
                t = math.gcd(tmp, nums[jj])
                tmp = (tmp // t) * (nums[jj] // t) * t
                if tmp == k:
                    # print(ii, jj)
                    res += 1
                elif tmp > k:
                    break
        return res
        