# !/usr/bin/env python

# -*- coding: utf-8 -*-

# Time: 2018/2/13 12:57

# Author: sty

# File: 283. Move Zeroes.py

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = 0
        for i in range(0, len(nums)):
            if nums[i]:
                if i != k:
                    nums[k], nums[i] = nums[i], nums[k]
                    k += 1
                else:
                    k += 1
            else:
                pass


class Solution2(object):
    def moveZeroes(self, nums):
        """
        利用python自身的属性解决问题
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        num_0 = nums.count(0)
        for i in range(num_0):
            nums.remove(0)
            nums.append(0)


