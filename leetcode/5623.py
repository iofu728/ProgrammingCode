# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-12-26 22:43:50
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-12-26 23:56:59

"""
5623. 修改后的最大二进制字符串 显示英文描述 
通过的用户数407
尝试过的用户数644
用户总通过次数412
用户总提交次数1613
题目难度Medium
给你一个二进制字符串 binary ，它仅有 0 或者 1 组成。你可以使用下面的操作任意次对它进行修改：

操作 1 ：如果二进制串包含子字符串 "00" ，你可以用 "10" 将其替换。
比方说， "00010" -> "10010"
操作 2 ：如果二进制串包含子字符串 "10" ，你可以用 "01" 将其替换。
比方说， "00010" -> "00001"
请你返回执行上述操作任意次以后能得到的 最大二进制字符串 。如果二进制字符串 x 对应的十进制数字大于二进制字符串 y 对应的十进制数字，那么我们称二进制字符串 x 大于二进制字符串 y 。

 

示例 1：

输入：binary = "000110"
输出："111011"
解释：一个可行的转换为：
"000110" -> "000101" 
"000101" -> "100101" 
"100101" -> "110101" 
"110101" -> "110011" 
"110011" -> "111011"
示例 2：

输入：binary = "01"
输出："01"
解释："01" 没办法进行任何转换。
 

提示：

1 <= binary.length <= 105
binary 仅包含 '0' 和 '1' 。
"""


class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        N = len(binary)
        zeros = [ii for ii in range(N) if binary[ii] == "0"]
        if len(zeros) == 0:
            return binary
        if len(zeros) == N:
            return "1" * (N - 1) + "0"
        M = len(zeros)
        idx = zeros[0]
        for ii in range(M - 1):
            jj = zeros[ii]
            if zeros[ii + 1] != jj + 1:
                idx = jj + 1
                zeros[ii + 1] = jj + 1
        print(idx)
        return "1" * idx + "0" + "1" * (N - idx - 1)