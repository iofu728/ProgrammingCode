# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2019-11-23 11:13:58
# @Last Modified by:   gunjianpan
# @Last Modified time: 2019-11-23 11:28:12

from sys import stdin


def main():
    def get_stdin():
        return int(stdin.readline().strip().split()[0])

    n = get_stdin()
    m = get_stdin()
    total = (1 + m) * m // 2
    max_index = m // n * n
    can_d = (n + max_index) * (max_index // n) // 2
    other_d = total - can_d
    print(other_d - can_d)


main()
