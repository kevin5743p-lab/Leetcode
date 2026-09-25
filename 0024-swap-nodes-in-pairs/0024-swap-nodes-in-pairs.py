# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        pointer = head
        if head == None or head.next == None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        pointer = dummy
        while pointer.next and pointer.next.next:
            curr = pointer.next
            nxt = pointer.next.next
            var = nxt.next
            nxt.next = curr
            pointer.next = nxt
            curr.next = var    
            pointer = pointer.next.next
        return dummy.next



        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna