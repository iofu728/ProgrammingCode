# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2024-06-02 12:04:07
# @Last Modified by:   gunjianpan
# @Last Modified time: 2024-06-02 12:04:18

"""
100307. 候诊室中的最少椅子数 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Easy
给你一个字符串 s，模拟每秒钟的事件 i：

如果 s[i] == 'E'，表示有一位顾客进入候诊室并占用一把椅子。
如果 s[i] == 'L'，表示有一位顾客离开候诊室，从而释放一把椅子。
返回保证每位进入候诊室的顾客都能有椅子坐的 最少 椅子数，假设候诊室最初是 空的 。

 

示例 1：

输入：s = "EEEEEEE"

输出：7

解释：

每秒后都有一个顾客进入候诊室，没有人离开。因此，至少需要 7 把椅子。

示例 2：

输入：s = "ELELEEL"

输出：2

解释：

假设候诊室里有 2 把椅子。下表显示了每秒钟等候室的状态。

秒	事件	候诊室的人数	可用的椅子数
0	Enter	1	1
1	Leave	0	2
2	Enter	1	1
3	Leave	0	2
4	Enter	1	1
5	Enter	2	0
6	Leave	1	1
示例 3：

输入：s = "ELEELEELLL"

输出：3

解释：

假设候诊室里有 3 把椅子。下表显示了每秒钟等候室的状态。

秒	事件	候诊室的人数	可用的椅子数
0	Enter	1	2
1	Leave	0	3
2	Enter	1	2
3	Enter	2	1
4	Leave	1	2
5	Enter	2	1
6	Enter	3	0
7	Leave	2	1
8	Leave	1	2
9	Leave	0	3
 

提示：

1 <= s.length <= 50
s 仅由字母 'E' 和 'L' 组成。
s 表示一个有效的进出序列。
"""
class Solution:
    def minimumChairs(self, s: str) -> int:
        res, now = 0, 0
        for ii in s:
            if ii == "E":
                now -= 1
            else:
                now += 1
            res = max(res, -now)
        return res