# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-25 22:22:59
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-25 23:26:10

"""
336. Palindrome Pairs Hard
Given a list of unique words, return all the pairs of the distinct indices (i, j) in the given list, so that the concatenation of the two words words[i] + words[j] is a palindrome.

 

Example 1:

Input: words = ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]]
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
Example 2:

Input: words = ["bat","tab","cat"]
Output: [[0,1],[1,0]]
Explanation: The palindromes are ["battab","tabbat"]
Example 3:

Input: words = ["a",""]
Output: [[0,1],[1,0]]
 

Constraints:

1 <= words.length <= 5000
0 <= words[i] <= 300
words[i] consists of lower-case English letters.
Accepted 103,859 Submissions 305,958
"""


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        N = len(words)
        res = []
        word2id = {w: idx for idx, w in enumerate(words)}
        for ii, w in enumerate(words):
            for jj in range(len(w) + 1):
                pre, last = w[:jj], w[jj:]
                if (
                    pre[::-1] in word2id
                    and word2id[pre[::-1]] != ii
                    and last == last[::-1]
                ):
                    res.append([ii, word2id[pre[::-1]]])
                if (
                    jj
                    and last[::-1] in word2id
                    and word2id[last[::-1]] != ii
                    and pre == pre[::-1]
                ):
                    res.append([word2id[last[::-1]], ii])
        return res


# class Solution:
#     def palindromePairs(self, words: List[str]) -> List[List[int]]:
#         def test(tree, w, types: int = 0):
#             idx = 0
#             while idx < len(w):
#                 if not w[idx] in tree:
#                     return False
#                 tree = tree[w[idx]]
#                 idx += 1
#             if types:
#                 for k, v in tree.items():
#                     if k != END and END in v:
#                         return w + k
#                 return False
#             return "#" in tree

#         def decoder(s: str):
#             n = len(s)
#             idx = n
#             while idx > 1:
#                 flag = True
#                 for ii in range(idx // 2):
#                     tmp = idx - ii - 1
#                     if s[tmp] != s[ii]:
#                         flag = False
#                         break
#                 print(idx, flag)
#                 if flag is True:
#                     return s[idx:]
#                 idx -= 1
#             return s

#         Trie = lambda: collections.defaultdict(Trie)
#         e_trie = Trie()
#         END = "#"
#         word2id, t2id = {}, {}
#         for idx, w in enumerate(words):
#             word2id[w] = idx
#             tmp = decoder(w[::-1])[::-1]
#             print(tmp)
#             t2id[tmp] = idx
#             reduce(dict.__getitem__, tmp, e_trie)[END] = tmp
#             reduce(dict.__getitem__, w, e_trie)[END] = w

#         res = []
#         for ii, jj in enumerate(words):
#             tmp = jj[::-1]
#             if test(e_trie, tmp):
#                 d = word2id[tmp] if tmp in word2id else t2id[tmp]
#                 if d != ii:
#                     res.append([ii, d])
#             tmp = jj[::-1][:-1]
#             if test(e_trie, tmp) and tmp in word2id:
#                 if ii != word2id[tmp]:
#                     res.append([ii, word2id[tmp]])

#             tmp = decoder(jj)
#             if tmp != jj:
#                 tmp = tmp[::-1]
#                 if test(e_trie, tmp) and tmp in word2id:
#                     if ii != word2id[tmp]:
#                         res.append([ii, word2id[tmp]])
#             tmp = test(e_trie, jj, 1)
#             if tmp is not False:
#                 if tmp != word2id[tmp]:
#                     res.append([ii, word2id[tmp]])
#         return res
