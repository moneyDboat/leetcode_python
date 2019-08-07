# -*- coding: utf-8 -*-

"""
@Author  : captain
@time    : 2019-07-20 15:44
@ide     : PyCharm  
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        pre_node, tmp_node = None, head
        while tmp_node:
            next_node = tmp_node.next
            tmp_node.next = pre_node
            pre_node, tmp_node = tmp_node, next_node
        return pre_node
