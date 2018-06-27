# -*- coding: utf-8 -*-

# !/usr/bin/env python

# Time: 2018/6/26 23:06

# Author: sty

# File: 17. Letter Combinations of a Phone Number.py

class Solution:
    """
    使用循环
    """
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        num = dict()
        num['2'] = 'abc'
        num['3'] = 'def'
        num['4'] = 'ghi'
        num['5'] = 'jkl'
        num['6'] = 'mno'
        num['7'] = 'pqrs'
        num['8'] = 'tuv'
        num['9'] = 'wxyz'
        if len(digits) == 0:
            return []
        all_res = [""]
        for digit in digits:
            new_res = []
            for letter in num[digit]:
                for res in all_res:
                    new_res.append(res+letter)
            all_res = new_res
        return all_res

class Solution1:
    """
    递归使用
    """
    d = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return self.d[digits]
        res = []
        l = self.letterCombinations(digits[:-1])
        r = self.letterCombinations(digits[-1])
        for i in l:
            for j in r:
                res.append(i + j)
        return res

a = Solution1()
print(a.letterCombinations("234"))
