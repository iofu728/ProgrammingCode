# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2024-06-30 11:52:39
# @Last Modified by:   gunjianpan
# @Last Modified time: 2024-06-30 11:53:02

"""
100340. 三角形的最大高度 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Easy
给你两个整数 red 和 blue，分别表示红色球和蓝色球的数量。你需要使用这些球来组成一个三角形，满足第 1 行有 1 个球，第 2 行有 2 个球，第 3 行有 3 个球，依此类推。

每一行的球必须是 相同 颜色，且相邻行的颜色必须 不同。

返回可以实现的三角形的 最大 高度。

 

示例 1：

输入： red = 2, blue = 4

输出： 3

解释：



上图显示了唯一可能的排列方式。

示例 2：

输入： red = 2, blue = 1

输出： 2

解释：


上图显示了唯一可能的排列方式。

示例 3：

输入： red = 1, blue = 1

输出： 1

示例 4：

输入： red = 10, blue = 1

输出： 2

解释：


上图显示了唯一可能的排列方式。

 

提示：

1 <= red, blue <= 100
"""
class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        res = 0
        for a, b in [(red, blue), (blue, red)]:
            idx = 1
            while True:
                if idx % 2 == 0:
                    if a < idx:
                        break
                    a -= idx

                    res = max(res, idx)
                    idx += 1
                else:
                    if b < idx:
                        break
                    b -= idx

                    res = max(res, idx)
                    idx += 1
        
        return res
            