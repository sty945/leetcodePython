# !/usr/bin/env python

# -*- coding: utf-8 -*-

# Time: 2018/1/14 20:46

# Author: sty

# File: 235. Lowest Common Ancestor of a Binary Search Tree.py

# Definition for a binary tree root.
# description: if p,q in node t's different sides,t is the LCA)

class Treeroot(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1(object):
    '''
    this is my first method, travel the tree to search the p,q,the compare their pre nodes,
    this method Time complexity is O(n), and not clear
    '''
    def getRes(self, root, p):
        res = []
        while root:
            if p.val > root.val:
                res.append(root.val)
                root = root.right
            elif p.val < root.val:
                res.append(root.val)
                root = root.left
            else:
                res.append(root.val)
                break
        return res

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: Treeroot
        :type p: Treeroot
        :type q: Treeroot
        :rtype: Treeroot
        """
        res = []
        res1 = self.getRes(root, p)
        res2 = self.getRes(root, q)
        length = min(len(res1), len(res2))
        for i in range(0, length):
            if res1[i] == res2[i]:
                res.append(res1[i])
            else:
                break
        return res[-1]

class Solution2(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        this method is easy to understand
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        while root:
            if min(p.val, q.val) > root.val:
                root = root.right
            elif max(p.val, q.val) < root.val:
                root = root.left
            else:
                return root
        return None

class Solution2(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        this method is easy to understand
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        while root:
            if p.val > root.val and q.val > root.val:
                return self.lowestCommonAncestor(root.right)
            elif p.val < root.val and q.val < root.val:
                return self.lowestCommonAncestor(root.left)
            else:
                return root


