# -*- coding: utf-8 -*-

# !/usr/bin/env python

# Time: 2018/4/3 9:14

# Author: sty

# File: 3. Longest Substring Without Repeating Characters.py


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq = [0 for i in range(256)]
        l, r = 0, -1
        res = 0
        while l < len(s):
            if r + 1 < len(s) and freq[ord(s[r + 1])] == 0:
                r += 1
                freq[ord(s[r])] += 1
            else:
                freq[ord(s[l])] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res


class Solution2:
    def lengthOfLongestSubstring(self, s):
        """
        use dict
        :param s:
        :return:
        """
        dic, res, start, = {}, 0, 0
        for i, ch in enumerate(s):
            if ch in dic:
                start = max(start, dic[ch]+1)
            res = max(res, i-start+1)
            dic[ch] = i
        return res