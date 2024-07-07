# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2024-07-07 11:49:43
# @Last Modified by:   gunjianpan
# @Last Modified time: 2024-07-07 11:49:54

"""
100350. Construct String with Minimum Cost 显示英文描述 
通过的用户数71
尝试过的用户数249
用户总通过次数87
用户总提交次数514
题目难度Hard
You are given a string target, an array of strings words, and an integer array costs, both arrays of the same length.

Imagine an empty string s.

You can perform the following operation any number of times (including zero):

Choose an index i in the range [0, words.length - 1].
Append words[i] to s.
The cost of operation is costs[i].
Return the minimum cost to make s equal to target. If it's not possible, return -1.

 

Example 1:

Input: target = "abcdef", words = ["abdef","abc","d","def","ef"], costs = [100,1,1,10,5]

Output: 7

Explanation:

The minimum cost can be achieved by performing the following operations:

Select index 1 and append "abc" to s at a cost of 1, resulting in s = "abc".
Select index 2 and append "d" to s at a cost of 1, resulting in s = "abcd".
Select index 4 and append "ef" to s at a cost of 5, resulting in s = "abcdef".
Example 2:

Input: target = "aaaa", words = ["z","zz","zzz"], costs = [1,10,100]

Output: -1

Explanation:

It is impossible to make s equal to target, so we return -1.

 

Constraints:

1 <= target.length <= 5 * 104
1 <= words.length == costs.length <= 5 * 104
1 <= words[i].length <= target.length
The total sum of words[i].length is less than or equal to 5 * 104.
target and words[i] consist only of lowercase English letters.
1 <= costs[i] <= 104
"""
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
        self.cost = float('inf')

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, cost):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.end = True
        node.cost = min(node.cost, cost)


class Solution:
    def minimumCost(self, target: str, words: List[str], costs: List[int]) -> int:
        trie = Trie()
        n = len(target)

        # Build Trie
        for word, cost in zip(words, costs):
            trie.insert(word, cost)

        # DP array
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        # Active nodes list
        for i in range(n):
            if dp[i] == float('inf'):
                continue
            active_nodes = [(trie.root, i)]  # (current node, start index)
            for j in range(i, n):
                next_active_nodes = []
                for node, start_idx in active_nodes:
                    char = target[j]
                    if char in node.children:
                        next_node = node.children[char]
                        if next_node.end:
                            dp[j + 1] = min(dp[j + 1], dp[start_idx] + next_node.cost)
                        next_active_nodes.append((next_node, start_idx))
                active_nodes = next_active_nodes
                if not active_nodes:
                    break

        return dp[n] if dp[n] != float('inf') else -1


