# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2023-10-22 15:47:20
# @Last Modified by:   gunjianpan
# @Last Modified time: 2023-10-22 15:47:32

"""
6920. 得到 K 个半回文串的最少修改次数 显示英文描述 
通过的用户数166
尝试过的用户数322
用户总通过次数200
用户总提交次数853
题目难度Hard
给你一个字符串 s 和一个整数 k ，请你将 s 分成 k 个 子字符串 ，使得每个 子字符串 变成 半回文串 需要修改的字符数目最少。

请你返回一个整数，表示需要修改的 最少 字符数目。

注意：

如果一个字符串从左往右和从右往左读是一样的，那么它是一个 回文串 。
如果长度为 len 的字符串存在一个满足 1 <= d < len 的正整数 d ，len % d == 0 成立且所有对 d 做除法余数相同的下标对应的字符连起来得到的字符串都是 回文串 ，那么我们说这个字符串是 半回文串 。比方说 "aa" ，"aba" ，"adbgad" 和 "abab" 都是 半回文串 ，而 "a" ，"ab" 和 "abca" 不是。
子字符串 指的是一个字符串中一段连续的字符序列。
 

示例 1：

输入：s = "abcac", k = 2
输出：1
解释：我们可以将 s 分成子字符串 "ab" 和 "cac" 。子字符串 "cac" 已经是半回文串。如果我们将 "ab" 变成 "aa" ，它也会变成一个 d = 1 的半回文串。
该方案是将 s 分成 2 个子字符串的前提下，得到 2 个半回文子字符串需要的最少修改次数。所以答案为 1 。
示例 2:

输入：s = "abcdef", k = 2
输出：2
解释：我们可以将 s 分成子字符串 "abc" 和 "def" 。子字符串 "abc" 和 "def" 都需要修改一个字符得到半回文串，所以我们总共需要 2 次字符修改使所有子字符串变成半回文串。
该方案是将 s 分成 2 个子字符串的前提下，得到 2 个半回文子字符串需要的最少修改次数。所以答案为 2 。
示例 3：

输入：s = "aabbaa", k = 3
输出：0
解释：我们可以将 s 分成子字符串 "aa" ，"bb" 和 "aa" 。
字符串 "aa" 和 "bb" 都已经是半回文串了。所以答案为 0 。
 

提示：

2 <= s.length <= 200
1 <= k <= s.length / 2
s 只包含小写英文字母。
"""
class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        @functools.lru_cache(None)
        def getdivs(nn) :
            div = [1]
            while nn % 2 == 0 :
                div.append(div[-1]*2)
                nn = nn // 2
            for pt in range(3, int(nn**0.5)+1, 2) :
                if pt * pt > nn :
                    break
                nt = 0
                while nn % pt == 0 :
                    nn = nn // pt
                    nt += 1
                lent = len(div)
                for i in range(nt) :
                    div += [t*pt for t in div[-lent:]]

            if not nn == 1 :
                div += [t*nn for t in div]
            return div
        
        @functools.lru_cache(None)
        def get_n(ps=0, pe=len(s)) :
            len_t = pe - ps
            div_n = getdivs(len_t)
            to_ret = 1e99
            for it in div_n :
                if it == len_t :
                    continue
                rett = 0
                for i in range(it) :
                    temp_str = s[ps+i:pe:it]
                    # print(ps, pe, it, i, temp_str)
                    for i in range(len(temp_str)//2) :
                        if not temp_str[i] == temp_str[-1-i] :
                            rett += 1
                to_ret = min(to_ret, rett)
            return to_ret
                  
        @functools.lru_cache(None)
        def solve(pt = 0, kt = k) :
            if pt == len(s) and kt == 0 :
                return 0
            if pt == len(s) or kt == 0 :
                return 1e99
            to_ret = 1e99
            for next_pt in range(pt+1, len(s)+1) :
                to_ret = min(to_ret, get_n(pt, next_pt)+solve(next_pt, kt-1))
            return to_ret
        
        return solve()
            