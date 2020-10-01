# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-10-01 17:09:15
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-10-01 17:09:37

"""
面试题 16.22. 兰顿蚂蚁
一只蚂蚁坐在由白色和黑色方格构成的无限网格上。开始时，网格全白，蚂蚁面向右侧。每行走一步，蚂蚁执行以下操作。

(1) 如果在白色方格上，则翻转方格的颜色，向右(顺时针)转 90 度，并向前移动一个单位。
(2) 如果在黑色方格上，则翻转方格的颜色，向左(逆时针方向)转 90 度，并向前移动一个单位。

编写程序来模拟蚂蚁执行的前 K 个动作，并返回最终的网格。

网格由数组表示，每个元素是一个字符串，代表网格中的一行，黑色方格由 'X' 表示，白色方格由 '_' 表示，蚂蚁所在的位置由 'L', 'U', 'R', 'D' 表示，分别表示蚂蚁 左、上、右、下 的朝向。只需要返回能够包含蚂蚁走过的所有方格的最小矩形。

示例 1:

输入: 0
输出: ["R"]
示例 2:

输入: 2
输出:
[
  "_X",
  "LX"
]
示例 3:

输入: 5
输出:
[
  "_U",
  "X_",
  "XX"
]
说明：

K <= 100000
通过次数1,197提交次数2,092
"""


class Solution:
    DIRS = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    DIRS_STR = "LURD"

    def printKMoves(self, K: int) -> List[str]:
        if K == 0:
            return ["R"]
        now, far_p, far_n, now_d = (0, 1), (0, 1), (0, 1), 2
        black = set()
        while K > 0:
            if now not in black:
                black.add(now)
                now_d = (now_d + 1) % 4
            else:
                black.remove(now)
                now_d = (now_d + 3) % 4
            d = self.DIRS[now_d]
            now = (now[0] + d[0], now[1] + d[1])
            far_p, far_n = (
                (max(far_p[0], now[0]), max(far_p[1], now[1])),
                (min(far_n[0], now[0]), min(far_n[1], now[1])),
            )
            # print(K, now, black, far_p, far_n)
            K -= 1
        res = []
        for ii in range(far_n[0], far_p[0] + 1):
            tmp = ""
            for jj in range(far_n[1], far_p[1] + 1):
                if (ii, jj) == now:
                    tmp += self.DIRS_STR[now_d]
                elif (ii, jj) in black:
                    tmp += "X"
                else:
                    tmp += "_"
            res.append(tmp)
        return res

