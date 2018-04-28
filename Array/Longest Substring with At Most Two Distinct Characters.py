# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Time: 2018/4/29 7:14
# Author: sty
# File: Longest Substring with At Most Two Distinct Characters.py

from collections import defaultdict

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s):
        begin, end, counter, length = 0, 0, 0, 0
        map_dict = defaultdict(int)
        while end < len(s):
            c = s[end]
            map_dict[c] += 1
            # counter 表示新的字符
            if map_dict == 1:
                counter += 1
            end += 1
            # 如果新字符的数量大于2,就开始移动窗口
            while counter > 2:
                char_tmp = s[begin]
                if map_dict[char_tmp] == 1:
                    counter -= 1
                map_dict[char_tmp] -= 1
                begin += 1
            length = max(length, end - begin)
        return length
