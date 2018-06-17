# -*- coding: utf-8 -*-

# !/usr/bin/env python

# Time: 2018/6/4 23:07

# Author: sty

# File: 10. Regular Expression Matching.py


class Solution1:
    """
    If a star is present in the pattern, it will be in the second position pattern[1].
    Then, we may ignore this part of the pattern, or delete a matching character in the text.
    If we have a match on the remaining strings after any of these operations, then the initial inputs matched.
    """
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p:
            return not s

        first_match = bool(s) and p[0] in {s[0], '.'}
        if len(p) >= 2 and p[1] == '*':
            return (self.isMatch(s, p[2:]) or
                    first_match and self.isMatch(s[1:], p))
        else:
            return first_match and self.isMatch(s[1:], p[1:])

# a = Solution()
# res = a.isMatch('aa', 'a*')
# print(res)