# 反转一个单链表。
#
# 示例:
#
# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        # 返回反转node之后节点的新节点
        def helper(node):
            if node is None or node.next is None:
                return node
            res = helper(node.next)
            node.next.next = node
            node.next = None
            return res
        return helper(head)