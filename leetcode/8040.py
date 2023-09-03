# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2023-09-03 12:08:42
# @Last Modified by:   gunjianpan
# @Last Modified time: 2023-09-03 12:08:57

"""
8040. 生成特殊数字的最少操作 显示英文描述 
通过的用户数70
尝试过的用户数92
用户总通过次数70
用户总提交次数114
题目难度Medium
给你一个下标从 0 开始的字符串 num ，表示一个非负整数。

在一次操作中，您可以选择 num 的任意一位数字并将其删除。请注意，如果你删除 num 中的所有数字，则 num 变为 0。

返回最少需要多少次操作可以使 num 变成特殊数字。

如果整数 x 能被 25 整除，则该整数 x 被认为是特殊数字。

 

 

示例 1：

输入：num = "2245047"
输出：2
解释：删除数字 num[5] 和 num[6] ，得到数字 "22450" ，可以被 25 整除。
可以证明要使数字变成特殊数字，最少需要删除 2 位数字。
示例 2：

输入：num = "2908305"
输出：3
解释：删除 num[3]、num[4] 和 num[6] ，得到数字 "2900" ，可以被 25 整除。
可以证明要使数字变成特殊数字，最少需要删除 3 位数字。
示例 3：

输入：num = "10"
输出：1
解释：删除 num[0] ，得到数字 "0" ，可以被 25 整除。
可以证明要使数字变成特殊数字，最少需要删除 1 位数字。
 

提示

1 <= num.length <= 100
num 仅由数字 '0' 到 '9' 组成
num 不含任何前导零
"""
class Solution:
    def minimumOperations(self, num: str) -> int:
        def get_x(flag):
            res = 0
            if flag == "0":
                idx = n - 1
                while idx >= 0 and num[idx] not in "0":
                    idx -= 1
                    res += 1
                y = idx - 1
                # print(res, idx, y)
                while y >= 0 and not ((num[idx] == "0" and num[y] in "05")):
                    y -= 1
                    res += 1
                if idx < 0 or y < 0 or not ((num[idx] == "0")):
                    res += 1
            else:
                idx = n - 1
                while idx >= 0 and num[idx] not in "5":
                    idx -= 1
                    res += 1
                y = idx - 1
                # print(res, idx, y)
                while y >= 0 and not ( (num[idx] == "5" and num[y] in "27")):
                    y -= 1
                    res += 1
                if idx < 0 or y < 0 or not ((num[idx] == "5" and num[y] in "27")):
                    res += 1
            return res
        n = len(num)
        if n <= 2:
            return 0 if num in ["25", "50", "75"] else (n - 1 if "0" in num else n)

        return min(get_x("0"), get_x("5"), n - num.count("0"))
            
        