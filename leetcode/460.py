# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-04-05 23:01:38
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-04-05 23:03:24

"""
460. LFU Cache Hard
Design and implement a data structure for Least Frequently Used (LFU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least frequently used item before inserting a new item. For the purpose of this problem, when there is a tie (i.e., two or more keys that have the same frequency), the least recently used key would be evicted.

Note that the number of times an item is used is the number of calls to the get and put functions for that item since it was inserted. This number is set to zero when the item is removed.

Follow up:
Could you do both operations in O(1) time complexity?

## Example:

LFUCache cache = new LFUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.get(3);       // returns 3.
cache.put(4, 4);    // evicts key 1.
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4

Accepted 64,592 Submissions 197,245
"""
class Node:
    def __init__(self, key: int, value: int, pre=None, nex=None, fre: int = 0):
        self.key = key
        self.value = value
        self.pre = pre
        self.nex = nex
        self.fre = fre

    def insert(self, o):
        o.pre = self
        o.nex = self.nex
        self.nex.pre = o
        self.nex = o

def link_list():
    head = Node(0, 0)
    tail = Node(0, 0)
    head.nex = tail
    tail.pre = head
    return (head, tail)

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.minFre = 0
        self.freMap = collections.defaultdict(link_list)
        self.keyMap = {}
    
    def increase(self, node: Node):
        node.fre += 1
        self.delete(node)
        self.freMap[node.fre][-1].pre.insert(node)
        if node.fre == 1:
            self.minFre = 1
        elif node.fre - 1 == self.minFre:
            h, t = self.freMap[node.fre - 1]
            if h.nex is t:
                self.minFre = node.fre

    def delete(self, node: Node):
        if node.pre:
            node.pre.nex = node.nex
            node.nex.pre = node.pre
            h, t = self.freMap[node.fre]
            if node.pre is h and node.nex is t:
                self.freMap.pop(node.fre)
        return node.key

    def get(self, key: int) -> int:
        if key not in self.keyMap:
            return -1
        self.increase(self.keyMap[key])
        return self.keyMap[key].value
        
    def put(self, key: int, value: int) -> None:
        if not self.capacity:
            return
        if key in self.keyMap:
            node = self.keyMap[key]
            node.value = value
        else:
            node = Node(key, value)
            self.keyMap[key] = node
            self.size += 1
        if self.size > self.capacity:
            self.size -= 1
            k = self.delete(self.freMap[self.minFre][0].nex)
            # print(k)
            self.keyMap.pop(k)
        self.increase(node)

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
