# -*- coding: utf-8 -*-

# !/usr/bin/env python

# Time: 2018/9/8 10:49

# Author: sty

# File: 145. Binary Tree Postorder Traversal.py


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        nodes = []
        to_visit = []
        cur = root
        last_node = None
        while cur or len(to_visit) != 0:
            if cur:
                to_visit.append(cur)
                cur = cur.left
            else:
                top_node = to_visit[-1]
                if top_node.right and last_node != top_node.right:
                    cur = top_node.right
                else:
                    nodes.append(top_node.val)
                    last_node = top_node
                    to_visit.pop()
        return nodes

