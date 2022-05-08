# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2021-04-11 11:06:13
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-05-04 13:22:30
"""
5727. 找出游戏的获胜者 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Medium
共有 n 名小伙伴一起做游戏。小伙伴们围成一圈，按顺时针顺序从 1 到 n 编号。确切地说，从第 i 名小伙伴顺时针移动一位会到达第 (i+1) 名小伙伴的位置，其中 1 <= i < n ，从第 n 名小伙伴顺时针移动一位会回到第 1 名小伙伴的位置。

游戏遵循如下规则：

从第 1 名小伙伴所在位置开始。
沿着顺时针方向数 k 名小伙伴，计数时需要 包含 起始时的那位小伙伴。逐个绕圈进行计数，一些小伙伴可能会被数过不止一次。
你数到的最后一名小伙伴需要离开圈子，并视作输掉游戏。
如果圈子中仍然有不止一名小伙伴，从刚刚输掉的小伙伴的 顺时针下一位 小伙伴 开始，回到步骤 2 继续执行。
否则，圈子中最后一名小伙伴赢得游戏。
给你参与游戏的小伙伴总数 n ，和一个整数 k ，返回游戏的获胜者。

 

示例 1：


输入：n = 5, k = 2
输出：3
解释：游戏运行步骤如下：
1) 从小伙伴 1 开始。
2) 顺时针数 2 名小伙伴，也就是小伙伴 1 和 2 。
3) 小伙伴 2 离开圈子。下一次从小伙伴 3 开始。
4) 顺时针数 2 名小伙伴，也就是小伙伴 3 和 4 。
5) 小伙伴 4 离开圈子。下一次从小伙伴 5 开始。
6) 顺时针数 2 名小伙伴，也就是小伙伴 5 和 1 。
7) 小伙伴 1 离开圈子。下一次从小伙伴 3 开始。
8) 顺时针数 2 名小伙伴，也就是小伙伴 3 和 5 。
9) 小伙伴 5 离开圈子。只剩下小伙伴 3 。所以小伙伴 3 是游戏的获胜者。
示例 2：

输入：n = 6, k = 5
输出：1
解释：小伙伴离开圈子的顺序：5、4、6、2、3 。小伙伴 1 是游戏的获胜者。
 

提示：

1 <= k <= n <= 500
"""


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        now, nex = list(range(1, n + 1)), []
        remove_id = -1
        for ii in range(n - 1):
            next_id = remove_id + k
            # print(next_id, remove_id)
            if next_id >= len(now):
                next_id -= len(now)
                nex.extend(now[remove_id + 1 :])
                next_id %= len(nex)
                # print(nex)
                now, nex = nex, []
                nex.extend(now[:next_id])
            else:
                nex.extend(now[remove_id + 1 : next_id])
            remove_id = next_id
            # print(now, nex, remove_id)
        # tmp_k = k % len(now)
        next_id = remove_id + k
        if next_id >= len(now):
            nex.extend(now[remove_id + 1 :])
            return nex[0]
        return now[next_id]


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        winner = 1
        for i in range(2, n + 1):
            winner = (k + winner - 1) % i + 1
        return winner
