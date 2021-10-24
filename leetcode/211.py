# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2021-10-19 22:19:16
# @Last Modified by:   gunjianpan
# @Last Modified time: 2021-10-19 22:19:48

"""
211. Design Add and Search Words Data Structure
Medium

3563

148

Add to List

Share
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
 

Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
 

Constraints:

1 <= word.length <= 500
word in addWord consists lower-case English letters.
word in search consist of  '.' or lower-case English letters.
At most 50000 calls will be made to addWord and search.
Accepted
325,303
Submissions
767,518
"""


class WordDictionary:
    def __init__(self):
        Trie = lambda: collections.defaultdict(Trie)
        self.trie = Trie()
        self.END = True

    def addWord(self, word: str) -> None:
        trie = self.trie
        for ii in word:
            trie = trie[ii]
        trie[self.END] = word

    def search(self, word: str) -> bool:
        def dfs(x, idx):
            if idx == len(word):
                if self.END in x:
                    self.res = True
                return
            if self.res:
                return
            if word[idx] in x:
                dfs(x[word[idx]], idx + 1)
            if "." == word[idx]:
                for k, v in x.items():
                    if k not in [self.END]:
                        dfs(v, idx + 1)

        self.res = False
        dfs(self.trie, 0)
        return self.res


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)