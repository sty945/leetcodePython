# !/usr/bin/env python

# -*- coding: utf-8 -*-

# Time: 2018/1/23 19:49

# Author: sty

# File: 404. Sum of Left Leaves.py

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ret = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                if node.left:
                    if node.left.left == None and node.left.right == None:
                        ret += node.left.val
                stack.append(node.right)
                stack.append(node.left)
        return ret



