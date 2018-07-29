# -*- coding: utf-8 -*-

# !/usr/bin/env python

# Time: 2018/7/29 15:42

# Author: sty

# File: 290. Word Pattern.py


class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str_list = str.split()
        if len(pattern) != len(str_list) or len(set(pattern)) != len(set(str_list)):
            return False
        res = set()
        for i in range(len(pattern)):
            res.add((pattern[i], str_list[i]))
        if len(res) == len(set(pattern)):
            return True
        else:
            return False


class Solution1:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str_list = str.split()
        lp = len(set(pattern))
        ls = len(set(str_list))
        return len(pattern) == len(str_list) and lp == ls and lp == len(set(list(zip(pattern, str_list))))

