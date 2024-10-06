# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2024-09-22 11:09:15
# @Last Modified by:   gunjianpan
# @Last Modified time: 2024-09-22 11:09:23

"""
100428. 统计重新排列后包含另一个字符串的子字符串数目 I 显示英文描述 
通过的用户数21
尝试过的用户数30
用户总通过次数23
用户总提交次数40
题目难度Medium
给你两个字符串 word1 和 word2 。

如果一个字符串 x 重新排列后，word2 是重排字符串的 前缀 ，那么我们称字符串 x 是 合法的 。

请你返回 word1 中 合法 子字符串 的数目。

 

示例 1：

输入：word1 = "bcca", word2 = "abc"

输出：1

解释：

唯一合法的子字符串是 "bcca" ，可以重新排列得到 "abcc" ，"abc" 是它的前缀。

示例 2：

输入：word1 = "abcabc", word2 = "abc"

输出：10

解释：

除了长度为 1 和 2 的所有子字符串都是合法的。

示例 3：

输入：word1 = "abcabc", word2 = "aaabc"

输出：0

 

解释：

1 <= word1.length <= 105
1 <= word2.length <= 104
word1 和 word2 都只包含小写英文字母。
"""
class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
#         def is_ok(a, b):
#             for i, j in b.items():
#                 if a[i] < j:
#                     return False
#             return True
#         c = Counter(word2)
#         N = len(word1)
#         res = 0
#         for l in range(N):
#             now = defaultdict(int)
#             now[word1[l]] += 1
#             if is_ok(now, c):
#                 res += (N - l)
#                 # print(l, N - l)
#                 continue
#             for r in range(l + 1, N):
#                 now[word1[r]] += 1
#                 if is_ok(now, c):
#                     res += (N - r) 
#                     break
#         return res
    
        # Initialize frequency arrays for 'a' to 'z'
        required = [0] * 26
        for c in word2:
            required[ord(c) - 97] +=1

        required_count = 0
        for cnt in required:
            if cnt >0:
                required_count +=1

        window_count = [0] * 26
        formed =0
        left =0
        result =0
        n = len(word1)

        for right in range(n):
            c = word1[right]
            idx = ord(c) - 97
            if required[idx] >0:
                window_count[idx] +=1
                if window_count[idx] == required[idx]:
                    formed +=1

            while left <= right and formed == required_count:
                # All substrings starting at left to the end are valid
                result += n - right

                c_left = word1[left]
                idx_left = ord(c_left) -97
                if required[idx_left] >0:
                    window_count[idx_left] -=1
                    if window_count[idx_left] < required[idx_left]:
                        formed -=1
                left +=1

        return result

                
                