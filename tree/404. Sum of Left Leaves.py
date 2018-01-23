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
        ret = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                # 左孩子非空
                if node.left:
                    # 左孩子为叶子节点
                    if node.left.left == None and node.left.right == None:
                        ret.append(node.left.val)
                stack.append(node.right)
                stack.append(node.left)
        return sum(ret)



