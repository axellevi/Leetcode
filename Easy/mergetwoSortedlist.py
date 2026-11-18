# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        l1_v = []
        l2_v = []
        while list1:
            l1_v.append(list1.val)
            list1 = list1.next
        while list2:
            l2_v.append(list2.val)
            list2 = list2.next
        l3 = sorted(l1_v + l2_v)
        dummy = ListNode()
        cur = dummy
        for elem in l3:
            cur.next = ListNode(elem)
            cur = cur.next
        return dummy.next
