# -*- coding: utf-8 -*-

# !/usr/bin/env python

# Time: 2018/5/12 13:58

# Author: sty

# File: 76. Minimum Window Substring.py

from collections import defaultdict


class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        map_dict = defaultdict(int)
        if len(t) > len(s):
            return ""
        for c in t:
            map_dict[c] += 1
        couter = len(map_dict)
        begin, end = 0, 0
        head = 0
        length = len(s) + 1

        while end < len(s):
            c = s[end]
            if c in map_dict:
                map_dict[c] -= 1
                # 与下面的判断，每遇到一个在map_dict中的字符就减1，下面的判断每次遇到一个在map_dict字符就加1
                if map_dict[c] == 0:
                    couter -= 1
            end += 1

            while couter == 0:
                tempc = s[begin]
                if tempc in map_dict:
                    map_dict[tempc] += 1
                    # 为了下次找到再出现的map_dict中的数
                    if map_dict[tempc] > 0:
                        couter += 1
                if length > end - begin:
                    length = end - begin
                    head = begin
                begin += 1

        if length == len(s) + 1:
            return ""
        return s[head:head + length]
