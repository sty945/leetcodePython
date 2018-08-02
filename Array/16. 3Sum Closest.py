# coding:utf-8

# !/usr/bin/env python

# Time: 2018/8/2 9:03

# Author: sty

# File: 16. 3Sum Closest.py


class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        length = len(nums)
        if length < 3:
            return []
        if length == 3:
            return sum(nums)

        closest = target
        min_diff = sum(nums)
        nums.sort()
        for i in range(0, length - 2):
            left = i + 1;
            right = length -1
            two_sum = target - nums[i]
            temp_sum = nums[left] + nums[right]
            while left < right:
                if temp_sum == two_sum:
                    return target
                else:
                    if abs(temp_sum - two_sum) < min_diff:
                        min_diff = abs(temp_sum - two_sum)
                        closest = temp_sum + nums[i]
                    if temp_sum > two_sum:
                        right -= 1
                    else:
                        left += 1
        return closest


