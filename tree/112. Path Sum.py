# !/usr/bin/env python

# -*- coding: utf-8 -*-

# Time: 2018/1/13 21:42

# Author: sty

# File: 112. Path Sum.py

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        Given a binary tree and a sum,
        determine if the tree has a root-to-leaf path
        such that adding up all the values along the path equals the given sum.
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False

        if not root.left and not root.right and root.val == sum:
            return True

        # minus the val every travel times
        sum -= root.val

        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)

