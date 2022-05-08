"""
6058. 统计打字方案数 显示英文描述 
通过的用户数1
尝试过的用户数2
用户总通过次数1
用户总提交次数2
题目难度Medium
Alice 在给 Bob 用手机打字。数字到字母的 对应 如下图所示。



为了 打出 一个字母，Alice 需要 按 对应字母 i 次，i 是该字母在这个按键上所处的位置。

比方说，为了按出字母 's' ，Alice 需要按 '7' 四次。类似的， Alice 需要按 '5' 两次得到字母  'k' 。
注意，数字 '0' 和 '1' 不映射到任何字母，所以 Alice 不 使用它们。
但是，由于传输的错误，Bob 没有收到 Alice 打字的字母信息，反而收到了 按键的字符串信息 。

比方说，Alice 发出的信息为 "bob" ，Bob 将收到字符串 "2266622" 。
给你一个字符串 pressedKeys ，表示 Bob 收到的字符串，请你返回 Alice 总共可能发出多少种文字信息 。

由于答案可能很大，将它对 109 + 7 取余 后返回。

 

示例 1：

输入：pressedKeys = "22233"
输出：8
解释：
Alice 可能发出的文字信息包括：
"aaadd", "abdd", "badd", "cdd", "aaae", "abe", "bae" 和 "ce" 。
由于总共有 8 种可能的信息，所以我们返回 8 。
示例 2：

输入：pressedKeys = "222222222222222222222222222222222222"
输出：82876089
解释：
总共有 2082876103 种 Alice 可能发出的文字信息。
由于我们需要将答案对 109 + 7 取余，所以我们返回 2082876103 % (109 + 7) = 82876089 。
 

提示：

1 <= pressedKeys.length <= 105
pressedKeys 只包含数字 '2' 到 '9' 。
"""

class Solution:
    T = {str(ii): jj for ii, jj in enumerate([0, 0, 3, 3, 3, 3, 3, 4, 3, 4])}
    MODS = 10 ** 9 + 7
    def countTexts(self, pressedKeys: str) -> int:
        # @lru_cache(None)
        def dp(a, b):
            res = {1: 1}
            for ii in range(2, a + 1):
                new = defaultdict(int)
                new[1] += sum(res.values())
                for ii in range(1, b + 1):
                    new[ii] += res.get(ii - 1, 0)
                res = new
            return res
            
            
        c = []
        for ii in pressedKeys:
            if not c or c[-1][0] != ii:
                c.append([ii, 1])
            else:
                c[-1][-1] += 1
        res = 1
        for ii, jj in c:
            res = (res * sum(dp(jj, self.T[ii]).values())) % self.MODS
        return res
        
        