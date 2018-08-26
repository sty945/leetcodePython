# -*- coding: utf-8 -*-

# !/usr/bin/env python

# Time: 2018/8/26 15:06

# Author: sty

# File: 106. Construct Binary Tree from Inorder and Postorder Traversal.py


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            idx = inorder.index(postorder.pop())
            root = TreeNode(inorder[idx])
            root.right = self.buildTree(inorder[idx+1:], postorder)
            root.left = self.buildTree(inorder[:idx], postorder)
            return root

    def buildTree1(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        length = len(postorder)
        if length == 0:
            return None
        i, j = length - 2, length - 1
        root = TreeNode(postorder[length-1])
        stack = [root]
        while i >=0:
            node = TreeNode(postorder[i])
            tmp = None
            while stack and stack[-1].val == inorder[j]:
                tmp = stack.pop()
                j -= 1
            if tmp:
                tmp.left = node
            else:
                stack[-1].right = node
            stack.append(node)
            i -= 1
        return root