# -*- coding: utf-8 -*-

"""
@Author  : captain
@time    : 2019-07-20 15:55
@ide     : PyCharm  
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow_node, quick_node = head, head
        while quick_node and quick_node.next:
            quick_node = quick_node.next.next
            slow_node = slow_node.next
        return slow_node
