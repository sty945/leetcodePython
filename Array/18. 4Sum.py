# -*- coding: utf-8 -*-

# !/usr/bin/env python

# Time: 2018/8/4 22:15

# Author: sty

# File: 18. 4Sum.py

class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        length = len(nums)
        res = []
        if length < 4:
            return []
        elif length == 4:
            if sum(nums) == target:
                res.append(nums)
                return res
            else:
                return []
        nums.sort()
        for i in range(length - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, length - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                left = j + 1
                right = length - 1
                while left < right:
                    if nums[left] + nums[right] == target - nums[i] - nums[j]:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif nums[left] + nums[right] > target - nums[i] - nums[j]:
                        right -= 1
                    else:
                        left += 1
        return res



