# 输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
# 输出：Reference of the node with value = 8
# 输入解释：相交节点的值为 8 （注意，如果两个链表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        def getLength(node):
            res = 0
            while node:
                res += 1
                node = node.next
            return res
        length_a = getLength(headA)
        length_b = getLength(headB)

        # 默认a比b短，相差minus
        def getInter(headA,headB,minus):
            for i in range(minus):
                headB = headB.next
            while headA != headB:
                headA = headA.next
                headB = headB.next
            return headA
        if length_a < length_b:
            return getInter(headA,headB,length_b - length_a)
        else:
            return getInter(headB,headA,length_a - length_b)