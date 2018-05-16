# -*- coding: utf-8 -*-

# !/usr/bin/env python

# Time: 2018/5/14 23:23

# Author: sty

# File: 2. Add Two Numbers.py

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        root = res_list = ListNode(0)
        num1, num2 = 0, 0
        i = 0
        while l1 is not None:
            num1 += l1.val * pow(10, i)
            i += 1
            l1 = l1.next
        i = 0
        while l2 is not None:
            num2 += l2.val* pow(10, i)
            i += 1
            l2 = l2.next
        res = num1 + num2
        if res == 0:
            return root
        while res != 0:
            # res_list.append(res % 10)
            res_list.next = ListNode(res % 10)
            res_list = res_list.next
            res //= 10
        return root.next
