# coding:utf-8

# !/usr/bin/env python

# Time: 2018/8/7 9:41

# Author: sty

# File: 217. Contains Duplicate.py


class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 2:
            return False
        res_dict = dict()
        for i in nums:
            if i in res_dict:
                return True
            else:
                res_dict[i] = 1
        return False
