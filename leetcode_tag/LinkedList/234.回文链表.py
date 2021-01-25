# 请判断一个链表是否为回文链表。
#
# 示例 1:
#
# 输入: 1->2
# 输出: false
# 示例 2:
#
# 输入: 1->2->2->1
# 输出: true

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return True
        slow = head
        fast = head
        p = None
        while fast and fast.next:
            p = slow
            slow = slow.next
            fast = fast.next.next
        if fast:
            p = slow
            slow = slow.next
        def reverse(node):
            if node is None or node.next is None:
                return node
            res = reverse(node.next)
            node.next.next = node
            node.next = None
            return res
        left = head

        right = reverse(slow)
        q = right

        flag = True
        while right:
            if left.val != right.val:
                flag = False
                break
            else:
                left = left.next
                right = right.next

        p.next = reverse(q)
        return flag
