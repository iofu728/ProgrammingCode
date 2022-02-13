# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2022-02-12 13:43:53
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-02-12 13:44:14

"""
127. 单词接龙
字典 wordList 中从单词 beginWord 和 endWord 的 转换序列 是一个按下述规格形成的序列 beginWord -> s1 -> s2 -> ... -> sk：

每一对相邻的单词只差一个字母。
 对于 1 <= i <= k 时，每个 si 都在 wordList 中。注意， beginWord 不需要在 wordList 中。
sk == endWord
给你两个单词 beginWord 和 endWord 和一个字典 wordList ，返回 从 beginWord 到 endWord 的 最短转换序列 中的 单词数目 。如果不存在这样的转换序列，返回 0 。

 
示例 1：

输入：beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
输出：5
解释：一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog", 返回它的长度 5。
示例 2：

输入：beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
输出：0
解释：endWord "cog" 不在字典中，所以无法进行转换。
 

提示：

1 <= beginWord.length <= 10
endWord.length == beginWord.length
1 <= wordList.length <= 5000
wordList[i].length == beginWord.length
beginWord、endWord 和 wordList[i] 由小写英文字母组成
beginWord != endWord
wordList 中的所有字符串 互不相同
通过次数136,229提交次数288,335
"""


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def is_close(a, b):
            num = 0
            for ii, jj in zip(wordList[a], wordList[b]):
                if ii != jj:
                    num += 1
                    if num > 1:
                        return False
            return num == 1

        res = 0
        if endWord not in wordList:
            return 0
        if beginWord not in wordList:
            wordList.append(beginWord)
        g = defaultdict(list)
        b_id, e_id = wordList.index(beginWord), wordList.index(endWord)
        N = len(wordList)
        M = len(beginWord)
        for ii in range(N):
            for jj in range(M):
                g[wordList[ii][:jj] + "*" + wordList[ii][jj + 1 :]].append(ii)
        queue = [(1, e_id)]
        has = set([e_id])
        while queue:
            h, root = heapq.heappop(queue)
            if root == b_id:
                return h
            if b_id in g[root]:
                return h + 1
            for jj in range(M):
                for ii in g[wordList[root][:jj] + "*" + wordList[root][jj + 1 :]]:
                    if ii not in has:
                        has.add(ii)
                        heapq.heappush(queue, (h + 1, ii))
        return 0
