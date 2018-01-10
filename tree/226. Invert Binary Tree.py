# !/usr/bin/env python

# -*- coding: utf-8 -*-

# Time: 2018/1/8 23:17

# Author: sty

# File: 226. Invert Binary Tree.py

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        root.left , root.right = root.right, root.left;
        self.invertTree(root.left)
        self.invertTree(root.right)