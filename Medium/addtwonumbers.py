# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        l1_v = []
        l2_v = []
        while l1:
            l1_v.append(l1.val)
            l1 = l1.next
        while l2:
            l2_v.append(l2.val)
            l2 = l2.next
        
        num1 = int(''.join(map(str, reversed(l1_v))))
        num2 = int(''.join(map(str, reversed(l2_v))))
        l3_v = [int(c) for c in str(num1 + num2)][::-1]
        dummy = ListNode()
        cur = dummy
        for x in l3_v:
            cur.next = ListNode(x)
            cur = cur.next
        return dummy.next