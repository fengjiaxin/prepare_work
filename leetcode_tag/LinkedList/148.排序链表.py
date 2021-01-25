# 给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。
#
# 进阶：
#
# 你可以在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # 如果是数组的话，采用归并方法
        # 合并两个有序的链表
        if head is None or head.next is None:
            return head


        def merge(a,b):
            if a is None:
                return b
            if b is None:
                return a
            if a.val < b.val:
                a.next = merge(a.next,b)
                return a
            else:
                b.next = merge(a,b.next)
                return b

        def helper(node):
            if node is None or node.next is None:
                return node
            # 找出中间节点
            slow = node
            fast = node
            while fast and fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            right_start = slow.next
            slow.next = None
            left_start = node

            # 分别对左右节点排序
            new_left = helper(left_start)
            new_right = helper(right_start)
            return merge(new_left,new_right)
        return helper(head)

