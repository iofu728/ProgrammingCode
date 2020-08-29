# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-08-29 23:37:38
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-08-29 23:38:24

"""
381. Insert Delete GetRandom O(1) - Duplicates allowed Hard
Design a data structure that supports all following operations in average O(1) time.

Note: Duplicate elements are allowed.
insert(val): Inserts an item val to the collection.
remove(val): Removes an item val from the collection if present.
getRandom: Returns a random element from current collection of elements. The probability of each element being returned is linearly related to the number of same value the collection contains.
Example:

// Init an empty collection.
RandomizedCollection collection = new RandomizedCollection();

// Inserts 1 to the collection. Returns true as the collection did not contain 1.
collection.insert(1);

// Inserts another 1 to the collection. Returns false as the collection contained 1. Collection now contains [1,1].
collection.insert(1);

// Inserts 2 to the collection, returns true. Collection now contains [1,1,2].
collection.insert(2);

// getRandom should return 1 with the probability 2/3, and returns 2 with the probability 1/3.
collection.getRandom();

// Removes 1 from the collection, returns true. Collection now contains [1,2].
collection.remove(1);

// getRandom should return 1 and 2 both equally likely.
collection.getRandom();
Accepted 68,594 Submissions 200,697
"""
from collections import defaultdict
import bisect
import random


class RandomizedCollection:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.set = defaultdict(int)
        self.list = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        have = self.set[val] <= 0
        self.set[val] += 1
        bisect.insort(self.list, val)
        return have

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        have = self.set[val] > 0
        if have:
            self.set[val] -= 1
            idx = bisect.bisect_left(self.list, val)
            self.list.pop(idx)
        return have

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        size = len(self.list)
        return self.list[random.randint(0, size - 1)]


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
