# 给你一个链表和一个特定值 x ，请你对链表进行分隔，使得所有小于 x 的节点都出现在大于或等于 x 的节点之前。
#
# 你应当保留两个分区中每个节点的初始相对位置。
#
#  
#
# 示例：
#
# 输入：head = 1->4->3->2->5->2, x = 3
# 输出：1->2->2->4->3->5

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        preLeft = ListNode()
        preRight = ListNode()

        left_curr = preLeft
        right_curr = preRight

        while head:
            if head.val < x:
                left_curr.next = head
                left_curr = left_curr.next
            else:
                right_curr.next = head
                right_curr = right_curr.next
            head = head.next
        right_curr.next = None
        left_curr.next = preRight.next

        return preLeft.next