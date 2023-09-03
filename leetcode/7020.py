# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2023-09-03 12:08:00
# @Last Modified by:   gunjianpan
# @Last Modified time: 2023-09-03 12:08:17

"""
7020. 统计对称整数的数目 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Easy
给你两个正整数 low 和 high 。

对于一个由 2 * n 位数字组成的整数 x ，如果其前 n 位数字之和与后 n 位数字之和相等，则认为这个数字是一个对称整数。

返回在 [low, high] 范围内的 对称整数的数目 。

 

示例 1：

输入：low = 1, high = 100
输出：9
解释：在 1 到 100 范围内共有 9 个对称整数：11、22、33、44、55、66、77、88 和 99 。
示例 2：

输入：low = 1200, high = 1230
输出：4
解释：在 1200 到 1230 范围内共有 4 个对称整数：1203、1212、1221 和 1230 。
 

提示：

1 <= low <= high <= 104
"""
class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        def check(x):
            s = str(x)
            if len(s) % 2 != 0:
                return False
            n = len(s)
            return sum(int(s[ii]) for ii in range(0, n // 2)) == sum(int(s[ii]) for ii in range(n // 2, n))
        return len([1 for ii in range(low, high + 1) if check(ii)])