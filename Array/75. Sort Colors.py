# !/usr/bin/env python

# -*- coding: utf-8 -*-

# Time: 2018/2/18 14:57

# Author: sty

# File: 75. Sort Colors.py


class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zero = -1
        two = len(nums)
        i = 0
        while i < two:
            if nums[i] == 1:
                i += 1
            elif nums[i] == 2:
                two -= 1
                nums[i], nums[two] = nums[two], nums[i]
            else:
                zero += 1
                nums[zero], nums[i] = nums[i], nums[zero]
                i += 1


class Solution1:
    """
    Runtime: 36 ms,beats 100.0% of python3 submissions
    """
    def set_num(self, nums, count, num):
        for i in range(0, count):
            nums.append(num)
        return nums

    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zero_num = nums.count(0)
        one_num = nums.count(1)
        two_num = nums.count(2)
        nums.clear()
        if zero_num:
            nums = self.set_num(nums, zero_num, 0)
        if one_num:
            nums = self.set_num(nums, one_num, 1)
        if two_num:
            nums = self.set_num(nums, two_num, 2)


