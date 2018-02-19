# !/usr/bin/env python

# -*- coding: utf-8 -*-

# Time: 2018/2/18 16:29

# Author: sty

# File: 88. Merge Sorted Array.py


class Solution:
    """
    time complexity: O(m+n)
    space complexity: O(n)
    """
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


class Solution1:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i, j, k = m - 1, n - 1, m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                k -= 1
                i -= 1
            else:
                nums1[k] = nums2[j]
                k -= 1
                j -= 1
        if i >= 0:
            nums1[:k+1] = nums1[:i+1]
        if j >= 0:
            nums1[:k+1] = nums2[:j+1]
