# -*- coding: utf-8 -*-

# !/usr/bin/env python

# Time: 2018/8/26 11:24

# Author: sty

# File: 105. Construct Binary Tree from Preorder and Inorder Traversal.py

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        def build(preorder, inorder):
            if inorder:
                ind = inorder.index(preorder.pop())
                root = TreeNode(inorder[ind])
                root.left = build(preorder, inorder[ind+1:])
                root.right = build(preorder, inorder[:ind])
                return root
        preorder.reverse()
        inorder.reverse()
        return build(preorder, inorder)
