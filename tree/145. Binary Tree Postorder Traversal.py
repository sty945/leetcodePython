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
        # to_visit是存储结点的栈
        to_visit = []
        cur = root
        last_node = None
        # 如果当前结点或者要遍历的结点不为空就持续遍历
        while cur or len(to_visit) != 0:
            # 一直访问左子树，直至为空
            if cur:
                to_visit.append(cur)
                cur = cur.left
            else:
                # 取到栈中最顶部的结点，然后判断是否有右结点并且右结点是否已经访问过
                top_node = to_visit[-1]
                if top_node.right and last_node != top_node.right:
                    cur = top_node.right
                else:
                    # 访问结点，并且将last_node记录为当前访问的结点
                    nodes.append(top_node.val)
                    last_node = top_node
                    to_visit.pop()
        return nodes

