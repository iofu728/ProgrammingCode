# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2022-04-10 23:53:15
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-04-10 23:53:28

"""
6037. 按奇偶性交换后的最大数字 显示英文描述 
通过的用户数2460
尝试过的用户数3019
用户总通过次数2469
用户总提交次数3809
题目难度Easy
给你一个正整数 num 。你可以交换 num 中 奇偶性 相同的任意两位数字（即，都是奇数或者偶数）。

返回交换 任意 次之后 num 的 最大 可能值。

 

示例 1：

输入：num = 1234
输出：3412
解释：交换数字 3 和数字 1 ，结果得到 3214 。
交换数字 2 和数字 4 ，结果得到 3412 。
注意，可能存在其他交换序列，但是可以证明 3412 是最大可能值。
注意，不能交换数字 4 和数字 1 ，因为它们奇偶性不同。
示例 2：

输入：num = 65875
输出：87655
解释：交换数字 8 和数字 6 ，结果得到 85675 。
交换数字 5 和数字 7 ，结果得到 87655 。
注意，可能存在其他交换序列，但是可以证明 87655 是最大可能值。
 

提示：

1 <= num <= 109
"""
class Solution:
    def largestInteger(self, num: int) -> int:
        num = [int(ii) for ii in str(num)]
        is_odd = [ii >> 1 << 1 == ii for ii in num]
        odd = sorted([ii for ii, jj in zip(num, is_odd) if jj == 1], reverse=True)
        x = sorted([ii for ii, jj in zip(num, is_odd) if jj == 0], reverse=True)
        l, r, idx = 0, 0, 0
        res = [0] * len(num)
        while idx < len(num):
            if is_odd[idx] == 0:
                res[idx] = x[r]
                r += 1
            else:
                res[idx] = odd[l]
                l += 1
            idx += 1
        ans = 0
        for ii in res:
            ans = ans * 10 + ii
        return ans