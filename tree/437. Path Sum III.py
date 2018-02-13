# !/usr/bin/env python

# -*- coding: utf-8 -*-

# Time: 2018/1/25 20:06

# Author: sty

# File: 437. Path Sum III.py

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1:
    '''
    Brute Force Solution:traverse each node (preorder traversal) and
    then find all paths which sum to the target using this node as root.
    good
    '''
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0
        return self.pathSumFrom(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)

    def pathSumFrom(self,node, sum):
        if not node:
            return 0
        return (1 if node.val == sum else 0) + self.pathSumFrom(node.left, sum - node.val) + self.pathSumFrom(node.right,sum - node.val)


class Solution:
    '''
    Two Sum Method: Optimized Solution
    '''
    def pathSum(self, root, target):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        dic = {0: 1}  # 保存从根节点到当前节点路径的和
        self.res = 0
        self.find_path(root, target, 0, dic)
        return self.res

    def find_path(self, root, target, cur_sum, dic):
        if not root:
            return
        # if
        cur_sum += root.val  # 从根节点到当前节点路径的和
        self.res += dic.get(cur_sum - target, 0)  # 减去target，若在dic中出现过，表明当前路径中有子路径和为target
        if cur_sum in dic:  # 把cur_sum加入到dic中
            dic[cur_sum] += 1
        else:
            dic[cur_sum] = 1
        self.find_path(root.left, target, cur_sum, dic)
        self.find_path(root.right, target, cur_sum, dic)
        dic[cur_sum] -= 1  # ！！！左右子树都遍历完后，要把这条路径的和删掉
        return