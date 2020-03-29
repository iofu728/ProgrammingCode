# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-03-28 23:47:40
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-03-29 00:30:53

"""
30. Substring with Concatenation of All Words Hard
You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

## Example 1:
Input:
  s = "barfoothefoobarman",
  words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.

## Example 2:
Input:
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
Output: []

Accepted 164,859 Submissions 663,454
"""
from collections import Counter


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        N, M, T = len(s), len(words), len(words[0])
        if N < M * T:
            return []
        TT = T * M
        result = []
        need_counter = Counter(words)
        # print(N, M, T, TT)
        for idx in range(T):
            before = [s[ii * T + idx : ii * T + T + idx] for ii in range(M)]
            counter = Counter(before)
            # print(before, counter)
            if counter == need_counter:
                result.append(idx)
            for b in range(idx + T, N - TT + 1, T):
                last = s[b - T : b]
                new = s[b + TT - T : b + TT]
                # print(last, new)
                counter[last] -= 1
                counter[new] = counter.get(new, 0) + 1
                if counter[last] == 0:
                    del counter[last]
                if counter == need_counter:
                    result.append(b)
        return result
