# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2024-08-11 11:31:54
# @Last Modified by:   gunjianpan
# @Last Modified time: 2024-08-11 11:32:15

"""
100393. 矩阵中的蛇 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Easy
大小为 n x n 的矩阵 grid 中有一条蛇。蛇可以朝 四个可能的方向 移动。矩阵中的每个单元格都使用位置进行标识： grid[i][j] = (i * n) + j。

蛇从单元格 0 开始，并遵循一系列命令移动。

给你一个整数 n 表示 grid 的大小，另给你一个字符串数组 commands，其中包括 "UP"、"RIGHT"、"DOWN" 和 "LEFT"。题目测评数据保证蛇在整个移动过程中将始终位于 grid 边界内。

返回执行 commands 后蛇所停留的最终单元格的位置。

 

示例 1：

输入：n = 2, commands = ["RIGHT","DOWN"]

输出：3

解释：

0	1
2	3
0	1
2	3
0	1
2	3
示例 2：

输入：n = 3, commands = ["DOWN","RIGHT","UP"]

输出：1

解释：

0	1	2
3	4	5
6	7	8
0	1	2
3	4	5
6	7	8
0	1	2
3	4	5
6	7	8
0	1	2
3	4	5
6	7	8
 

提示：

2 <= n <= 10
1 <= commands.length <= 100
commands 仅由 "UP"、"RIGHT"、"DOWN" 和 "LEFT" 组成。
生成的测评数据确保蛇不会移动到矩阵的边界外。
"""
class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        i, j = 0, 0
        c_map = {"UP": [-1, 0], "RIGHT": [0, 1], "DOWN": [1, 0], "LEFT": [0, -1]}
        for ii in commands:
            dx, dy = c_map[ii]
            i = i + dx
            j = j + dy
        return i * n + j
            