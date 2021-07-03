class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        l1head = l1
        l2head = l2
        required = l1
        while l1 or l2:
            sm = carry + (l1.val if l1 else 0) + (l2.val if l2 else 0)
            carry = 1 if sm > 9 else 0
            sm = sm%10

            if l1:
                l1.val = sm
                prev = l1
                l1 = l1.next
            else:
                required = l2head
                prev = l2

            if l2:
                l2.val = sm
                l2 = l2.next
        if carry:
            prev.next = ListNode(1)
        return required