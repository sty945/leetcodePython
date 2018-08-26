# -*- coding: utf-8 -*-

# !/usr/bin/env python

# Time: 2018/8/21 16:40

# Author: sty

# File: 104. Maximum Depth of Binary Tree.py


class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        else:
            return max(self.maxDepth(root.left)+1, self.maxDepth(root.right)+1)