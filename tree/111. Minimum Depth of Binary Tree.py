# !/usr/bin/env python

# -*- coding: utf-8 -*-

# Time: 2018/1/13 20:50

# Author: sty

# File: 111. Minimum Depth of Binary Tree.py

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root):
        """
        if root have left and right children, we count min depth value between
        left and right children,
        else root's depth must left or right children's depth + 1,
        one of left or right children's depth is 0,
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if root.left and root.right:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        else:
            return self.minDepth(root.left) + self.minDepth(root.right) + 1