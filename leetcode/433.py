"""
433. Minimum Genetic Mutation
Medium

884

102

Add to List

Share
A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.

Suppose we need to investigate a mutation from a gene string start to a gene string end where one mutation is defined as one single character changed in the gene string.

For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
There is also a gene bank bank that records all the valid gene mutations. A gene must be in bank to make it a valid gene string.

Given the two gene strings start and end and the gene bank bank, return the minimum number of mutations needed to mutate from start to end. If there is no such a mutation, return -1.

Note that the starting point is assumed to be valid, so it might not be included in the bank.

 

Example 1:

Input: start = "AACCGGTT", end = "AACCGGTA", bank = ["AACCGGTA"]
Output: 1
Example 2:

Input: start = "AACCGGTT", end = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
Output: 2
Example 3:

Input: start = "AAAAACCC", end = "AACCCCCC", bank = ["AAAACCCC","AAACCCCC","AACCCCCC"]
Output: 3
 

Constraints:

start.length == 8
end.length == 8
0 <= bank.length <= 10
bank[i].length == 8
start, end, and bank[i] consist of only the characters ['A', 'C', 'G', 'T'].
Accepted
53,647
Submissions
114,662
"""
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        def is_neighbor(a, b):
            return len([1 for ii, jj in zip(a, b) if ii != jj]) == 1
        g = defaultdict(list)
        N = len(bank)
        idx = -1
        for ii in range(N):
            if bank[ii] == end:
                idx = ii
            for jj in range(ii + 1, N):
                if is_neighbor(bank[ii], bank[jj]):
                    g[ii].append(jj)
                    g[jj].append(ii)
        if idx == -1:
            return -1
        done = set()
        q = deque()
        for ii in range(N):
            if is_neighbor(start, bank[ii]):
                q.append((1, ii))
                done.add(ii)
        while q:
            h, head = q.popleft()
            if head == idx:
                return h
            for ii in g[head]:
                if ii not in done:
                    q.append((h + 1, ii))
                    done.add(ii)
        return -1



