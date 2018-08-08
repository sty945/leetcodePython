# -*- coding: utf-8 -*-

# !/usr/bin/env python

# Time: 2018/8/8 21:44

# Author: sty

# File: 220. Contains Duplicate III.py

# Info:http://bookshadow.com/weblog/2015/06/03/leetcode-contains-duplicate-iii/
# info:https://www.geeksforgeeks.org/bucket-sort-2/


from collections import OrderedDict
class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        length = len(nums)
        if length < 2 or k < 1 or t < 0:
            return False
        dict_num = OrderedDict()
        for i in range(length):
            key = nums[i] / max(1, t)
            for m in (key - 1, key, key + 1):
                if m in dict_num and abs(nums[i] - dict_num[m]) <= t:
                    return True
            dict_num[key] = nums[i]
            if i >= k:
                dict_num.popitem(last=False)
        return False

        return False

