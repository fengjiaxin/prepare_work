# 给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
#
# 进阶：你能尝试使用一趟扫描实现吗？
#
# 输入：head = [1,2,3,4,5], n = 2
# 输出：[1,2,3,5]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        prevNode = ListNode(0)
        prevNode.next = head
        slow = prevNode
        fast = prevNode
        for i in range(n):
            fast = fast.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return prevNode.next