# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2022-03-20 13:53:41
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-03-20 13:54:02

"""
6029. 射箭比赛中的最大得分 显示英文描述 
通过的用户数34
尝试过的用户数43
用户总通过次数34
用户总提交次数51
题目难度Medium
Alice 和 Bob 是一场射箭比赛中的对手。比赛规则如下：

Alice 先射 numArrows 支箭，然后 Bob 也射 numArrows 支箭。
分数按下述规则计算：
箭靶有若干整数计分区域，范围从 0 到 11 （含 0 和 11）。
箭靶上每个区域都对应一个得分 k（范围是 0 到 11），Alice 和 Bob 分别在得分 k 区域射中 ak 和 bk 支箭。如果 ak >= bk ，那么 Alice 得 k 分。如果 ak < bk ，则 Bob 得 k 分
如果 ak == bk == 0 ，那么无人得到 k 分。
例如，Alice 和 Bob 都向计分为 11 的区域射 2 支箭，那么 Alice 得 11 分。如果 Alice 向计分为 11 的区域射 0 支箭，但 Bob 向同一个区域射 2 支箭，那么 Bob 得 11 分。

给你整数 numArrows 和一个长度为 12 的整数数组 aliceArrows ，该数组表示 Alice 射中 0 到 11 每个计分区域的箭数量。现在，Bob 想要尽可能 最大化 他所能获得的总分。

返回数组 bobArrows ，该数组表示 Bob 射中 0 到 11 每个 计分区域的箭数量。且 bobArrows 的总和应当等于 numArrows 。

如果存在多种方法都可以使 Bob 获得最大总分，返回其中 任意一种 即可。

 

示例 1：



输入：numArrows = 9, aliceArrows = [1,1,0,1,0,0,2,1,0,1,2,0]
输出：[0,0,0,0,1,1,0,0,1,2,3,1]
解释：上表显示了比赛得分情况。
Bob 获得总分 4 + 5 + 8 + 9 + 10 + 11 = 47 。
可以证明 Bob 无法获得比 47 更高的分数。
示例 2：



输入：numArrows = 3, aliceArrows = [0,0,1,0,0,0,0,0,0,0,0,2]
输出：[0,0,0,0,0,0,0,0,1,1,1,0]
解释：上表显示了比赛得分情况。
Bob 获得总分 8 + 9 + 10 = 27 。
可以证明 Bob 无法获得比 27 更高的分数。
 

提示：

1 <= numArrows <= 105
aliceArrows.length == bobArrows.length == 12
0 <= aliceArrows[i], bobArrows[i] <= numArrows
sum(aliceArrows[i]) == numArrows
"""


class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        def dp(n, idx):
            if n <= 0 or idx < 0:
                return 0, [0] * 12
            res, b = dp(n, idx - 1)
            if n > aliceArrows[idx]:
                y, bb = dp(n - aliceArrows[idx] - 1, idx - 1)
                y += idx
                bb[idx] = aliceArrows[idx] + 1
                if y > res:
                    b = bb
                    res = y
            return res, b

        a, b = dp(numArrows, len(aliceArrows) - 1)
        b[0] += numArrows - sum(b)
        return b
