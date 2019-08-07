# -*- coding: utf-8 -*-

"""
@Author  : captain
@time    : 2019-07-20 16:20
@ide     : PyCharm  
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None
        cur_node = head
        while cur_node.next:
            if cur_node.val == cur_node.next.val:
                cur_node.next = cur_node.next.next
            else:
                cur_node = cur_node.next
        return head
