# -*- coding: utf-8 -*-

# !/usr/bin/env python

# Time: 2018/7/29 16:30

# Author: sty

# File: 451. Sort Characters By Frequency.py

from collections import defaultdict
class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        res_dict = defaultdict(int)
        for i in s:
            res_dict[i] += 1
        s_dict = sorted(res_dict.items(), key=lambda e:e[1], reverse=True)
        res_str = []
        for k, v in s_dict:
            res_str.append(k * v)
        return ''.join(res_str)

import collections
class Solution1(object):
    def frequencySort(self, str):
        """
        :type str: str
        :rtype: str
        """
        return "".join([char * times for char, times in collections.Counter(str).most_common()])

