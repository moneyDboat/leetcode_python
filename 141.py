# -*- coding: utf-8 -*-

"""
@Author  : captain
@time    : 2019-08-06 21:30
@ide     : PyCharm  
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        slow_node, quick_node = head, head
        while quick_node.next and quick_node.next.next:
            quick_node = quick_node.next.next
            slow_node = slow_node.next
            if quick_node.val == slow_node.val:
                return True

        return False
