# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2022-04-24 11:32:17
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-04-24 11:32:36

"""
6042. 统计圆内格点数目 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Medium
给你一个二维整数数组 circles ，其中 circles[i] = [xi, yi, ri] 表示网格上圆心为 (xi, yi) 且半径为 ri 的第 i 个圆，返回出现在 至少一个 圆内的 格点数目 。

注意：

格点 是指整数坐标对应的点。
圆周上的点 也被视为出现在圆内的点。
 

示例 1：



输入：circles = [[2,2,1]]
输出：5
解释：
给定的圆如上图所示。
出现在圆内的格点为 (1, 2)、(2, 1)、(2, 2)、(2, 3) 和 (3, 2)，在图中用绿色标识。
像 (1, 1) 和 (1, 3) 这样用红色标识的点，并未出现在圆内。
因此，出现在至少一个圆内的格点数目是 5 。
示例 2：



输入：circles = [[2,2,2],[3,4,1]]
输出：16
解释：
给定的圆如上图所示。
共有 16 个格点出现在至少一个圆内。
其中部分点的坐标是 (0, 2)、(2, 0)、(2, 4)、(3, 2) 和 (4, 4) 。
 

提示：

1 <= circles.length <= 200
circles[i].length == 3
1 <= xi, yi <= 100
1 <= ri <= min(xi, yi)
"""
class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        @lru_cache(None)
        def get_h(x, xx, r):
            return (r ** 2 - (x - xx) ** 2) ** 0.5
        
        res = set([])
        for x, y, r in circles:
            for xx in range(x - r, x + r + 1):
                h = get_h(x, xx, r)
                for yy in range(y - int(h), y + int(h) + 1):
                    res.add((xx, yy))
        return len(res)
