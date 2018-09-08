# -*- coding: utf-8 -*-

# !/usr/bin/env python

# Time: 2018/9/7 16:05

# Author: sty

# File: 25 FindPath.py


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        """
        非递归做法
        :param root:
        :param expectNumber:
        :return:
        """
        to_visit = []
        cur = root
        last_node = None
        res, path = [], []
        while cur or len(to_visit) != 0:
            if cur:
                to_visit.append(cur)
                path.append(cur.val)
                cur = cur.left
            else:
                top_node = to_visit[-1]
                if top_node.right and last_node != top_node.right:
                    cur = top_node.right
                else:
                    if sum(path) == expectNumber and top_node.left is None and top_node.right is None:
                        res.append([value for value in path])
                    to_visit.pop()
                    path.pop()
                    last_node = top_node
        return res

    def FindPath1(self, root, expectNumber):
        """
        递归做法
        :param root:
        :param expectNumber:
        :return:
        """
        res = []
        if root is None:
            return res

        def find_path_main(root, path, expectNumber):
            if root is None:
                return
            path.append(root.val)
            expectNumber -= root.val
            if expectNumber == 0 and root.left is None and root.right is None:
                res.append([value for value in path])
            find_path_main(root.left, path, expectNumber)
            find_path_main(root.right, path, expectNumber)
            path.pop()
            return

        find_path_main(root, [], expectNumber)
        return res





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

values = [10,5,12,4,7]
print(values)
root = list_to_treenode(values)
print(Solution().FindPath1(root, 22))