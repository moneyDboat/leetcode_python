# -*- coding: utf-8 -*-

"""
@Author  : captain
@time    : 2019-08-06 21:23
@ide     : PyCharm  
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        # 关键在于fake_head
        fake_head, cur_node = ListNode(0), head
        pre_node = fake_head
        fake_head.next = head
        while cur_node:
            if cur_node.val == val:
                pre_node.next = cur_node.next
                cur_node = pre_node.next
            else:
                pre_node = cur_node
                cur_node = cur_node.next

        return fake_head.next
