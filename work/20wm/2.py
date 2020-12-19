# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-10-27 19:06:32
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-10-27 19:47:18

import sys


class Solution:
    def number2CNNMoney(self, money):
        def decoder_once(aa):
            res = ""
            for ii, jj in enumerate(aa):
                if jj != "0":
                    res += n2CN[int(jj)]
                    if len(aa) - ii == 4:
                        res += "仟"
                    elif len(aa) - ii == 3:
                        res += "佰"
                    elif len(aa) - ii == 2:
                        res += "拾"
            return res

        n2CN = "零壹贰叁肆伍陆柒捌玖"
        a = str(int(money))
        b = str(money)[len(a) :]

        res = ""
        N = len(str(a))
        A = [
            str(a)[-4 * (ii + 1) : -4 * ii if ii else None]
            for ii in range((N - 1) // 4 + 1)
        ]
        res = ""
        for ii, jj in enumerate(A):
            tmp = decoder_once(jj)
            if tmp != "":
                if ii == 1:
                    tmp += "万"
                elif ii == 2:
                    tmp += "亿"
            res = tmp + res
        if res == "":
            res = n2CN[0]
        res += "元"
        if b:
            b = b[1:]
            if len(b) and int(b) and res[-1] != n2CN[0]:
                res += n2CN[0]
            if len(b) >= 1 and int(b[0]):
                res += n2CN[int(b[0])] + "角"

            if len(b) >= 2 and int(b[1]):
                res += n2CN[int(b[1])] + "分"
        return res

