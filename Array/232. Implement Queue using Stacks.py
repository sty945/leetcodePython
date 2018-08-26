# -*- coding: utf-8 -*-

# !/usr/bin/env python

# Time: 2018/8/26 16:40

# Author: sty

# File: 232. Implement Queue using Stacks.py


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.stack1.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if len(self.stack1) == 0 and len(self.stack2) == 0:
            return None
        else:
            if len(self.stack2) == 0:
                while len(self.stack1) != 1:
                    self.stack2.append(self.stack1.pop())
                return self.stack1.pop()
            else:
                return self.stack2.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if len(self.stack2) == 0 and len(self.stack1) == 0:
            return None
        else:
            if len(self.stack2) == 0:
                return self.stack1[0]
            else:
                return self.stack2[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if len(self.stack1) == 0 and len(self.stack2) == 0:
            return True
        else:
            return False
