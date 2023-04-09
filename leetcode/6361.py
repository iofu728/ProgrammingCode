# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2023-04-09 12:11:58
# @Last Modified by:   gunjianpan
# @Last Modified time: 2023-04-09 12:12:00

n=4*10**6 + 1
num_list = [True]*n
num_list[0], num_list[1] = False, False

for i in range(2, int(pow(n, 0.5)) + 1):
    if num_list[i]:  # 如果i为质数(不是任何质数的倍数)
        num_list[i * i::i] = [False] * ((n - i * i - 1) // i + 1)  # 因为要包含i*i所以需要+1；因为n不在列表里，所以需要-1

class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        res = 0
        N, M = len(nums), len(nums[0])
        for ii in range(N):
            x = nums[ii][ii]
            if num_list[x] is True:
                res = max(res, x)
            y = nums[ii][N - ii - 1]
            if num_list[y] is True:
                res = max(res, y)
        return res