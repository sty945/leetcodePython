# -*- coding: utf-8 -*-

# !/usr/bin/env python

# Time: 2018/8/5 11:50

# Author: sty

# File: 454. 4Sum II.py

from collections import defaultdict
class Solution:
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        ab_sum_dict = defaultdict(int)
        res_sum = 0
        for i in A:
            for j in B:
                ab_sum_dict[i + j] += 1
        for i in C:
            for j in D:
                if -i-j in ab_sum_dict:
                    res_sum += ab_sum_dict[-i-j]
        return res_sum
