# 给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
#
# 输入: 1->1->2->3->3
# 输出: 1->2->3

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        slow = head
        fast = head.next
        while fast:
            if fast.val == slow.val:
                fast = fast.next
            else:
                slow.next = fast
                slow = slow.next
                fast = fast.next
        slow.next = None
        return head
        return head