# !/usr/bin/env python

# -*- coding: utf-8 -*-

# Time: 2018/1/6 23:05

# Author: sty

# File: 102. Binary Tree Level Order Traversal.py

class Solution:
    def levelOrder(self, root):
        """
        普通二叉树层次遍历，并输出
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res, level = [], [root]
        while root and level:
            currentNode = []
            nextLevel = []
            for node in level:
                currentNode.append(node.val)
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            res.append(currentNode)
            level = nextLevel
        return res
