# -*- coding: utf-8 -*-

# !/usr/bin/env python

# Time: 2018/5/12 17:37

# Author: sty

# File: 30. Substring with Concatenation of All Words.py

from collections import defaultdict

class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        res = []
        if len(words) == 0 or len(s) < len(words[0]) * len(words):
            return res
        str_len = len(s)
        word_len = len(words[0])
        total_len = len(words) * word_len
        map_dict = defaultdict(int)
        cur_dict = defaultdict(int)
        for word in words:
            map_dict[word] += 1

        for start in range(0, str_len - total_len + 1):
            end = start
            while end < start + total_len:
                substr = s[end: end + word_len]
                cur_dict[substr] += 1
                # 如果当前dict中还有之前的没有的，或者值比至之前的大都终止
                if cur_dict[substr] > map_dict[substr]:
                    break
                end += word_len
            if end == start + total_len:
                res.append(start)
            cur_dict.clear()
        return res





