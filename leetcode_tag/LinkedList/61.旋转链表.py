# 给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。
#
# 示例 1:
#
# 输入: 1->2->3->4->5->NULL, k = 2
# 输出: 4->5->1->2->3->NULL
# 解释:
# 向右旋转 1 步: 5->1->2->3->4->NULL
# 向右旋转 2 步: 4->5->1->2->3->NULL
# 示例 2:
#
# 输入: 0->1->2->NULL, k = 4
# 输出: 2->0->1->NULL
# 解释:
# 向右旋转 1 步: 2->0->1->NULL
# 向右旋转 2 步: 1->2->0->NULL
# 向右旋转 3 步: 0->1->2->NULL
# 向右旋转 4 步: 2->0->1->NULL
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # k 小于node的长度
        def getLen(node):
            res = 0
            while node:
                res += 1
                node = node.next
            return res
        def helper(node,k):
            pre = None
            curr = node
            for i in range(k):
                pre = curr
                curr = curr.next
            pre.next = None
            res = curr
            while curr.next:
                curr = curr.next
            curr.next = node
            return res
        if head is None or head.next is None:
            return head
        length = getLen(head)
        # print(length)
        k = k % length
        if k == 0:
            return head
        else:
            return helper(head,length - k)
        