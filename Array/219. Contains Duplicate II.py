# coding:utf-8

# !/usr/bin/env python

# Time: 2018/8/7 8:38

# Author: sty

# File: 219. Contains Duplicate II.py


class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        length = len(nums)
        if length < 2:
            return False
        res_num = {}
        for i in range(length):
            if nums[i] in res_num and i - res_num[nums[i]] <= k:
                return True
            res_num[nums[i]] = i
        return False