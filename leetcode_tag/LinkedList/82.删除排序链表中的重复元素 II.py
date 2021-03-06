# 给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。
#
# 示例 1:
#
# 输入: 1->2->3->3->4->4->5
# 输出: 1->2->5
# 示例 2:
#
# 输入: 1->1->1->2->3
# 输出: 2->3

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        def helper(node):
            if node is None or node.next is None:
                return node
            if node.val == node.next.val:
                while node.next and node.val == node.next.val:
                    node = node.next
                return helper(node.next)
            else:
                node.next = helper(node.next)
                return node
        return helper(head)