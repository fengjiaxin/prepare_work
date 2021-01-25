# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
#
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

# 递归实现
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head):
        # 应该是一个递归
        # 交换两个节点，返回交换后的节点
        def helper(node):
            if node is None or node.next is None:
                return node
            # 交换两个节点
            curr = node
            next_curr = node.next
            next2_curr = next_curr.next
            next_curr.next = curr
            curr.next = helper(next2_curr)
            return next_curr
        return helper(head)
