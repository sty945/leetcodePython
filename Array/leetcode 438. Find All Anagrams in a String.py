# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Time: 2018/4/29 7:10
# Author: sty
# File: leetcode 438. Find All Anagrams in a String.py

from collections import defaultdict


class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res = []
        map_dict = defaultdict(int)
        if len(p) > len(s):
            return res
        for c in p:
            map_dict[c] += 1
        couter = len(map_dict)
        begin , end = 0, 0

        while end < len(s):
            c = s[end]
            if c in map_dict:
                map_dict[c] -= 1
                if map_dict[c] == 0:
                    couter -= 1
            end += 1

            while couter == 0:
                tempc = s[begin]
                if tempc in map_dict:
                    map_dict[tempc] += 1
                    if map_dict[tempc] > 0:
                        couter += 1
                if len(p) == end - begin:
                    res.append(begin)
                begin += 1
        return res