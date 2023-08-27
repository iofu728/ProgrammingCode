# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2023-08-27 14:20:32
# @Last Modified by:   gunjianpan
# @Last Modified time: 2023-08-27 14:20:45

"""
8015. 距离原点最远的点 显示英文描述 
通过的用户数3472
尝试过的用户数3533
用户总通过次数3510
用户总提交次数4559
题目难度Easy
给你一个长度为 n 的字符串 moves ，该字符串仅由字符 'L'、'R' 和 '_' 组成。字符串表示你在一条原点为 0 的数轴上的若干次移动。

你的初始位置就在原点（0），第 i 次移动过程中，你可以根据对应字符选择移动方向：

如果 moves[i] = 'L' 或 moves[i] = '_' ，可以选择向左移动一个单位距离
如果 moves[i] = 'R' 或 moves[i] = '_' ，可以选择向右移动一个单位距离
移动 n 次之后，请你找出可以到达的距离原点 最远 的点，并返回 从原点到这一点的距离 。

 

示例 1：

输入：moves = "L_RL__R"
输出：3
解释：可以到达的距离原点 0 最远的点是 -3 ，移动的序列为 "LLRLLLR" 。
示例 2：

输入：moves = "_R__LL_"
输出：5
解释：可以到达的距离原点 0 最远的点是 -5 ，移动的序列为 "LRLLLLL" 。
示例 3：

输入：moves = "_______"
输出：7
解释：可以到达的距离原点 0 最远的点是 7 ，移动的序列为 "RRRRRRR" 。
 

提示：

1 <= moves.length == n <= 50
moves 仅由字符 'L'、'R' 和 '_' 组成
"""
class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        a, b, c = 0, 0, 0
        res = 0
        for ii in moves:
            if ii == "L":
                a += 1
            elif ii == "R":
                b += 1
            else:
                c += 1
            if b > a:
                now = b - a + c
            else:
                now = a - b + c
            res = now
        return res
                
            