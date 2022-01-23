# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2022-01-18 19:46:16
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-01-18 19:46:31

"""
605. 种花问题
假设有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花不能种植在相邻的地块上，它们会争夺水源，两者都会死去。

给你一个整数数组  flowerbed 表示花坛，由若干 0 和 1 组成，其中 0 表示没种植花，1 表示种植了花。另有一个数 n ，能否在不打破种植规则的情况下种入 n 朵花？能则返回 true ，不能则返回 false。

 

示例 1：

输入：flowerbed = [1,0,0,0,1], n = 1
输出：true
示例 2：

输入：flowerbed = [1,0,0,0,1], n = 2
输出：false
 

提示：

1 <= flowerbed.length <= 2 * 104
flowerbed[i] 为 0 或 1
flowerbed 中不存在相邻的两朵花
0 <= n <= flowerbed.length
通过次数118,899提交次数358,077
"""
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        res = n
        N = len(flowerbed)
        if flowerbed[0] == 0 and (N == 1 or flowerbed[1] == 0):
            flowerbed[0] = 1
            res -= 1
        if flowerbed[-1] == 0 and flowerbed[-2] == 0:
            flowerbed[-1] = 1
            res -= 1
        for ii in range(1, N - 1):
            if flowerbed[ii] == 0 and flowerbed[ii - 1] == 0 and flowerbed[ii + 1] == 0 and res > 0:
                flowerbed[ii] = 1
                res -= 1
                if res == 0:
                    return True
        return res <= 0
        