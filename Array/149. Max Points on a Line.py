# -*- coding: utf-8 -*-

# !/usr/bin/env python

# Time: 2018/8/5 14:23

# Author: sty

# File: 149. Max Points on a Line.py


# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

from collections import defaultdict



class Solution:
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        length = len(points)
        if length == 0:
            return 0
        res_num = 0
        # points = map(lambda p: [p.x, p.y], points)
        for i in range(length):
            x1, y1 = points[i].x, points[i].y
            same = 1
            dict_temp = defaultdict(int)
            for j in range(i + 1, length):
                x2, y2 = points[j].x, points[j].y
                if i != j:
                    if x1 == x2 and y1 == y2:
                        same += 1
                    else:
                        a = y1 - y2
                        b = x2 - x1
                        c = x1 * y2 - x2 * y1
                        if a < 0 or a == 0 and b < 0:
                            a, b, c = -a, -b, -c
                        ratio = self.gcd(self.gcd(a, b), c)
                        dict_temp[(a/ratio, b/ratio, c/ratio)] += 1
            res_num = max(res_num, (max(dict_temp.values()) if dict_temp.values() else 0) + same)

            # for k, v in dict_temp.items():
            #     if v > res_num:
            #         res_num = v + same
        return res_num


