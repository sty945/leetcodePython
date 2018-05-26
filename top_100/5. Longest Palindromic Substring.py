# -*- coding: utf-8 -*-

# !/usr/bin/env python

# Time: 2018/5/25 9:05

# Author: sty

# File: 5. Longest Palindromic Substring.py

class Solution:
    """
    假若一个字符串是一个回数，那么该字符串内部一定还存在更多的回数。例如，abbbcbbba是一个回数，那么bbbcbbb一定是一个回数，那么bcb也是回数，最后到b。同理，bccb是一个回数，那么cc也是一个回数。因此可以看出，假设当前一个字符串是回数，那么加上两侧的字符可能还是回数。假设当前一个字符串不是回数，那么加上右侧的字符可能构成一个回数。
因此，假设当前得到的回数的最大长度为n，我们可以判断n+1或者n+2是不是回数。
为什么这么判断呢？下面给出证明。
我们假设有一个字符串xxxxxxxxabaxxxxxxs，其中x代表任意字符。
假设此时指针指向s，而已知最大回数子字符串的长度为3。我们只需要判断xxxs以及xxxxs是不是回数。无需判断xxs乃至更近是因为它们的长度必然无法超过当前的最大长度。而无需判断xxxxxs乃至更远是因为假如xxxxxs是回数，那么xxxx一定是回数，则当前的最大长度为4而不是3，与题设不符。所以只需判断两种情况。
这里就充分利用了回数的性质，省去了很多无效的遍历
    """
    def isPalindrome(self, s, start, end):
        if start < 0:
            return False
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        curr_len = 0
        for i in range(len(s)):
            if self.isPalindrome(s, i - curr_len - 1, i):
                res = s[i - curr_len - 1: i + 1]
                curr_len += 2
            elif self.isPalindrome(s, i - curr_len, i):
                res = s[i - curr_len : i + 1]
                curr_len += 1
        return res


class Solution2:
    """
    通过从中间向两边查找，判断是否是回文数，时间复杂度：O(n^2)
    """
    start, end  = 0, 0
    def extendsPalindrome(self, s, j, k,):
        while j >= 0 and k < len(s) and s[j] == s[k]:
            j -= 1
            k += 1
        return k - j - 1

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        if length < 2:
            return s
        for i in range(length):
            # 如果是奇数长度
            len1 = self.extendsPalindrome(s, i, i)
            # 如果是偶数长度
            len2 = self.extendsPalindrome(s, i, i + 1)
            max_len = max(len1, len2)
            if max_len > self.end - self.start:
                self.start = i - (max_len - 1) // 2
                self.end = i + (max_len) // 2
        return s[self.start : self.end + 1]


class Solution3:
    """
    Manacher's algorithm  Time complexity:O(n)
    """
    def preprocess(self, s):
        length = len(s)
        if length == 0:
            return "^$"
        ret = "^"
        for i in range(length):
            ret += "#" + s[i]
        ret += "#$"
        return ret

    def longestPalindrome(self, s):
        if len(s) < 2:
            return s
        t = self.preprocess(s)
        n = len(t)
        p = [0 for i in range(n)]
        C, R = 0, 0
        for i in range(1, n - 1):
            # 等于i' = C - (i - C)
            i_mirror = 2 * C - i

            # 最核心的算法思想
            if R > i:
                p[i] = min(R - i, p[i_mirror])
            else:
                p[i] = 0

            while t[i + 1 + p[i]] == t[i - 1 - p[i]]:
                p[i] += 1

            # 如果以i为中心的回文串扩展超过R,基于扩展的回文串扩展调整中心位置
            if i + p[i] > R:
                C, R = i, i + p[i]

        max_len = 0
        center_index = 0
        for i in range(1, n - 1):
            if p[i] > max_len:
                max_len = p[i]
                center_index = i
        start = (center_index - max_len) // 2
        end = start + max_len
        # print(start, max_len)
        return s[start:end]

# a = Solution3()
# print(a.longestPalindrome("bb"))
