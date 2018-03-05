# !/usr/bin/env python

# -*- coding: utf-8 -*-

# Time: 2018/3/5 11:15

# Author: sty

# File: 344. Reverse String.py


class Solution:
    """
    classic method
    """
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        i, j = 0, len(s) - 1
        s = list(s)
        while i < j:
            s[i],s[j] = s[j], s[i]
            i += 1
            j -= 1
        return ''.join(s)


class Solution1:
    """
    By using python specifics
    """
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]