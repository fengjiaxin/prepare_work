# 给你一个链表数组，每个链表都已经按升序排列。
#
# 请你将所有链表合并到一个升序链表中，返回合并后的链表。
#
#  
#
# 示例 1：

# 输入：lists = [[1,4,5],[1,3,4],[2,6]]
# 输出：[1,1,2,3,4,4,5,6]
# 解释：链表数组如下：
# [
#     1->4->5,
#           1->3->4,
#                 2->6
# ]
# 将它们合并到一个有序链表中得到。
# 1->1->2->3->4->4->5->6


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        def mergeTwo(a,b):
            if a is None:
                return b
            if b is None:
                return a
            if a.val < b.val:
                a.next = mergeTwo(a.next,b)
                return a
            else:
                b.next = mergeTwo(a,b.next)
                return b
        def merge_helper(lists):
            length = len(lists)
            if length == 0:
                return None
            if length == 1:
                return lists[0]
            if length == 2:
                return mergeTwo(lists[0],lists[1])
            else:
                mid = length//2
                left_arr = lists[:mid+1]
                right_arr = lists[mid+1:]
                left_start = merge_helper(left_arr)
                right_start = merge_helper(right_arr)
                return mergeTwo(left_start,right_start)
        return merge_helper(lists)

