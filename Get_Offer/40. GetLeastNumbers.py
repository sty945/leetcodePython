# -*- coding: utf-8 -*-

# !/usr/bin/env python

# Time: 2018/5/13 15:39

# Author: sty

# File: 40. GetLeastNumbers.py

class Solution:
    """
    最小的 K 个数
    practice:https://www.nowcoder.com/practice/6a296eb82cf844ca8539b57c23e6e9bf?tpId=13&tqId=11182&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking
    """
    def find_kth_smallest(self, nums, k):
        l, h = 0, len(nums) - 1
        while l < h:
            j = self.partition(nums, l, h)
            if j == k:
                break
            if j > k:
                h = j - 1
            else:
                l = j + 1

    def partition(self, nums, low, high):
        parti = nums[low]
        while low < high:
            while low < high and nums[high] >= parti:
                high -= 1
            nums[low] = nums[high]
            while low < high and nums[low] <= parti:
                low += 1
            nums[high] = nums[low]
        nums[low] = parti
        return low

    def GetLeastNumbers_Solution(self, tinput, k):
        res = []
        if k > len(tinput) or k <= 0:
            return res
        self.find_kth_smallest(tinput, k - 1)
        print(tinput)
        for i in range(k):
            res.append(tinput[i])
        return sorted(res)

# a = Solution()
# print(a.GetLeastNumbers_Solution([4,5,1,6,2,7,3,8], 4))