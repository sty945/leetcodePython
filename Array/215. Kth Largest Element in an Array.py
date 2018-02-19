# !/usr/bin/env python

# -*- coding: utf-8 -*-

# Time: 2018/2/19 16:40

# Author: sty

# File: 215. Kth Largest Element in an Array.py

import random

class Solution:
    def partition(self, nums, low, high):
        pivot = nums[low]
        while low < high:
            while low < high and nums[high] >= pivot:
                high -= 1
            nums[low] = nums[high]
            while low < high and nums[low] <= pivot:
                low += 1
            nums[high] = nums[low]
        nums[low] = pivot
        return low

    def find(self, nums, k, m, n):
        p = self.partition(nums, m, n)
        if p == k:
            return nums[p]
        if p > k:
            return self.find(nums, k, m, p-1)
        if p < k:
            return self.find(nums, k, p+1, n)

    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #  O(N) guaranteed running time + O(1) space by using shuffle algorithm
        # O(N) best case / O(N^2) worst case running time + O(1) memory if not use shuffle algorithm
        random.shuffle(nums)
        m = 0
        n = len(nums) - 1
        k = len(nums) - k
        return self.find(nums, k, m, n)


#Knuth-Durstenfeld Shuffle
def shuffle(lis):
    for i in range(len(lis) - 1, 0, -1):
        p = random.randrange(0, i + 1)
        lis[i], lis[p] = lis[p], lis[i]
    return lis
