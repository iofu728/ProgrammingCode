"""
100268. 最长公共后缀查询 显示英文描述 
通过的用户数21
尝试过的用户数29
用户总通过次数21
用户总提交次数42
题目难度Hard
给你两个字符串数组 wordsContainer 和 wordsQuery 。

对于每个 wordsQuery[i] ，你需要从 wordsContainer 中找到一个与 wordsQuery[i] 有 最长公共后缀 的字符串。如果 wordsContainer 中有两个或者更多字符串有最长公共后缀，那么答案为长度 最短 的。如果有超过两个字符串有 相同 最短长度，那么答案为它们在 wordsContainer 中出现 更早 的一个。

请你返回一个整数数组 ans ，其中 ans[i]是 wordsContainer中与 wordsQuery[i] 有 最长公共后缀 字符串的下标。

 

示例 1：

输入：wordsContainer = ["abcd","bcd","xbcd"], wordsQuery = ["cd","bcd","xyz"]

输出：[1,1,1]

解释：

我们分别来看每一个 wordsQuery[i] ：

对于 wordsQuery[0] = "cd" ，wordsContainer 中有最长公共后缀 "cd" 的字符串下标分别为 0 ，1 和 2 。这些字符串中，答案是下标为 1 的字符串，因为它的长度为 3 ，是最短的字符串。
对于 wordsQuery[1] = "bcd" ，wordsContainer 中有最长公共后缀 "bcd" 的字符串下标分别为 0 ，1 和 2 。这些字符串中，答案是下标为 1 的字符串，因为它的长度为 3 ，是最短的字符串。
对于 wordsQuery[2] = "xyz" ，wordsContainer 中没有字符串跟它有公共后缀，所以最长公共后缀为 "" ，下标为 0 ，1 和 2 的字符串都得到这一公共后缀。这些字符串中， 答案是下标为 1 的字符串，因为它的长度为 3 ，是最短的字符串。
示例 2：

输入：wordsContainer = ["abcdefgh","poiuygh","ghghgh"], wordsQuery = ["gh","acbfgh","acbfegh"]

输出：[2,0,2]

解释：

我们分别来看每一个 wordsQuery[i] ：

对于 wordsQuery[0] = "gh" ，wordsContainer 中有最长公共后缀 "gh" 的字符串下标分别为 0 ，1 和 2 。这些字符串中，答案是下标为 2 的字符串，因为它的长度为 6 ，是最短的字符串。
对于 wordsQuery[1] = "acbfgh" ，只有下标为 0 的字符串有最长公共后缀 "fgh" 。所以尽管下标为 2 的字符串是最短的字符串，但答案是 0 。
对于 wordsQuery[2] = "acbfegh" ，wordsContainer 中有最长公共后缀 "gh" 的字符串下标分别为 0 ，1 和 2 。这些字符串中，答案是下标为 2 的字符串，因为它的长度为 6 ，是最短的字符串。
 

提示：

1 <= wordsContainer.length, wordsQuery.length <= 104
1 <= wordsContainer[i].length <= 5 * 103
1 <= wordsQuery[i].length <= 5 * 103
wordsContainer[i] 只包含小写英文字母。
wordsQuery[i] 只包含小写英文字母。
wordsContainer[i].length 的和至多为 5 * 105 。
wordsQuery[i].length 的和至多为 5 * 105 。
"""
Trie = lambda: collections.defaultdict(Trie)
WEIGHT = False

class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        
        self.trie = Trie()
        default = 0
        
        for ii, jj in sorted(enumerate(wordsContainer), key=lambda i:(-len(i[1]), -i[0])):
            trie = self.trie
            for k in range(len(jj) - 1, -1, -1):
                if isinstance(trie[jj[k]], dict):
                    trie[jj[k]] = [ii, trie[jj[k]]]
                else:
                    trie[jj[k]] = [ii, trie[jj[k]][1]]
                trie = trie[jj[k]][1]
            default = ii
            
        res = []
        for word in wordsQuery:
            trie = self.trie
            print(word)
            tmp = default
            for k in range(len(word) - 1, -1, -1):
                trie = trie[word[k]]
                if isinstance(trie, list):
                    tmp = trie[0]
                    trie = trie[1]
                else:
                    break
            res.append(tmp)
                
        return res
