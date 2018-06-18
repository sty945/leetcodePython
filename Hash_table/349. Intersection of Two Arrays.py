# -*- coding: utf-8 -*-

# !/usr/bin/env python

# Time: 2018/6/17 21:17

# Author: sty

# File: 349. Intersection of Two Arrays.py

class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        set_num1 = set(nums1)
        set_num2 = set(nums2)
        res = set_num1 & set_num2
        return list(res)

a = Solution()
print(a.intersection([1, 2, 2, 1], [2, 2]))