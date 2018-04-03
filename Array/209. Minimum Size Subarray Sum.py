# -*- coding: utf-8 -*-

# !/usr/bin/env python

# Time: 2018/4/3 8:48

# Author: sty

# File: 209. Minimum Size Subarray Sum

class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ans = n + 1
        left, ans_sum = 0, 0
        for i in range(n):
            ans_sum += nums[i]
            while ans_sum >= s:
                ans = min(ans, i + 1 - left)
                ans_sum -= nums[left]
                left += 1
        if ans != n + 1:
            return ans
        else:
            return 0
