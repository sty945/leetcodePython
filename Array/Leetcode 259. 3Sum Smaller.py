# coding:utf-8

# !/usr/bin/env python

# Time: 2018/8/2 11:48

# Author: sty

# File: Leetcode 259. 3Sum Smaller.py


class Solution:
    def threeSumSmaller(self, nums, target):
        count = 1
        length = len(nums)
        if length < 3:
            return 0
        elif length == 3:
            if sum(nums) < target:
                return 1
            else:
                return 0

        nums.sort()
        for i in range(0, length - 2):
            two_sum = target - nums[i]
            left = i + 1
            right = length - 1
            while left < right:
                if nums[left] + nums[right] >= two_sum:
                    right -= 1
                else:
                    left += 1
                    count += 1
        return count
