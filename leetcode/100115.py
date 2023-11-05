# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2023-11-05 13:38:04
# @Last Modified by:   gunjianpan
# @Last Modified time: 2023-11-05 13:38:16

"""
100115. 找到冠军 I 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Easy
一场比赛中共有 n 支队伍，按从 0 到  n - 1 编号。

给你一个下标从 0 开始、大小为 n * n 的二维布尔矩阵 grid 。对于满足 0 <= i, j <= n - 1 且 i != j 的所有 i, j ：如果 grid[i][j] == 1，那么 i 队比 j 队 强 ；否则，j 队比 i 队 强 。

在这场比赛中，如果不存在某支强于 a 队的队伍，则认为 a 队将会是 冠军 。

返回这场比赛中将会成为冠军的队伍。

 

示例 1：

输入：grid = [[0,1],[0,0]]
输出：0
解释：比赛中有两支队伍。
grid[0][1] == 1 表示 0 队比 1 队强。所以 0 队是冠军。
示例 2：

输入：grid = [[0,0,1],[1,0,1],[0,0,0]]
输出：1
解释：比赛中有三支队伍。
grid[1][0] == 1 表示 1 队比 0 队强。
grid[1][2] == 1 表示 1 队比 2 队强。
所以 1 队是冠军。
 

提示：

n == grid.length
n == grid[i].length
2 <= n <= 100
grid[i][j] 的值为 0 或 1
对于满足 i != j 的所有 i, j ，grid[i][j] != grid[j][i] 均成立
生成的输出满足：如果 a 队比 b 队强，b 队比 c 队强，那么 a 队比 c 队强
"""
class Solution:
    def maxBalancedSubsequenceSum(self, nums: List[int]) -> int:
        to_ret = nums[0]
        values = [[-1e99, 0]]
        for i in range(len(nums)) :
            vt = nums[i] - i
            pt = bisect.bisect(values, [vt+0.1, 0])
            sumt = nums[i]
            if nums[i] >= 0 :
                if pt > 0 :
                    sumt += values[pt-1][1]
                values.insert(pt, [vt, sumt])
                while pt + 1 < len(values) and values[pt+1][1] <=  values[pt][1] :
                    values.pop(pt+1)
            to_ret = max(to_ret, sumt)
            # print(values)
        return to_ret