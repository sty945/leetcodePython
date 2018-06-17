# -*- coding: utf-8 -*-

# !/usr/bin/env python

# Time: 2018/6/17 16:49

# Author: sty

# File: 1. Two Sum.py


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict_temp = dict()
        for i in range(len(nums)):
            dict_temp[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in dict_temp and dict_temp[complement] != i:
                return [i, dict_temp[complement]]
        return []
