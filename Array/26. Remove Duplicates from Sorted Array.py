# !/usr/bin/env python

# -*- coding: utf-8 -*-

# Time: 2018/2/13 14:05

# Author: sty

# File: 26. Remove Duplicates from Sorted Array.py

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        k = 0
        for i in range(1, len(nums)):
            if nums[k] != nums[i]:
                k += 1
                nums[k] = nums[i]
        return k + 1


class Solution2(object):
    def removeDuplicates(self, nums):
        """
        利用python属性
        :type nums: List[int]
        :rtype: int
        """
        nums[:] = sorted(set(nums))
        return len(nums)




