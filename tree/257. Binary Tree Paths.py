# !/usr/bin/env python

# -*- coding: utf-8 -*-

# Time: 2018/1/14 22:16

# Author: sty

# File: 257. Binary Tree Paths.py

# Definition for a binary tree node.



class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    '''
    record every node, when you reach the leaf node, add leaf node to the list
    '''
    def travel(self, root, path, answer):
        # leaf node
        if root.left == None and root.right == None:
            answer.append(path + str(root.val))
        if root.left != None:
            self.travel(root.left, path + str(root.val) + '->', answer)
        if root.right != None:
            self.travel(root.right, path + str(root.val) + '->', answer)


    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        answer = []
        if root:
            self.travel(root, '', answer)
        return answer




