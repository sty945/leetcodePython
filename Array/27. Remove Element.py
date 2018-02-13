# !/usr/bin/env python

# -*- coding: utf-8 -*-

# Time: 2018/2/13 13:55

# Author: sty

# File: 27. Remove Element.py


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        for i in range(nums.count(val)):
            nums.remove(val)
        return len(nums)

