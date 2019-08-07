# -*- coding: utf-8 -*-

"""
@Author  : captain
@time    : 2019-07-20 20:15
@ide     : PyCharm  
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        len_headA, len_headB = 0, 0
        cur_nodeA, cur_nodeB = headA, headB
        while cur_nodeA:
            len_headA += 1
            cur_nodeA = cur_nodeA.next
        while cur_nodeB:
            len_headB += 1
            cur_nodeB = cur_nodeB.next

        # 计算出两个链表的长度差，然后用前后指针
        if len_headA < len_headB:
            len_headA, len_headB = len_headB, len_headA
            headA, headB = headB, headA
        len_diff = len_headA - len_headB
        cur_nodeA, cur_nodeB = headA, headB
        for i in range(len_diff):
            cur_nodeA = cur_nodeA.next
        while cur_nodeA and cur_nodeB and cur_nodeA != cur_nodeB:
            cur_nodeA, cur_nodeB = cur_nodeA.next, cur_nodeB.next
        if not cur_nodeA or not cur_nodeB:
            return None
        else:
            return cur_nodeA
