# -*- coding: utf-8 -*-

# !/usr/bin/env python

# Time: 2018/8/5 14:06

# Author: sty

# File: 447. Number of Boomerangs.py

from collections import defaultdict
class Solution:
    def get_dis_pow(self, point_a, point_b):
        return pow(point_a[0] - point_b[0], 2) + pow(point_a[1] - point_b[1], 2)
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        length = len(points)
        if length <= 1:
            return 0
        res = 0
        for i in range(length):
            res_dict = defaultdict(int)
            for j in range(length):
                if i != j:
                    res_dict[self.get_dis_pow(points[i], points[j])] += 1
            for k, v in res_dict.items():
                res += v * (v - 1)
        return res


