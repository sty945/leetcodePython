# -*- coding: utf-8 -*-

# !/usr/bin/env python

# Time: 2018/7/21 12:31

# Author: sty

# File: 20. Valid Parentheses.py

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        string_stack = []
        for str in s:
            if len(string_stack) == 0:
                string_stack.append(str)
            else:
                if str == ')' and string_stack[-1] == '(':
                    string_stack.pop()
                elif str == '}' and string_stack[-1] == '{':
                    string_stack.pop()
                elif str == ']' and string_stack[-1] == '[':
                    string_stack.pop()
                else:
                    string_stack.append(str)
        if len(string_stack) != 0:
            return False
        return True


