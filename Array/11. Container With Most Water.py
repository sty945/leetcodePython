# !/usr/bin/env python

# -*- coding: utf-8 -*-

# Time: 2018/3/14 20:35

# Author: sty

# File: 11. Container With Most Water.py


class Solution:
    """
    求坐标轴上竖线围成的面积可以装最多的水，对撞指针
    """
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        low, high = 0, len(height) - 1
        max_container = 0
        res_start, res_end = 0, 0
        while low <= high:
            start_line, end_line = height[low], height[high]
            min_line = min(start_line, end_line)
            container = (high - low) * min_line
            if container > max_container:
                max_container = container
            if min_line == start_line:
                low += 1
            else:
                high -= 1
        return max_container
