# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2021-07-25 16:45:13
# @Last Modified by:   gunjianpan
# @Last Modified time: 2021-07-25 16:45:26

"""
5824. 子字符串突变后可能得到的最大整数
给你一个字符串 num ，该字符串表示一个大整数。另给你一个长度为 10 且 下标从 0  开始 的整数数组 change ，该数组将 0-9 中的每个数字映射到另一个数字。更规范的说法是，数字 d 映射为数字 change[d] 。

你可以选择 突变  num 的任一子字符串。突变 子字符串意味着将每位数字 num[i] 替换为该数字在 change 中的映射（也就是说，将 num[i] 替换为 change[num[i]]）。

请你找出在对 num 的任一子字符串执行突变操作（也可以不执行）后，可能得到的 最大整数 ，并用字符串表示返回。

子字符串 是字符串中的一个连续序列。

 

示例 1：

输入：num = "132", change = [9,8,5,0,3,6,4,2,6,8]
输出："832"
解释：替换子字符串 "1"：
- 1 映射为 change[1] = 8 。
因此 "132" 变为 "832" 。
"832" 是可以构造的最大整数，所以返回它的字符串表示。
示例 2：

输入：num = "021", change = [9,4,3,5,7,2,1,9,0,6]
输出："934"
解释：替换子字符串 "021"：
- 0 映射为 change[0] = 9 。
- 2 映射为 change[2] = 3 。
- 1 映射为 change[1] = 4 。
因此，"021" 变为 "934" 。
"934" 是可以构造的最大整数，所以返回它的字符串表示。 
示例 3：

输入：num = "5", change = [1,4,7,5,3,2,5,6,9,4]
输出："5"
解释："5" 已经是可以构造的最大整数，所以返回它的字符串表示。
 

提示：

1 <= num.length <= 105
num 仅由数字 0-9 组成
change.length == 10
0 <= change[d] <= 9
通过次数3,357提交次数12,428
"""


class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        bigger = {str(ii): str(jj) for ii, jj in enumerate(change) if ii < jj}
        same = {str(jj): jj for ii, jj in enumerate(change) if ii == jj}
        idx, N = 0, len(num)
        while idx < N:
            if num[idx] in bigger:
                break
            idx += 1
        if idx < N:
            num = num[:idx] + bigger[num[idx]] + num[idx + 1 :]
            while idx + 1 < N and (num[idx + 1] in bigger or num[idx + 1] in same):
                idx += 1
                num = num[:idx] + bigger.get(num[idx], num[idx]) + num[idx + 1 :]
        return num
