# -*- coding: utf-8 -*-

# !/usr/bin/env python

# Time: 2018/6/18 13:45

# Author: sty

# File: 242. Valid Anagram.py


from collections import defaultdict
class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict_s = defaultdict(int)
        dict_t = defaultdict(int)
        if len(s) == 0 and len(t) == 0:
            return True
        for i in s:
            dict_s[i] += 1

        for i in t:
            dict_t[i] += 1

        if len(dict_s) != len(dict_t):
            return False
        else:
            for k, v in dict_s.items():
                if dict_t[k] != v:
                    return False
        return True

# a = Solution()
# print(a.isAnagram("anagram", "nagaram"))