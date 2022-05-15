"""
6066. 统计区间中的整数数目 显示英文描述 
通过的用户数19
尝试过的用户数39
用户总通过次数19
用户总提交次数50
题目难度Hard
给你区间的 空 集，请你设计并实现满足要求的数据结构：

新增：添加一个区间到这个区间集合中。
统计：计算出现在 至少一个 区间中的整数个数。
实现 CountIntervals 类：

CountIntervals() 使用区间的空集初始化对象
void add(int left, int right) 添加区间 [left, right] 到区间集合之中。
int count() 返回出现在 至少一个 区间中的整数个数。
注意：区间 [left, right] 表示满足 left <= x <= right 的所有整数 x 。

 

示例 1：

输入
["CountIntervals", "add", "add", "count", "add", "count"]
[[], [2, 3], [7, 10], [], [5, 8], []]
输出
[null, null, null, 6, null, 8]

解释
CountIntervals countIntervals = new CountIntervals(); // 用一个区间空集初始化对象
countIntervals.add(2, 3);  // 将 [2, 3] 添加到区间集合中
countIntervals.add(7, 10); // 将 [7, 10] 添加到区间集合中
countIntervals.count();    // 返回 6
                           // 整数 2 和 3 出现在区间 [2, 3] 中
                           // 整数 7、8、9、10 出现在区间 [7, 10] 中
countIntervals.add(5, 8);  // 将 [5, 8] 添加到区间集合中
countIntervals.count();    // 返回 8
                           // 整数 2 和 3 出现在区间 [2, 3] 中
                           // 整数 5 和 6 出现在区间 [5, 8] 中
                           // 整数 7 和 8 出现在区间 [5, 8] 和区间 [7, 10] 中
                           // 整数 9 和 10 出现在区间 [7, 10] 中
 

提示：

1 <= left <= right <= 109
最多调用  add 和 count 方法 总计 105 次
调用 count 方法至少一次
"""
from sortedcontainers import SortedList


class CountIntervals:
    def __init__(self):
        self.x = SortedList()
        self.y = {}
        self.c = 0

    def add(self, left: int, right: int) -> None:
        idx = self.x.bisect_left(left)
        # print(idx, self.x, (len(self.x) == 0 or (len(self.x) and idx == len(self.x) and self.y[self.x[idx - 1]] < left)))
        if not (len(self.x) == 0 or (len(self.x) and idx == len(self.x) and self.y[self.x[idx - 1]] < left)):
            if idx:
                if self.y[self.x[idx - 1]] >= left:
                    idx -= 1
            idx_y = self.x.bisect_right(right)
            xx = left
            y = right
            need = set()
            for ii in range(idx, idx_y):
                x = self.x[ii]
                xx = min(x, xx)
                self.c -= (self.y[x] - x + 1)
                y = max(self.y[x], y)
                need.add(x)
                del self.y[x]
            for ii in need:
                self.x.remove(ii)
            self.x.add(xx)
            self.y[xx] = y
            self.c += (y - xx + 1)
        else:
            self.x.add(left)
            self.y[left] = right
            self.c += (right - left + 1)
        # print(self.x, self.y, self.c)

    def count(self) -> int:
        return self.c


# Your CountIntervals object will be instantiated and called as such:
# obj = CountIntervals()
# obj.add(left,right)
# param_2 = obj.count()
