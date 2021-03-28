'''
5713. 字符串中不同整数的数目 显示英文描述 
通过的用户数1326
尝试过的用户数2018
用户总通过次数1328
用户总提交次数3615
题目难度Easy
给你一个字符串 word ，该字符串由数字和小写英文字母组成。

请你用空格替换每个不是数字的字符。例如，"a123bc34d8ef34" 将会变成 " 123  34 8  34" 。注意，剩下的这些整数间至少要用一个空格隔开："123"、"34"、"8" 和 "34" 。

返回对 word 完成替换后形成的 不同 整数的数目。

如果两个整数的 不含前导零 的十进制表示不同，则认为这两个整数也不同。

 

示例 1：

输入：word = "a123bc34d8ef34"
输出：3
解释：不同的整数有 "123"、"34" 和 "8" 。注意，"34" 只计数一次。
示例 2：

输入：word = "leet1234code234"
输出：2
示例 3：

输入：word = "a1b01c001"
输出：1
解释："1"、"01" 和 "001" 视为同一个整数的十进制表示，因为在比较十进制值时会忽略前导零的存在。
 

提示：

1 <= word.length <= 1000
word 由数字和小写英文字母组成
'''

class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        num_set = set()
        num = 0
        is_num = False
        for ii in word:
            if ii.isdigit():
                if is_num is False:
                    num = 0
                    is_num = True
                num *= 10
                num += int(ii)
            else:
                if is_num is True:
                    num_set.add(num)
                is_num = False
        if is_num is True:
            num_set.add(num)
        return len(num_set)
            