# !/usr/bin/env python

# -*- coding: utf-8 -*-

# Time: 2018/2/20 11:40

# Author: sty

# File: 125. Valid Palindrome.py

class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        s = s.lower()
        res = ''
        for i in range(len(s)):
            if 'a' <= s[i] <= 'z' or '0' <= s[i] <= '9':
                res += s[i]
        low, high = 0, len(res) - 1
        while low < high:
            if res[low] == res[high]:
                low += 1
                high -= 1
            else:
                return False
        return True


