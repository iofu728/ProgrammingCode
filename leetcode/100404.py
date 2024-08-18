# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2024-08-18 12:25:59
# @Last Modified by:   gunjianpan
# @Last Modified time: 2024-08-18 12:26:16

"""
100404. 统计满足 K 约束的子字符串数量 II 显示英文描述 
通过的用户数3
尝试过的用户数21
用户总通过次数3
用户总提交次数25
题目难度Hard
给你一个 二进制 字符串 s 和一个整数 k。

另给你一个二维整数数组 queries ，其中 queries[i] = [li, ri] 。

如果一个 二进制字符串 满足以下任一条件，则认为该字符串满足 k 约束：

字符串中 0 的数量最多为 k。
字符串中 1 的数量最多为 k。
返回一个整数数组 answer ，其中 answer[i] 表示 s[li..ri] 中满足 k 约束 的 子字符串 的数量。

 

示例 1：

输入：s = "0001111", k = 2, queries = [[0,6]]

输出：[26]

解释：

对于查询 [0, 6]， s[0..6] = "0001111" 的所有子字符串中，除 s[0..5] = "000111" 和 s[0..6] = "0001111" 外，其余子字符串都满足 k 约束。

示例 2：

输入：s = "010101", k = 1, queries = [[0,5],[1,4],[2,3]]

输出：[15,9,3]

解释：

s 的所有子字符串中，长度大于 3 的子字符串都不满足 k 约束。

 

提示：

1 <= s.length <= 105
s[i] 是 '0' 或 '1'
1 <= k <= s.length
1 <= queries.length <= 105
queries[i] == [li, ri]
0 <= li <= ri < s.length
所有查询互不相同
"""
import collections

class SegmentTree:
    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0] * (4 * self.n)
        self.lazy = [0] * (4 * self.n)
        self.build(0, 0, self.n - 1, nums)

    def build(self, node, start, end, nums):
        if start == end:
            self.tree[node] = nums[start]
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2
            self.build(left_child, start, mid, nums)
            self.build(right_child, mid + 1, end, nums)
            self.tree[node] = self.tree[left_child] + self.tree[right_child]

    def update_range(self, node, start, end, l, r, val):
        if self.lazy[node] != 0:
            self.tree[node] += (end - start + 1) * self.lazy[node]
            if start != end:
                left_child = 2 * node + 1
                right_child = 2 * node + 2
                self.lazy[left_child] += self.lazy[node]
                self.lazy[right_child] += self.lazy[node]
            self.lazy[node] = 0
        
        if start > end or start > r or end < l:
            return
        
        if start >= l and end <= r:
            self.tree[node] += (end - start + 1) * val
            if start != end:
                left_child = 2 * node + 1
                right_child = 2 * node + 2
                self.lazy[left_child] += val
                self.lazy[right_child] += val
            return
        
        mid = (start + end) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2
        self.update_range(left_child, start, mid, l, r, val)
        self.update_range(right_child, mid + 1, end, l, r, val)
        self.tree[node] = self.tree[left_child] + self.tree[right_child]

    def query_range(self, node, start, end, l, r):
        if self.lazy[node] != 0:
            self.tree[node] += (end - start + 1) * self.lazy[node]
            if start != end:
                left_child = 2 * node + 1
                right_child = 2 * node + 2
                self.lazy[left_child] += self.lazy[node]
                self.lazy[right_child] += self.lazy[node]
            self.lazy[node] = 0
        
        if start > end or start > r or end < l:
            return 0
        
        if start >= l and end <= r:
            return self.tree[node]
        
        mid = (start + end) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2
        left_sum = self.query_range(left_child, start, mid, l, r)
        right_sum = self.query_range(right_child, mid + 1, end, l, r)
        return left_sum + right_sum

    def add(self, p1, p2):
        self.update_range(0, 0, self.n - 1, p1, p2, 1)

    def range_sum(self, p1, p2):
        return self.query_range(0, 0, self.n - 1, p1, p2)

    def to_array(self):
        # 辅助函数，用来递归处理每个节点
        def retrieve_values(node, start, end, arr):
            if start == end:
                # 叶节点，对应具体的数组元素
                arr[start] = self.query_range(0, 0, self.n - 1, start, start)
            else:
                mid = (start + end) // 2
                left_child = 2 * node + 1
                right_child = 2 * node + 2
                # 递归处理左右子树
                retrieve_values(left_child, start, mid, arr)
                retrieve_values(right_child, mid + 1, end, arr)
        
        # 创建一个空数组，大小与初始数组相同
        arr = [0] * self.n
        # 从根节点开始遍历树，获取每个位置的值
        retrieve_values(0, 0, self.n - 1, arr)
        return arr



class Solution:
    def countKConstraintSubstrings(self, s: str, k: int, queries):
        n = len(s)
        s = [int(c) for c in s]
        
        iqs = [[l, r, i] for i, (l, r) in enumerate(queries)]
        iqs = sorted(iqs, key=lambda x : (x[1], x[0]))
        to_ret = [-1] *len(queries)
        sgt = SegmentTree([0]*n)
        
        piqs = 0
        cts = 0
        ct = [0, 0]
        for i, vt in enumerate(s) :
            ct[vt] += 1
            # while ct[vt] > k :
            #     ct[s[cts]] -= 1
            #     cts += 1
            while ct[0] > k and ct[1] > k:
                ct[s[cts]] -= 1
                cts += 1
            
            sgt.add(cts, i) # 闭区间
            # print(sgt.to_array())
            
            while piqs < len(iqs) and iqs[piqs][1] == i :
                # print(iqs[piqs][0], i)
                to_ret[iqs[piqs][2]] = sgt.range_sum(iqs[piqs][0], i) # 闭区间
                piqs += 1
                
        return to_ret
