# -*- coding: utf-8 -*-

# !/usr/bin/env python

# Time: 2018/4/7 13:01

# Author: sty

# File: 567. Permutation in String.py


class Solution:
    """
    暴力解法
    """
    def perm(self, s=''):
        if len(s) <= 1:
            return [s]
        sl = []
        for i in range(len(s)):
            for j in self.perm(s[0:i] + s[i + 1:]):
                sl.append(s[i] + j)
        return sl

    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False
        s1_perm = list(set(self.perm(s1)))
        for i in s1_perm:
            index = s2.find(i)
            if index != -1:
                return True
        return False

from collections import defaultdict
import operator
class Solution1:
    """
    使用hashmap的方式
    """
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False
        map_dict1 = defaultdict(int);
        map_dict2 = defaultdict(int);
        for i in s1:
            map_dict1[i] += 1
        for i in range(len(s2) - len(s1) + 1):
            for j in range(len(s1)):
                map_dict2[s2[i + j]] += 1
            if operator.eq(map_dict1, map_dict2):
                return True
            map_dict2.clear()
        return False


class Solution2:
    """
    使用list计数的方法
    """
    def match(self, s1, s2):
        for i in range(26):
            if s1[i] != s2[i]:
                return False
        return True

    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False
        list1 = [0 for i in range(26)]
        for i in s1:
            list1[ord(i) - ord('a')] += 1
        for i in range(len(s2) - len(s1) + 1):
            list2 = [0 for i in range(26)]
            for j in range(len(s1)):
                list2[ord(s2[i + j]) - ord('a')] += 1
            if self.match(list1, list2):
                return True
        return False


class Solution3:
    """
    滑动窗口法，时间复杂度O(l1+26∗(l2−l1),l1是s1的长度,l2是s2的长度
    """
    def match(self, s1, s2):
        for i in range(26):
            if s1[i] != s2[i]:
                return False
        return True

    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False
        list1 = [0 for i in range(26)]
        list2 = [0 for i in range(26)]
        for i in range(len(s1)):
            list1[ord(s1[i]) - ord('a')] += 1
            list2[ord(s2[i]) - ord('a')] += 1
        for i in range(len(s2) - len(s1)):
            if self.match(list1, list2):
                return True
            list2[ord(s2[i + len(s1)]) - ord('a')] += 1
            list2[ord(s2[i]) - ord('a')] -= 1
        return self.match(list1, list2)


class Solution4:
    """
    进阶的滑动窗口法,使用count来表示26个字符频率在s1,s2中相同个数
    """
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False
        list1 = [0 for i in range(26)]
        list2 = [0 for i in range(26)]
        for i in range(len(s1)):
            list1[ord(s1[i]) - ord('a')] += 1
            list2[ord(s2[i]) - ord('a')] += 1

        count = 0
        for i in range(26):
            if list1[i] == list2[i]:
                count += 1

        for i in range(len(s2) - len(s1)):
            r = ord(s2[i + len(s1)]) - ord('a')
            l = ord(s2[i]) - ord('a')
            if count == 26:
                return True
            list2[r] += 1
            if list2[r] == list1[r]:
                count += 1
            elif list2[r] == list1[r] + 1:
                count -= 1
            list2[l] -= 1
            if list2[l] == list1[l]:
                count += 1
            elif list2[l] == list1[l] - 1:
                count -= 1
        return count == 26

