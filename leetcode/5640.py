# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-12-27 11:53:37
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-12-27 12:32:27

"""
5640. 与数组中元素的最大异或值 显示英文描述 
通过的用户数169
尝试过的用户数466
用户总通过次数184
用户总提交次数853
题目难度Hard
给你一个由非负整数组成的数组 nums 。另有一个查询数组 queries ，其中 queries[i] = [xi, mi] 。

第 i 个查询的答案是 xi 和任何 nums 数组中不超过 mi 的元素按位异或（XOR）得到的最大值。换句话说，答案是 max(nums[j] XOR xi) ，其中所有 j 均满足 nums[j] <= mi 。如果 nums 中的所有元素都大于 mi，最终答案就是 -1 。

返回一个整数数组 answer 作为查询的答案，其中 answer.length == queries.length 且 answer[i] 是第 i 个查询的答案。

 

示例 1：

输入：nums = [0,1,2,3,4], queries = [[3,1],[1,3],[5,6]]
输出：[3,3,7]
解释：
1) 0 和 1 是仅有的两个不超过 1 的整数。0 XOR 3 = 3 而 1 XOR 3 = 2 。二者中的更大值是 3 。
2) 1 XOR 2 = 3.
3) 5 XOR 2 = 7.
示例 2：

输入：nums = [5,2,4,6,6,3], queries = [[12,4],[8,1],[6,3]]
输出：[15,-1,5]
 

提示：

1 <= nums.length, queries.length <= 105
queries[i].length == 2
0 <= nums[j], xi, mi <= 109
"""


class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        def insert(val):
            t = trie
            for i in range(63, -1, -1):
                if (val & (1 << i)) > 0:
                    if 1 not in t:
                        t[1] = {}
                    t = t[1]
                else:
                    if 0 not in t:
                        t[0] = {}
                    t = t[0]
            t[2] = True

        def find(val):
            t = trie
            x = 0
            for i in range(63, -1, -1):
                if (val & (1 << i)) > 0:
                    if 0 in t:
                        x |= 1 << i
                        t = t[0]
                    elif 1 in t:
                        t = t[1]
                    else:
                        return -1
                else:
                    if 1 in t:
                        x |= 1 << i
                        t = t[1]
                    elif 0 in t:
                        t = t[0]
                    else:
                        return -1
            return x

        trie = {}
        nums.sort()
        queries = sorted([(y, ii, x) for ii, (x, y) in enumerate(queries)])
        N, M = len(queries), len(nums)
        ans = [-1] * N

        jj = 0
        for y, ii, x in queries:
            while jj < M and nums[jj] <= y:
                insert(nums[jj])
                jj += 1
            ans[ii] = find(x)

        return ans