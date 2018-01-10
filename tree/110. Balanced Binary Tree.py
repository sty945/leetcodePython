# !/usr/bin/env python

# -*- coding: utf-8 -*-

# Time: 2018/1/10 21:13

# Author: sty

# File: 110. Balanced Binary Tree.py

# description:
# 判断是否是平衡二叉树
# judge is Balanced Binary Tree or not

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    '''
    1.first method:the top down approach
    For the current node root, calling depth() for its left and right children actually
    has to access all of its children, thus the complexity is O(N).
    We do this for each node in the tree, so the overall complexity of isBalanced will be O(N^2)

    '''
    def depth(self, root):
        if not root:
            return 0;
        return max(self.depth(root.left), self.depth(root.right)) + 1;

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        left_depth = self.depth(root.left)
        right_depth = self.depth(root.right)
        if abs(left_depth - right_depth) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        return False


class Solution2:
    '''
    2.second method:the bottom up way
    It is based on DFS,
    Instead of calling depth() explicitly for each child node,
     we return the height of the current node in DFS recursion.
     When the sub tree of the current node (inclusive) is balanced,
     the function height_judge() returns a non-negative value as the height.
     Otherwise -1 is returned. According to the leftHeight and rightHeight of the two children,
     the parent node could check if the sub tree is balanced, and decides its return value.
    '''
    def height_judge(self, root):
        if not root:
            return 0
        left_height = self.height_judge(root.left)
        if left_height == -1:
            return -1
        right_height = self.height_judge(root.right)
        if right_height == -1:
            return -1
        if abs(left_height - right_height) > 1:
            return -1
        return 1 + max(left_height, right_height)

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if self.height_judge(root) == -1:
            return False
        else:
            return True