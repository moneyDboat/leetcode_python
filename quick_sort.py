# -*- coding: utf-8 -*-

"""
@Author  : captain
@time    : 2019-10-07 20:29
@ide     : PyCharm  
"""


def quick_sort(lst):
    if not lst:
        return []
    pivot = lst[0]
    left = quick_sort([x for x in lst[1:] if x < pivot])
    right = quick_sort([x for x in lst[1:] if x >= pivot])
    return left + [pivot] + right


if __name__ == '__main__':
    test_case = [7, 6, 9, 0, 5, 8, 4, 2, 3, 1]
    print(test_case)
    print(quick_sort(test_case))
