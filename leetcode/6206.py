# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2022-09-11 12:44:48
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-09-11 12:45:56

"""
6206. 最长递增子序列 II 显示英文描述 
通过的用户数9
尝试过的用户数26
用户总通过次数9
用户总提交次数37
题目难度Hard
给你一个整数数组 nums 和一个整数 k 。

找到 nums 中满足以下要求的最长子序列：

子序列 严格递增
子序列中相邻元素的差值 不超过 k 。
请你返回满足上述要求的 最长子序列 的长度。

子序列 是从一个数组中删除部分元素后，剩余元素不改变顺序得到的数组。

 

示例 1：

输入：nums = [4,2,1,4,3,4,5,8,15], k = 3
输出：5
解释：
满足要求的最长子序列是 [1,3,4,5,8] 。
子序列长度为 5 ，所以我们返回 5 。
注意子序列 [1,3,4,5,8,15] 不满足要求，因为 15 - 8 = 7 大于 3 。
示例 2：

输入：nums = [7,4,5,1,8,12,4,7], k = 5
输出：4
解释：
满足要求的最长子序列是 [4,5,8,12] 。
子序列长度为 4 ，所以我们返回 4 。
示例 3：

输入：nums = [1,5], k = 1
输出：1
解释：
满足要求的最长子序列是 [1] 。
子序列长度为 1 ，所以我们返回 1 。
 

提示：

1 <= nums.length <= 105
1 <= nums[i], k <= 105
"""

# https://github.com/981377660LMT/algorithm-study/blob/master/6_tree/%E7%BA%BF%E6%AE%B5%E6%A0%91/template/%E5%9C%A8%E7%BA%BF-rmq%E7%BA%BF%E6%AE%B5%E6%A0%91%E6%A8%A1%E6%9D%BF.py
class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        tmp = SegmentTree([0] * (10 ** 5 + 1))
        for x in nums:
            note = tmp.query(max(0, x-k), x-1)
            tmp.update(x, note + 1)
        return tmp.query(0, 10 ** 5)
        
class SegmentTree:
    def __init__(self, data, merge=max): 
        '''
        data:传入的数组
        merge:处理的业务逻辑，例如求和/最大值/最小值，lambda表达式
        '''

        self.data = data
        self.n = len(data)
        #  申请4倍data长度的空间来存线段树节点
        self.tree = [None] * (4 * self.n) # 索引i的左孩子索引为2i+1，右孩子为2i+2
        self._merge = merge
        if self.n:
            self._build(0, 0, self.n-1)


    def query(self, ql, qr):
        '''
        返回区间[ql,..,qr]的值
        '''
        return self._query(0, 0, self.n-1, ql, qr)

    def update(self, index, value):
        # 将data数组index位置的值更新为value,然后递归更新线段树中被影响的各节点的值
        self.data[index] = value
        self._update(0, 0, self.n-1, index)

    def _build(self, tree_index, l, r):
        '''
        递归创建线段树
        tree_index : 线段树节点在数组中位置
        l, r : 该节点表示的区间的左,右边界
        '''
        if l == r:
            self.tree[tree_index] = self.data[l]
            return
        mid = (l+r) // 2 # 区间中点,对应左孩子区间结束,右孩子区间开头
        left, right = 2 * tree_index + 1, 2 * tree_index + 2 # tree_index的左右子树索引
        self._build(left, l, mid)
        self._build(right, mid+1, r)
        self.tree[tree_index] = self._merge(self.tree[left], self.tree[right])

    def _query(self, tree_index, l, r, ql, qr):
        '''
        递归查询区间[ql,..,qr]的值
        tree_index : 某个根节点的索引
        l, r : 该节点表示的区间的左右边界
        ql, qr: 待查询区间的左右边界
        '''
        if l == ql and r == qr:
            return self.tree[tree_index]

        mid = (l+r) // 2 # 区间中点,对应左孩子区间结束,右孩子区间开头
        left, right = tree_index * 2 + 1, tree_index * 2 + 2
        if qr <= mid:
            # 查询区间全在左子树
            return self._query(left, l, mid, ql, qr)
        elif ql > mid:
            # 查询区间全在右子树
            return self._query(right, mid+1, r, ql, qr)

        # 查询区间一部分在左子树一部分在右子树
        return self._merge(self._query(left, l, mid, ql, mid), 
                          self._query(right, mid+1, r, mid+1, qr))

    def _update(self, tree_index, l, r, index):
        '''
        tree_index:某个根节点索引
        l, r : 此根节点代表区间的左右边界
        index : 更新的值的索引
        '''
        if l == r == index:
            self.tree[tree_index] = self.data[index]
            return
        mid = (l+r)//2
        left, right = 2 * tree_index + 1, 2 * tree_index + 2
        if index > mid:
            # 要更新的区间在右子树
            self._update(right, mid+1, r, index)
        else:
            # 要更新的区间在左子树index<=mid
            self._update(left, l, mid, index)
        # 里面的小区间变化了，包裹的大区间也要更新
        self.tree[tree_index] = self._merge(self.tree[left], self.tree[right])