# !/usr/bin/env python

# -*- coding: utf-8 -*-

# Time: 2018/2/18 16:29

# Author: sty

# File: 88. Merge Sorted Array.py


class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        nums = nums1.copy()
        nums1.clear()
        i, j = 0, 0
        while i < m and j < n:
            if nums[i] <= nums2[j]:
                nums1.append(nums[i])
                i += 1
            else:
                nums1.append(nums2[j])
                j += 1
        if i != m:
            while i < m:
                nums1.append(nums[i])
                i += 1
        if j != n:
            while j < n:
                nums1.append(nums2[j])
                j += 1
        return nums1


a = Solution()
list1 = [0]
list2 = [1]
b = a.merge(list1, 0, list2, 1)
print(b)

