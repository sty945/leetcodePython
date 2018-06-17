# -*- coding: utf-8 -*-

# !/usr/bin/env python

# Time: 2018/6/17 15:44

# Author: sty

# File: 15. 3Sum.py


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length = len(nums)
        if length < 3:
            return []
        if length == 3:
            if sum(nums) == 0:
                return [nums]
            else:
                return []

        nums.sort()
        res = []
        for i in range(length - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue;
            j = i + 1
            k = length - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s < 0:
                    j += 1
                elif s > 0:
                    k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k - 1] == nums[k]:
                        k -= 1
                    j += 1
                    k -= 1
        return res

# a = Solution()
# res = a.threeSum([-1,0,1,2,-1,-4])
# print(res)
