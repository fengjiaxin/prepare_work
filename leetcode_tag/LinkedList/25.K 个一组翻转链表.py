# 给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
#
# k 是一个正整数，它的值小于或等于链表的长度。
#
# 如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
#
#  
#
# 示例：
#
# 给你这个链表：1->2->3->4->5
#
# 当 k = 2 时，应当返回: 2->1->4->3->5
#
# 当 k = 3 时，应当返回: 3->2->1->4->5

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # 想一下，首先需要反转链表，反转[a,b)的链表
        def reverse(start,end):
            if start is None or start.next is None:
                return start
            pre = None
            curr = start
            nextNode = None
            while curr != end:
                nextNode = curr.next
                curr.next = pre
                pre = curr
                curr = nextNode
            return pre

        def helper(head,k):
            pre = None
            curr = head
            for i in range(k):
                if curr is None:
                    return head
                pre = curr
                curr = curr.next
            end = curr
            new_start = reverse(head,end)
            head.next = helper(end,k)
            return new_start
        return helper(head,k)
