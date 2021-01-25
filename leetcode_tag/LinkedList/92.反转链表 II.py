# 反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。
#
# 说明:
# 1 ≤ m ≤ n ≤ 链表长度。
#
# 示例:
#
# 输入: 1->2->3->4->5->NULL, m = 2, n = 4
# 输出: 1->4->3->2->5->NULL

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        # 反转,长度为length
        def helper(startNode,length):
            if startNode is None:
                return startNode
            pre = None
            curr = startNode
            nextNode = None
            while length > 0:
                nextNode = curr.next
                curr.next = pre
                pre = curr
                curr = nextNode
                length -= 1
            startNode.next = curr
            return pre
        if m == 1:
            return helper(head,n-m+1)
        else:
            pre_node = head
            for i in range(m -2):
                pre_node = pre_node.next
            pre_node.next = helper(pre_node.next,n-m+1)
            return head