# -*- coding: utf-8 -*-

# !/usr/bin/env python

# Time: 2018/6/18 15:00

# Author: sty

# File: 202. Happy Number.py

from collections import defaultdict
class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        res_have_dict = defaultdict(int)
        while 1:
            list_num = []
            while n:
                list_num.append(n % 10)
                n //= 10
            pow_res = [i * i for i in list_num]
            res = sum(pow_res)
            if res == 1:
                return True
            else:
                n = res
            if res not in res_have_dict:
                res_have_dict[res] += 1
            else:
                return False

# a = Solution()
# print(a.isHappy(19))
# print(a.isHappy(39))

