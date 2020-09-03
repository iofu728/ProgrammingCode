# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-03 20:52:58
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-03 21:37:13

"""
745. Prefix and Suffix Search Hard
Design a special dictionary which has some words and allows you to search the words in it by a prefix and a suffix.

Implement the WordFilter class:

WordFilter(string[] words) Initializes the object with the words in the dictionary.
f(string prefix, string suffix) Returns the index of the word in the dictionary which has the prefix prefix and the suffix suffix. If there is more than one valid index, return the largest of them. If there is no such word in the dictionary, return -1.
 

Example 1:

Input
["WordFilter", "f"]
[[["apple"]], ["a", "e"]]
Output
[null, 0]

Explanation
WordFilter wordFilter = new WordFilter(["apple"]);
wordFilter.f("a", "e"); // return 0, because the word at index 0 has prefix = "a" and suffix = 'e".
 

Constraints:

1 <= words.length <= 15000
1 <= words[i].length <= 10
1 <= prefix.length, suffix.length <= 10
words[i], prefix and suffix consist of lower-case English letters only.
At most 15000 calls will be made to the function f.
Accepted 19,403 Submissions 56,609
"""
Trie = lambda: collections.defaultdict(Trie)
WEIGHT = False


class WordFilter:
    def __init__(self, words: List[str]):
        self.trie = Trie()
        for idx, word in enumerate(words):
            word += "#"
            for ii in range(len(word)):
                cur = self.trie
                cur[WEIGHT] = idx
                for jj in range(ii, 2 * len(word) - 1):
                    cur = cur[word[jj % len(word)]]
                    cur[WEIGHT] = idx

    def f(self, prefix: str, suffix: str) -> int:
        cur = self.trie
        for ii in suffix + "#" + prefix:
            if ii not in cur:
                return -1
            cur = cur[ii]
        return cur[WEIGHT]
