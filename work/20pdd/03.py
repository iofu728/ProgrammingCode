# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-08-02 18:57:32
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-08-02 20:57:24


import sys

N, M, T = [int(ii) for ii in sys.stdin.readline().strip().split()]
NN, MM = [], []
for ii in range(N):
    NN.append([int(ii) for ii in sys.stdin.readline().strip().split()])
for ii in range(M):
    MM.append([int(ii) for ii in sys.stdin.readline().strip().split()])


def get_engine():
    if not T:
        return 0
    nn = sorted(NN, key=lambda x: (-x[1], x[0]))
    mm = sorted(MM, key=lambda x: (-x[1], x[0]))
    n_max_T = nn[0]
    m_max_T = mm[0]
    if n_max_T[1] + m_max_T[1] < T:
        return -1
    res = 10 ** 9 + 7
    # n_min_T = min(enumerate(nn), key=lambda x: x[1][0])
    nn = [[ii, jj] for ii, jj in nn if jj + m_max_T[1] >= T]
    mm = [[ii, jj] for ii, jj in mm if jj + n_max_T[1] >= T]
    nn1, mm1 = {}, {}
    for ii, jj in nn:
        if jj not in nn1:
            nn1[jj] = ii
    for ii, jj in mm:
        if jj not in mm1:
            mm1[jj] = ii
    nn = [[v, k] for k, v in nn1.items()]
    mm = [[v, k] for k, v in mm1.items()]

    m_min_T = min(enumerate(mm), key=lambda x: x[1][0])
    # n_min_T = min(enumerate(nn), key=lambda x: x[1][0])
    # print(nn, m_min_T)
    nn1 = [[ii, jj] for ii, jj in nn if jj + m_min_T[1][1] >= T]
    # mm1 = [[ii, jj] for ii, jj in mm if jj + n_min_T[1][1] >= T]

    res = min(nn1, key=lambda x: x[0])[0] + m_min_T[1][0]
    # res = min(res, min(mm1, key=lambda x: x[0])[0] + n_min_T[1][0])
    nn = nn[len(nn1) :]
    last_mm = -1
    for ni, nj in nn:
        if nj >= T:
            if ni < res:
                res = ni
                mm = [[ii, jj] for ii, jj in mm if ii < ni]
                if not len(mm):
                    break
            continue
        if ni >= res:
            continue
        if last_mm != -1 and last_mm[-1] + nj >= T:
            tmp_MM = last_mm
        elif last_mm != -1 and last_mm[0] + ni >= res:
            continue
        else:
            tmp_MM = [[ii, jj] for ii, jj in mm if jj + nj >= T]
            if not len(tmp_MM):
                break
            tmp_MM = min(enumerate(tmp_MM), key=lambda x: x[1][0])
            mm = mm[: tmp_MM[0]]
            tmp_MM = tmp_MM[1]
            last_mm = tmp_MM
        if ni + tmp_MM[0] < res:
            res = ni + tmp_MM[0]
            mm = [[ii, jj] for ii, jj in mm if ii < ni]
            if not len(mm):
                break

        # print(ni, nj, tmp_MM, res)
    return res


print(get_engine())

