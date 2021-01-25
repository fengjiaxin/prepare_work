# 删除链表中等于给定值 val 的所有节点。
#
# 示例:
#
# 输入: 1->2->6->3->4->5->6, val = 6
# 输出: 1->2->3->4->5

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        preNode = ListNode(0)
        preNode.next = head

        pre = preNode
        while head:
            if head.val == val:
                pre.next = head.next
                head = pre.next
            else:
                pre = head
                head = head.next
        return preNode.next