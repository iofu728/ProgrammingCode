# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-08-28 21:40:15
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-08-28 21:40:32

"""
剑指 Offer 59 - II. 队列的最大值
请定义一个队列并实现函数 max_value 得到队列里的最大值，要求函数max_value、push_back 和 pop_front 的均摊时间复杂度都是O(1)。

若队列为空，pop_front 和 max_value 需要返回 -1

示例 1：

输入: 
["MaxQueue","push_back","push_back","max_value","pop_front","max_value"]
[[],[1],[2],[],[],[]]
输出: [null,null,null,2,1,2]
示例 2：

输入: 
["MaxQueue","pop_front","max_value"]
[[],[],[]]
输出: [null,-1,-1]
 

限制：

1 <= push_back,pop_front,max_value的总操作数 <= 10000
1 <= value <= 10^5
通过次数36,892提交次数77,321
"""


class MaxQueue:
    def __init__(self):
        self.queue = []
        self.deque = []

    def max_value(self) -> int:
        if not len(self.deque):
            return -1
        return self.deque[0]

    def push_back(self, value: int) -> None:

        while len(self.deque) and self.deque[-1] < value:
            self.deque.pop(-1)
        self.deque.append(value)
        self.queue.append(value)

    def pop_front(self) -> int:
        if not len(self.deque):
            return -1
        ans = self.queue.pop(0)
        if ans == self.deque[0]:
            self.deque = self.deque[1:]
        return ans


# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()
