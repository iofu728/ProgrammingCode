# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2021-04-05 15:07:13
# @Last Modified by:   gunjianpan
# @Last Modified time: 2021-04-05 15:35:56

"""
2. 乐团站位
通过的用户数136
尝试过的用户数634
用户总通过次数136
用户总提交次数1073
题目难度Easy
某乐团的演出场地可视作 num * num 的二维矩阵 grid（左上角坐标为 [0,0])，每个位置站有一位成员。乐团共有 9 种乐器，乐器编号为 1~9，每位成员持有 1 个乐器。

为保证声乐混合效果，成员站位规则为：自 grid 左上角开始顺时针螺旋形向内循环以 1，2，...，9 循环重复排列。例如当 num = 5 时，站位如图所示

image.png

请返回位于场地坐标 [Xpos,Ypos] 的成员所持乐器编号。

示例 1：

输入：num = 3, Xpos = 0, Ypos = 2

输出：3

解释：
image.png

示例 2：

输入：num = 4, Xpos = 1, Ypos = 2

输出：5

解释：
image.png

提示：

1 <= num <= 10^9
0 <= Xpos, Ypos < num
"""


class Solution:
    def orchestraLayout(self, num: int, xPos: int, yPos: int) -> int:
        cx = cy = (num - 1) / 2
        layer_num = int(cx - max(abs(xPos - cx), abs(yPos - cy)))
        if layer_num:
            pre = 2 * ((num - 1 + num - (layer_num - 1) * 2 - 1)) * (layer_num)
            pre %= 9
        else:
            pre = 0
        # for ii in range(layer_num):
        #     pre += (num - ii * 2 - 1) * 4
        lt1 = layer_num
        rd2 = num - 1 - layer_num
        if xPos == yPos == cx:
            pre += 1
        elif xPos == layer_num:
            pre += yPos - lt1 + 1
        else:
            pre += rd2 - lt1 + 1
            if yPos == rd2:
                pre += xPos - lt1
            else:
                pre += rd2 - lt1
                if xPos == rd2:
                    pre += rd2 - yPos
                else:
                    pre += (rd2 - lt1) + (rd2 - xPos)
        pre = pre % 9
        return pre if pre else 9