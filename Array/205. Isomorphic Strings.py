# -*- coding: utf-8 -*-

# !/usr/bin/env python

# Time: 2018/7/29 16:21

# Author: sty

# File: 205. Isomorphic Strings.py


class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ls = len(set(s))
        lt = len(set(t))
        return ls == lt and lt == len(set(list(zip(s, t))))