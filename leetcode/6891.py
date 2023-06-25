# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2023-06-25 11:11:34
# @Last Modified by:   gunjianpan
# @Last Modified time: 2023-06-25 11:11:47

"""
6891. 机器人碰撞 显示英文描述 
通过的用户数41
尝试过的用户数49
用户总通过次数41
用户总提交次数72
题目难度Hard
现有 n 个机器人，编号从 1 开始，每个机器人包含在路线上的位置、健康度和移动方向。

给你下标从 0 开始的两个整数数组 positions、healths 和一个字符串 directions（directions[i] 为 'L' 表示 向左 或 'R' 表示 向右）。 positions 中的所有整数 互不相同 。

所有机器人以 相同速度 同时 沿给定方向在路线上移动。如果两个机器人移动到相同位置，则会发生 碰撞 。

如果两个机器人发生碰撞，则将 健康度较低 的机器人从路线中 移除 ，并且另一个机器人的健康度 减少 1 。幸存下来的机器人将会继续沿着与之前 相同 的方向前进。如果两个机器人的健康度相同，则将二者都从路线中移除。

请你确定全部碰撞后幸存下的所有机器人的 健康度 ，并按照原来机器人编号的顺序排列。即机器人 1 （如果幸存）的最终健康度，机器人 2 （如果幸存）的最终健康度等。 如果不存在幸存的机器人，则返回空数组。

在不再发生任何碰撞后，请你以数组形式，返回所有剩余机器人的健康度（按机器人输入中的编号顺序）。

注意：位置  positions 可能是乱序的。

 

示例 1：



输入：positions = [5,4,3,2,1], healths = [2,17,9,15,10], directions = "RRRRR"
输出：[2,17,9,15,10]
解释：在本例中不存在碰撞，因为所有机器人向同一方向移动。所以，从第一个机器人开始依序返回健康度，[2, 17, 9, 15, 10] 。
示例 2：



输入：positions = [3,5,2,6], healths = [10,10,15,12], directions = "RLRL"
输出：[14]
解释：本例中发生 2 次碰撞。首先，机器人 1 和机器人 2 将会碰撞，因为二者健康度相同，二者都将被从路线中移除。接下来，机器人 3 和机器人 4 将会发生碰撞，由于机器人 4 的健康度更小，则它会被移除，而机器人 3 的健康度变为 15 - 1 = 14 。仅剩机器人 3 ，所以返回 [14] 。
示例 3：



输入：positions = [1,2,5,6], healths = [10,10,11,11], directions = "RLRL"
输出：[]
解释：机器人 1 和机器人 2 将会碰撞，因为二者健康度相同，二者都将被从路线中移除。机器人 3 和机器人 4 将会碰撞，因为二者健康度相同，二者都将被从路线中移除。所以返回空数组 [] 。
 

提示：

1 <= positions.length == healths.length == directions.length == n <= 105
1 <= positions[i], healths[i] <= 109
directions[i] == 'L' 或 directions[i] == 'R'
positions 中的所有值互不相同
"""
class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        N = len(positions)
        now = []
        for ii in sorted(list(range(N)), key=lambda i:positions[i]):
            x = directions[ii]
            y = healths[ii]
            if x == "L":
                while now and now[-1][0] == "R" and y:
                    p = now.pop()
                    if healths[p[1]] < y:
                        y -= 1
                        healths[p[1]] = 0
                    elif healths[p[1]] == y:
                        y = 0
                        healths[p[1]] = 0
                        break
                    else:
                        healths[p[1]] -= 1
                        now.append(p)
                        y = 0
                        break
                if y != 0:
                    now.append([x, ii])
                healths[ii] = y
            else:
                now.append([x, ii])
        return [healths[ii] for ii in range(N) if healths[ii]]
                        
        