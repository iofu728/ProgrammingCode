# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2023-11-26 12:18:31
# @Last Modified by:   gunjianpan
# @Last Modified time: 2023-11-26 12:18:42

"""
100142. 交换得到字典序最小的数组 显示英文描述 
通过的用户数708
尝试过的用户数1451
用户总通过次数718
用户总提交次数3054
题目难度Medium
给你一个下标从 0 开始的 正整数 数组 nums 和一个 正整数 limit 。

在一次操作中，你可以选择任意两个下标 i 和 j，如果 满足 |nums[i] - nums[j]| <= limit ，则交换 nums[i] 和 nums[j] 。

返回执行任意次操作后能得到的 字典序最小的数组 。

如果在数组 a 和数组 b 第一个不同的位置上，数组 a 中的对应字符比数组 b 中的对应字符的字典序更小，则认为数组 a 就比数组 b 字典序更小。例如，数组 [2,10,3] 比数组 [10,2,3] 字典序更小，下标 0 处是两个数组第一个不同的位置，且 2 < 10 。

 

示例 1：

输入：nums = [1,5,3,9,8], limit = 2
输出：[1,3,5,8,9]
解释：执行 2 次操作：
- 交换 nums[1] 和 nums[2] 。数组变为 [1,3,5,9,8] 。
- 交换 nums[3] 和 nums[4] 。数组变为 [1,3,5,8,9] 。
即便执行更多次操作，也无法得到字典序更小的数组。
注意，执行不同的操作也可能会得到相同的结果。
示例 2：

输入：nums = [1,7,6,18,2,1], limit = 3
输出：[1,6,7,18,1,2]
解释：执行 3 次操作：
- 交换 nums[1] 和 nums[2] 。数组变为 [1,6,7,18,2,1] 。
- 交换 nums[0] 和 nums[4] 。数组变为 [2,6,7,18,1,1] 。
- 交换 nums[0] 和 nums[5] 。数组变为 [1,6,7,18,1,2] 。
即便执行更多次操作，也无法得到字典序更小的数组。
示例 3：

输入：nums = [1,7,28,19,10], limit = 3
输出：[1,7,28,19,10]
解释：[1,7,28,19,10] 是字典序最小的数组，因为不管怎么选择下标都无法执行操作。
 

提示：

1 <= nums.length <= 105
1 <= nums[i] <= 109
1 <= limit <= 109
"""
class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        def get_father(r, p):
            q =  r[p]
            while p != r[p]:
                p = r[p]
            while q != p:
                tmp = r[q]
                r[q] = p
                q = tmp
            return p
        N = len(nums)
        ra = list(range(N))
        l, r = 0, 0
        o_nums = nums
        nums = sorted(enumerate(nums), key=lambda i:(i[1], i[0]))
        res = [0] * N
        while l < N:
            now = nums[l][1]
            while r + 1 < N and nums[r + 1][1] - now <= limit:
                r += 1
            a, b = get_father(ra, nums[l][0]), get_father(ra, nums[r][0])
            ra[a] = b
            l += 1
        c = defaultdict(list)
        for ii in range(N):
            c[get_father(ra, ii)].append((ii, o_nums[ii]))
        for k, v in c.items():
            v1 = sorted([ii[0] for ii in v])
            v2 = sorted([ii[1] for ii in v])
            # print(v)
            for x, y in zip(v1, v2):
                res[x] = y
        return res
            
            
            