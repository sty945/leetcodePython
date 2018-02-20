# !/usr/bin/env python

# -*- coding: utf-8 -*-

# Time: 2018/2/20 10:11

# Author: sty

# File: 167. Two Sum II - Input array is sorted.py


class Solution:
    """
    By using binary Search to solve problem
    O(nlog(n))
    """
    def binSearch(self, numbers, low, high, target):
        while low < high:
            mid = low + (high - low) // 2
            if numbers[mid] == target:
                return mid
            elif numbers[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return -1

    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(numbers)
        for i in range(length - 1):
            res = self.binSearch(numbers, i + 1, length - 1, target - numbers[i])
            if res != -1:
                return [i + 1, res + 1]
        return []


class Solution1:
    """
    By using two pointer
    O(n)
    """
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        low, high = 0, len(numbers) - 1
        while low < high:
            if numbers[low] + numbers[high] == target:
                return [low + 1, high + 1]
            elif numbers[low] + numbers[high] < target:
                low += 1
            else:
                high -= 1

