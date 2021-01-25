# 给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
# 将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…
#
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
#
# 示例 1:
#
# 给定链表 1->2->3->4, 重新排列为 1->4->2->3.
# 示例 2:
#
# 给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # 有意思了，可以这么来
        # 1 - 2 - 3 - 4 - 5 =》 1 - 5- 4 -3 -2 =》 1 - 5 - 2 -3 -4 =？ 1 - 5 - 2 - 4 -3
        if head is None or head.next is None:
            return head

        def reverse(node):
            if node is None or node.next is None:
                return node
            last = reverse(node.next)
            node.next.next = node
            node.next = None
            return last


        # curr = head
        # while curr.next:
        #     curr.next = reverse(curr.next)
        #     curr = curr.next


        # 可以换个思路啊，1 - 2 - 3 ， 4 - 5 然后reverse(4) = 5 ,4,在重新merge
        slow = head
        preSlow = None
        fast = head
        while fast and fast.next:
            preSlow = slow
            slow = slow.next
            fast = fast.next.next

        if fast:
            preSlow = slow
            slow = slow.next
        preSlow.next = None
        newHead = reverse(slow)
        slow.next = None

        # 加下来是合并两个链表
        left = head
        right = newHead


        next_left = None
        next_right = None

        while right:
            next_left = left.next
            next_right = right.next
            left.next = right
            right.next = next_left
            left = next_left
            right = next_right



