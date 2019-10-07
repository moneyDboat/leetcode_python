# -*- coding: utf-8 -*-

"""
@Author  : captain
@time    : 2019-08-11 15:24
@ide     : PyCharm
"""


# Python实现二叉树的递归非递归遍历
# https://blog.yangx.site/2016/07/22/Python-binary-tree-traverse/，这篇博文里有详细的注解
class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


# 前序遍历递归写法
def pre_order_recur(root):
    if not root:
        return []
    res = []
    res.append(root.val)
    res += pre_order_recur(root.left)
    res += pre_order_recur(root.right)
    return res


# 中序遍历递归写法
def in_order_recur(root):
    if not root:
        return []
    res = []
    res += in_order_recur(root.left)
    res.append(root.val)
    res += in_order_recur(root.right)
    return res


# 后序遍历递归写法
def post_order_recur(root):
    if not root:
        return []
    res = []
    res += post_order_recur(root.left)
    res += post_order_recur(root.right)
    res.append(root.val)
    return res


# 前序遍历非递归循环特有简洁写法
def pre_order_cycle1(root):
    if not root:
        return []
    res, stack = [], [root]
    while stack:
        node = stack.pop()
        res.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return res


# 前序非递归循环常规写法
def pre_order_cycle2(root):
    if not root:
        return []
    res, stack, node = [], [], root
    while node or stack:
        while node:
            stack.append(node)
            res.append(node.val)
            node = node.left
        node = stack.pop()
        node = node.right

    return res


# 中序非递归循环写法
def in_order_cycle(root):
    if not root:
        return []
    res, stack, node = [], [], root
    while node or stack:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        res.append(node.val)
        node = node.right

    return res


# 后序遍历非递归循环写法
def post_order_cycle(root):
    if not root:
        return []
    res, stack1, stack2, node = [], [], [], root
    stack1.append(root)
    while stack1:
        node = stack1.pop()
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)
        stack2.append(node)
    while stack2:
        res.append(stack2.pop().val)

    return res


# 层序遍历
def level_order(root):
    if not root:
        return []
    res, queue = [], [root]
    while queue:
        cur_queue = queue
        queue = []
        for node in cur_queue:
            res.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return res


class Solution:
    def increasingBST(self, root: Node) -> Node:
        stack = []
        fake_root = Node(0, None, None)
        node, res_node = root, fake_root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            res_node.left, res_node.right = None, node
            res_node = res_node.right
            node = node.right

        return fake_root.right


if __name__ == '__main__':
    left_node = Node(2, Node(4, None, None), Node(5, None, None))
    right_node = Node(3, None, Node(6, None, None))
    root = Node(1, left_node, right_node)

    # 标准答案：
    # [1, 2, 4, 5, 3, 6]
    # [4, 2, 5, 1, 3, 6]
    # [4, 5, 2, 6, 3, 1]
    # [1, 2, 3, 4, 5, 6]
    print('前序遍历结果：')
    print(pre_order_recur(root))
    print(pre_order_cycle1(root))
    print(pre_order_cycle2(root))
    print('中序遍历结果：')
    print(in_order_recur(root))
    print(in_order_cycle(root))
    print('后序遍历结果：')
    print(post_order_recur(root))
    print(post_order_cycle(root))
    print('层次遍历结果：')
    print(level_order(root))

    root = Node(379, Node(826, None, None), None)
    solution = Solution()
    res = solution.increasingBST(root)
    in_order_recur(res)
