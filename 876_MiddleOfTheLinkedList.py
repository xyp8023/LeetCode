# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# from math import floor
# class Solution:
#     def middleNode(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
#         List = []
#         head_ = head
#         while head_ != None:
#             List.append(head_.val)
#             head_ = head_.next
#
#         N = floor(len(List) / 2)
#         for i in range(N):
#             head = head.next
#         return head


# another solution
class Solution:
    # each time slow goes 1 step, fast goes 2 steps
    def middleNode(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow