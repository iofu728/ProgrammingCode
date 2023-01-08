'''
6278. 统计能整除数字的位数 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Easy
给你一个整数 num ，返回 num 中能整除 num 的数位的数目。

如果满足 nums % val == 0 ，则认为整数 val 可以整除 nums 。

 

示例 1：

输入：num = 7
输出：1
解释：7 被自己整除，因此答案是 1 。
示例 2：

输入：num = 121
输出：2
解释：121 可以被 1 整除，但无法被 2 整除。由于 1 出现两次，所以返回 2 。
示例 3：

输入：num = 1248
输出：4
解释：1248 可以被它每一位上的数字整除，因此答案是 4 。
 

提示：

1 <= num <= 109
num 的数位中不含 0
'''
class Solution:
    def countDigits(self, num: int) -> int:
        res = 0
        for ii in str(num):
            ii = int(ii)
            if ii and num % ii == 0:
                res += 1
        return res