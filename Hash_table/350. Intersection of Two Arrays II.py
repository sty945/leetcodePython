# -*- coding: utf-8 -*-

# !/usr/bin/env python

# Time: 2018/6/17 22:27

# Author: sty

# File: 350. Intersection of Two Arrays II.py

from collections import defaultdict

class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dict_num1 = defaultdict(int)
        dict_res = defaultdict(int)

        for i in nums1:
            dict_num1[i] += 1

        for i in nums2:
            if i in dict_num1 and dict_num1[i] > 0:
                dict_res[i] += 1
                dict_num1[i] -= 1

        res = []
        for k, v in dict_res.items():
            for i in range(v):
                res.append(k)
        return res
