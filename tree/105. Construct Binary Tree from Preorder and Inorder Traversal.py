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

    def buildTree1(self, preorder, inorder):
        """
        优化算法：https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/discuss/34543/Simple-O(n)-without-map
        :param preorder:
        :param inorder:
        :return:
        """
        def build(stop):
            if inorder and inorder[-1] != stop:
                root = TreeNode(preorder.pop())
                root.left = build(root.val)
                inorder.pop()
                root.right = build(stop)
                return root

        preorder.reverse()
        inorder.reverse()
        return build(None)

    def buildTree2(self, preorder, inorder):
        if len(preorder) == 0:
            return None
        i, j = 1, 0
        root = TreeNode(preorder[0])
        stack = [root]
        while i < len(preorder):
            node = TreeNode(preorder[i])
            tmp = None
            while stack and stack[-1].val == inorder[j]:
                tmp = stack.pop()
                j += 1
            if tmp:
                tmp.right = node
            else:
                stack[-1].left = node
            stack.append(node)
            i += 1
        return root
