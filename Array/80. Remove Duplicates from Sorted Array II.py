# !/usr/bin/env python

# -*- coding: utf-8 -*-

# Time: 2018/2/13 16:38

# Author: sty

# File: 80. Remove Duplicates from Sorted Array II.py


class Solution(object):
    """
    对数组元素进行去重，使得原数组重复元素最多保留2个
    """
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return len(nums)

        i, j, cnt = 1, 1, 1
        while j < len(nums):
            if nums[j] != nums[j - 1]:
                cnt = 1
                nums[i] = nums[j]
                i += 1
            else:
                if cnt < 2:
                    nums[i] = nums[j]
                    i += 1
                    cnt += 1
            j += 1
        return i

    def removeDuplicates2(self, nums):
        """
        very short code
        :param nums:
        :return:
        """
        i = 0
        for n in nums:
            if i < 2 or n > nums[i - 2]:
                nums[i] = n
                i += 1
        return i


class Solution1(object):
    """
    对数组元素进行去重，使得原数组重复元素最多保留k个
    """
    def removeDuplicates(self, nums, k):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= k:
            return len(nums)

        i, j, cnt = 1, 1, 1
        while j < len(nums):
            if nums[j] != nums[j - 1]:
                cnt = 1
                nums[i] = nums[j]
                i += 1
            else:
                if cnt < k:
                    nums[i] = nums[j]
                    i += 1
                    cnt += 1
            j += 1
        return i

    def removeDuplicates2(self, nums, k):
        """
        very short code
        :param nums:
        :return:
        """
        i = 0
        for n in nums:
            if i < k or n > nums[i - k]:
                nums[i] = n
                i += 1
        return i
