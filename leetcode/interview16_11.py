# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-07-08 00:40:50
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-07-08 00:41:34

"""
面试题 16.11. 跳水板
你正在使用一堆木板建造跳水板。有两种类型的木板，其中长度较短的木板长度为shorter，长度较长的木板长度为longer。你必须正好使用k块木板。编写一个方法，生成跳水板所有可能的长度。

返回的长度需要从小到大排列。

示例：

输入：
shorter = 1
longer = 2
k = 3
输出： {3,4,5,6}
提示：

0 < shorter <= longer
0 <= k <= 100000
通过次数6,608提交次数16,186
"""


class Solution:
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        num = shorter * k
        res = []
        if k == 0:
            return res
        res.append(num)
        if longer != shorter:
            for ii in range(1, k + 1):
                res.append(num + ii * (longer - shorter))
        return res
