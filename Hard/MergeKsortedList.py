# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        lists_val = []

        for node in lists:
            while node:
                lists_val.append(node.val)
                node = node.next
        lists_val.sort()
        dummy = ListNode()
        curr = dummy
        for elem in lists_val:
            curr.next = ListNode(elem)
            curr = curr.next
        return dummy.next
