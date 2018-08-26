# -*- coding: utf-8 -*-

# !/usr/bin/env python

# Time: 2018/8/21 16:44

# Author: sty

# File: tree_operate_python.py

import sys


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                ret.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return ret


def list_to_treenode(input_values):
    if not input_values:
        return None
    root = TreeNode(int(input_values[0]))
    node_queue = [root]
    front = 0
    index = 1
    while index < len(input_values):
        node = node_queue[front]
        front += 1

        item = input_values[index]
        index += 1

        if item != "null":
            left_num = int(item)
            node.left = TreeNode(left_num)
            node_queue.append(node.left)

        if index >= len(input_values):
            break

        item = input_values[index]
        index += 1
        if item != "null":
            right_num = int(item)
            node.right = TreeNode(right_num)
            node_queue.append(node.right)
    return root


def main():
    line = sys.stdin.readline().strip()
    values = list(map(str, line.split()))
    root = list_to_treenode(values)
    pret = Solution().preorderTraversal(root)
    print(pret)


if __name__ == '__main__':
    main()


"""
input:
3 9 20 null null 15 7
output:
[3, 9, 20, 15, 7]
"""