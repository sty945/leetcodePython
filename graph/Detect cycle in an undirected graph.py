# -*- coding: utf-8 -*-

# !/usr/bin/env python

# Time: 2018/5/27 19:57

# Author: sty

# File: Detect cycle in an undirected graph.py

from collections import defaultdict


# 建图
def create_graph(e, arr, graph):
    i = 0
    while i < 2 * e:
        graph[arr[i]].append(arr[i + 1])
        graph[arr[i + 1]].append(arr[i])
        i += 2


def is_cyclic_util(v, visited, parent, graph):
    """
    对于每一个被访问的节点v,如果有一个相邻节点u已经被访问，
    但是u又不是v的父节点，那么图中一定有环
    :param v:
    :param visited:
    :param parent:
    :param graph:
    :return:
    """
    visited[v] = True
    for i in graph[v]:
        if visited[i] is False:
            if is_cyclic_util(i, visited, v, graph):
                return True
        elif i != parent:
            return True
    return False


def is_cyclic(n, graph):
    visited = [False] * n
    for i in range(n):
        if visited[i] is False:
            if is_cyclic_util(i, visited, -1, graph) is True:
                return True
    return False


if __name__ == '__main__':
    t = int(input())
    for ti in range(1, t + 1):
        # n 表示有n个节点，e表示有e个边
        n, e = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        graph = defaultdict(list)
        create_graph(e, arr, graph)
        if is_cyclic(n, graph):
            print("yes")
        else:
            print("No")



"""
Input:
2
2 2
0 1 0 0
4 3
0 1 1 2 2 3

Output:
1
0
"""
