# -*- coding: utf-8 -*-

# !/usr/bin/env python

# Time: 2018/6/27 23:44

# Author: sty

# File: 19. Remove Nth Node From End of List.py
import json

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        res = ListNode(None)
        res.next = head
        cur = runner = res

        for _ in range(n):
            runner = runner.next

        while runner.next is not None:
            cur = cur.next
            runner = runner.next

        cur.next = cur.next.next

        return res.next

def stringToIntegerList(input):
    return json.loads(input)

def stringToListNode(input):
    # Generate list from the input
    numbers = stringToIntegerList(input)
    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr

def listNodeToString(node):
    if not node:
        return "[]"
    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            head = stringToListNode(line);
            line = next(lines)
            n = int(line);
            ret = Solution().removeNthFromEnd(head, n)
            out = listNodeToString(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()