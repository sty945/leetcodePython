# !/usr/bin/env python

# -*- coding: utf-8 -*-

# Time: 2018/1/6 23:06

# Author: sty

# File: 107. Binary Tree Level Order Traversal II.py

class Solution:
    def levelOrderBottom(self, root):
        """
        普通的二叉树的层次遍历，但是需要逆序输出
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res, level = [],[root]
        while level:
            currentNode = []
            nextLevel = []
            for node in level:
                currentNode.append(node.val)
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            res.insert(0, currentNode)   # 每次都给插入到列表的头部
            level = nextLevel
        return res