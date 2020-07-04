# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-03-22 20:37:31
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-06-05 18:03:53

"""
146. LRU Cache Medium

Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

## Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
 
Accepted 450,879 Submissions 1,488,460
"""
from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity: int):
        self.cmap = OrderedDict()
        self.cap = capacity

    def get(self, key: int) -> int:
        if key not in self.cmap:
            return -1
        self.cmap.move_to_end(key)
        return self.cmap[key]

    def put(self, key: int, value: int) -> None:
        self.cmap[key] = value
        self.cmap.move_to_end(key)
        if len(self.cmap) > self.cap:
            self.cmap.pop(list(self.cmap.keys())[0])


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


from header import read_data, VALID_AREAS


def clean_data(data):
    tt = {}
    for key, value in data.items():
        tmp = {ii: jj for ii, jj in value.items()}
        if len(tmp["expenditure"]) == 0:
            tmp["expenditure"] = None
        elif tmp["expenditure"][0] == "-":
            if not tmp["expenditure"][1:].isdigit():
                tmp["expenditure"] = None
        elif not tmp["expenditure"].isdigit():
            tmp["expenditure"] = None
        if tmp["area"] not in VALID_AREAS:
            tmp["area"] = None
        fin_years = tmp["fin_year"][2:].split("-")
        if len(fin_years) == 2 and len([ii for ii in fin_years if ii.isdigit()]) == 2:
            aa, bb = [int(ii) for ii in fin_years]
            cc = int(tmp["fin_year"][:4])
            if (
                (aa + 1) % 100 != bb
                or not (1997 <= cc <= 2011)
                or tmp["fin_year"][4] != "-"
                or len(tmp["fin_year"]) != 7
            ):
                tmp["fin_year"] = None
        else:
            tmp["fin_year"] = None
        tt[key] = tmp

    return tt


# to test your function with 'noisy_data.csv' or another CSV file,
# change the value of this variable
test_file = "noisy_sample.csv"

# you don't need to modify the code below
if __name__ == "__main__":
    data_noisy = read_data(test_file)

from header import read_data


def avg_expenditure(data, start, end):
    s = int(start[:4])
    if int(end[:4]) == 1999:
        e = 2000
    else:
        e = int(end[:2] + end[-2:])

    if s <= e:
        num, total = 0, 0
        for key, value in data.items():
            if (
                value["fin_year"] is None
                or value["fin_year"] == ""
                or value["expenditure"] is None
            ):
                continue
            now = int(value["fin_year"][:4])
            if s <= now < e:
                total += int(value["expenditure"]) if len(value["expenditure"]) else 0
                num += 1
        if num == 0:
            return 0
        return int(round(total / num))
    else:
        return -1


# to test your function with 'cleaned_data.csv' or another CSV file,
# change the value of this variable
test_file = "cleaned_sample.csv"

# you don't need to modify the code below
if __name__ == "__main__":
    data_cleaned = read_data(test_file)

from header import read_data, VALID_AREAS


def funding_dist(data, n_bins, area):
    max_expend, min_expend = 0, 0
    for key, value in data.items():
        # ignore invalid data
        if (
            value["area"] is None
            or value["area"] == ""
            or value["expenditure"] is None
            or value["expenditure"] == ""
        ):
            continue
        if value["area"] == area and int(value["expenditure"]) > max_expend:
            max_expend = int(value["expenditure"])
        if value["area"] == area and int(value["expenditure"]) < min_expend:
            min_expend = int(value["expenditure"])
    bin_width = (max_expend - min_expend) // int(n_bins)
    dist = []
    for i in range(n_bins):
        num = 0
        for key, value in data.items():
            if (
                value["area"] is None
                or value["area"] == ""
                or value["expenditure"] is None
                or value["expenditure"] == ""
                or value["area"] != area
            ):
                continue
            if i < (n_bins - 1):
                if (
                    (min_expend + i * bin_width)
                    <= round(value["expenditure"])
                    < (min_expend + (i + 1) * bin_width)
                ):
                    num += 1
            if i == (n_bins - 1):
                if (
                    (min_expend + i * bin_width)
                    <= int(value["expenditure"])
                    <= max_expend
                ):
                    num += 1
        dist.append(num)
    return dist


# to test your function with another CSV file,
# change the value of this variable
test_file = "cleaned_data.csv"

# you don't need to modify the code below
if __name__ == "__main__":
    data_cleaned = read_data(test_file)

from header import read_data, VALID_AREAS


def area_expenditure_counts(data, lower_spent, upper_spent):
    allarea = {}
    # for area in VALID_AREAS:
    # if lower_spent > upper_spent:
    #     return 0
    if lower_spent < upper_spent:
        for key, value in data.items():
            if (
                value["area"] is None
                or value["area"] == ""
                or value["expenditure"] is None
                or value["expenditure"] == ""
            ):
                continue
            area = value["area"]
            if lower_spent <= int(value["expenditure"]) <= upper_spent:
                allarea[area] = allarea.get(area, 0) + 1
    # store the 5 most counts in top5
    for ii in VALID_AREAS:
        if ii not in allarea:
            allarea[ii] = 0
    top5 = []
    for i, j in sorted(allarea.items(), key=lambda x: (-x[1], x[0]))[:5]:
        top5.append((i, j))
    return top5


# to test your function with another CSV file,
# change the value of this variable
test_file = "cleaned_data.csv"

# you don't need to modify the code below
if __name__ == "__main__":
    data_cleaned = read_data(test_file)


from header import read_data, VALID_AREAS
from reference import clean_data, avg_expenditure, funding_dist, area_expenditure_counts


def main(datafile):
    print("Average Australian health expenditure")
    data_cleaned = read_data(datafile)
    new_data = clean_data(data_cleaned)
    for year in range(1997, 2012):
        start = str(year) + "-" + str(year + 1)[-2:]
        end = str(year + 1) + "-" + str(year + 2)[-2:]
        tmp = avg_expenditure(new_data, start, end)
        if tmp != 0:
            print(start, "({},000,000)".format(tmp))
    print("\n")
    print("Top 5 health expenditure areas by count")
    result = area_expenditure_counts(new_data, 0, 800)
    for i in range(5):
        if result[i][1] != 0:
            print("{} ({})".format(result[i][0], result[i][1]))
