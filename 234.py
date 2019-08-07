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
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow_node, quick_node = head, head
        while quick_node:
            slow_node = slow_node.next
            quick_node = quick_next.next.next if quick_node.next else quick_node.next
        pre_node = None
        while slow_node:
            slow_node.next, slow_node, pre_node = pre_node, slow_node.next, slow_node

        while head and pre_node:
            if head.val != pre_node.val:
                return False
            head, pre_node = head.next, pre_node.next
        return True
