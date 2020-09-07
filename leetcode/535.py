# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-07 11:19:27
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-07 11:21:50

"""
535. Encode and Decode TinyURL Medium
Note: This is a companion problem to the System Design problem: Design TinyURL.
TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.

Accepted 110,732 Submissions 138,392
"""
import random


class Codec:
    def __init__(self):
        self.word_list = (
            "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        )
        self.word_size = len(self.word_list)
        self.word_map = {}
        self.basic_url = "http://tinyurl.com/"

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        code_size = random.randint(6, 12)
        res = ""
        for ii in range(code_size):
            res += self.word_list[random.randint(0, self.word_size - 1)]
        self.word_map[res] = longUrl
        return "{}{}".format(self.basic_url, res)

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        res = shortUrl.replace(self.basic_url, "")
        return self.word_map[res]
