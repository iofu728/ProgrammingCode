"""
5715. 还原排列的最少操作步数 显示英文描述 
通过的用户数150
尝试过的用户数184
用户总通过次数151
用户总提交次数195
题目难度Medium
给你一个偶数 n​​​​​​ ，已知存在一个长度为 n 的排列 perm ，其中 perm[i] == i​（下标 从 0 开始 计数）。

一步操作中，你将创建一个新数组 arr ，对于每个 i ：

如果 i % 2 == 0 ，那么 arr[i] = perm[i / 2]
如果 i % 2 == 1 ，那么 arr[i] = perm[n / 2 + (i - 1) / 2]
然后将 arr​​ 赋值​​给 perm 。

要想使 perm 回到排列初始值，至少需要执行多少步操作？返回最小的 非零 操作步数。

 

示例 1：

输入：n = 2
输出：1
解释：最初，perm = [0,1]
第 1 步操作后，perm = [0,1]
所以，仅需执行 1 步操作
示例 2：

输入：n = 4
输出：2
解释：最初，perm = [0,1,2,3]
第 1 步操作后，perm = [0,2,1,3]
第 2 步操作后，perm = [0,1,2,3]
所以，仅需执行 2 步操作
示例 3：

输入：n = 6
输出：4
 

提示：

2 <= n <= 1000
n​​​​​​ 是一个偶数
"""


class Solution:
    def reinitializePermutation(self, n: int) -> int:
        root = list(range(n))

        def do(array):
            res = []
            for ii in range(n // 2):
                res.append(array[ii * 2])
            for ii in range(n // 2):
                res.append(array[ii * 2 + 1])
            return res

        idx = 1
        tmp = do(root)
        while tmp != root:
            tmp = do(tmp)
            idx += 1
        return idx