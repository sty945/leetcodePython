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

from collections import defaultdict


class Solution3:
    def lengthOfLongestSubstring(self, s):
        begin, end , counter, d = 0, 0, 0, 0
        map_dict = defaultdict(int)
        while end < len(s):
            c = s[end]
            map_dict[c] += 1
            # counter表示重复字符的个数
            if map_dict[c] > 1:
                counter += 1
            end += 1
            # 将begin一直移到第一个重复字符的位置
            while counter > 0:
                char_tmp = s[begin]
                if map_dict[char_tmp] > 1:
                    counter -= 1
                map_dict[char_tmp] -= 1
                begin += 1
            # 每次计算下当前子串长度
            d = max(d, end - begin)
        return d