# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-06-20 12:56:47
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-06-20 12:57:27

"""
212. Word Search II Hard
Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

Example:

Input: 
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]

Output: ["eat","oath"]

Note:

All inputs are consist of lowercase letters a-z.
The values of words are distinct.
Accepted 191,556 Submissions 574,674
"""

class Solution:
    SEP = "$"
    CLS = "#"
    DIR = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        N, M = len(board), len(board[0])
        trie = {}
        for word in words:
            node = trie
            for char in word:
                node = node.setdefault(char, {})
            node[self.SEP] = word
        res = []

        def backward(x: int, y: int, pre):
            char = board[x][y]
            node = pre[char]
            word = node.pop(self.SEP, False)
            if word:
                res.append(word)

            board[x][y] = self.CLS
            for dx, dy in self.DIR:
                xx, yy = x + dx, y + dy
                if xx < 0 or xx >= N or yy < 0 or yy >= M:
                    continue
                if not board[xx][yy] in node:
                    continue
                backward(xx, yy, node)
            board[x][y] = char
            if not node:
                pre.pop(char)

        for x in range(N):
            for y in range(M):
                if board[x][y] in trie:
                    backward(x, y, trie)
        return res
