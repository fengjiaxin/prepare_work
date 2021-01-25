# 给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
#
# 请你将两个数相加，并以相同形式返回一个表示和的链表。
#
# 你可以假设除了数字 0 之外，这两个数都不会以 0 开头。


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        flag = 0
        preHead = ListNode(0)
        preNode = preHead
        while l1 and l2:
            res = flag + l1.val + l2.val
            preNode.next = ListNode(res%10)
            flag = res//10
            preNode = preNode.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            res = flag + l1.val
            preNode.next = ListNode(res%10)
            flag = res//10
            preNode = preNode.next
            l1 = l1.next
        while l2:
            res = flag + l2.val
            preNode.next = ListNode(res%10)
            flag = res//10
            preNode = preNode.next
            l2 = l2.next
        if flag:
            preNode.next = ListNode(flag)
        return preHead.next

            