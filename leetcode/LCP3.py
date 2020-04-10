# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-04-04 12:26:25
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-04-04 12:27:09

"""
LCP 3. 机器人大冒险
力扣团队买了一个可编程机器人，机器人初始位置在原点(0, 0)。小伙伴事先给机器人输入一串指令command，机器人就会无限循环这条指令的步骤进行移动。指令有两种：

U: 向y轴正方向移动一格
R: 向x轴正方向移动一格。
不幸的是，在 xy 平面上还有一些障碍物，他们的坐标用obstacles表示。机器人一旦碰到障碍物就会被损毁。

给定终点坐标(x, y)，返回机器人能否完好地到达终点。如果能，返回true；否则返回false。

## 示例 1：
输入：command = "URR", obstacles = [], x = 3, y = 2
输出：true
解释：U(0, 1) -> R(1, 1) -> R(2, 1) -> U(2, 2) -> R(3, 2)。

## 示例 2：
输入：command = "URR", obstacles = [[2, 2]], x = 3, y = 2
输出：false
解释：机器人在到达终点前会碰到(2, 2)的障碍物。

## 示例 3：
输入：command = "URR", obstacles = [[4, 2]], x = 3, y = 2
输出：true
解释：到达终点后，再碰到障碍物也不影响返回结果。
 

## 限制：
2 <= command的长度 <= 1000
command由U，R构成，且至少有一个U，至少有一个R
0 <= x <= 1e9, 0 <= y <= 1e9
0 <= obstacles的长度 <= 1000
obstacles[i]不为原点或者终点

通过次数5,118提交次数26,810
"""


class Solution:
    COMMAND_MAPS = {"U": [0, 1], "R": [1, 0]}

    def robot(self, command: str, obstacles: List[List[int]], x: int, y: int) -> bool:
        one_step, dx, dy = [], 0, 0
        for ii in command:
            dx, dy = dx + self.COMMAND_MAPS[ii][0], dy + self.COMMAND_MAPS[ii][1]
            one_step.append([dx, dy])

        def can_get(tx: int, ty: int) -> bool:
            xx, yy = one_step[-1]
            if not xx and not yy:
                return False
            if (
                (not xx or tx % xx == 0)
                and (not yy or ty % yy == 0)
                and ((not xx or not yy) or tx // xx == ty // yy)
            ):
                return True
            integer = int(tx // xx) if xx else int(ty // yy)
            nowx, nowy = integer * xx, integer * yy
            for dx, dy in one_step[:-1]:
                if dx + nowx == tx and dy + nowy == ty:
                    return True
            return False

        if not can_get(x, y):
            return False
        for tx, ty in obstacles:
            if tx > x or ty > y:
                continue
            if can_get(tx, ty):
                print(tx, ty, one_step)
                return False
        return True
