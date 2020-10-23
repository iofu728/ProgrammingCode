# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-10-23 22:54:47
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-10-23 22:55:37

"""
1257. 最小公共区域
给你一些区域列表 regions ，每个列表的第一个区域都包含这个列表内所有其他区域。

很自然地，如果区域 X 包含区域 Y ，那么区域 X  比区域 Y 大。

给定两个区域 region1 和 region2 ，找到同时包含这两个区域的 最小 区域。

如果区域列表中 r1 包含 r2 和 r3 ，那么数据保证 r2 不会包含 r3 。

数据同样保证最小公共区域一定存在。

 

示例 1：

输入：
regions = [["Earth","North America","South America"],
["North America","United States","Canada"],
["United States","New York","Boston"],
["Canada","Ontario","Quebec"],
["South America","Brazil"]],
region1 = "Quebec",
region2 = "New York"
输出："North America"
 

提示：

2 <= regions.length <= 10^4
region1 != region2
所有字符串只包含英文字母和空格，且最多只有 20 个字母。
通过次数1,284提交次数2,392
"""


class Solution:
    def findSmallestRegion(
        self, regions: List[List[str]], region1: str, region2: str
    ) -> str:
        N = len(regions)
        have1 = set()
        fathes = {}
        for ii in regions:
            for jj in ii[1:]:
                fathes[jj] = ii[0]
        pre = region1
        while pre in fathes:
            have1.add(pre)
            pre = fathes[pre]
        pre = region2
        # print(have1)
        while pre in fathes:
            if pre in have1:
                return pre
            pre = fathes[pre]
        return pre
