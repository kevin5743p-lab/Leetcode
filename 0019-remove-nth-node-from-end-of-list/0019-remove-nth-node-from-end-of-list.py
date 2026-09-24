# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        dummy = ListNode(0)
        dummy.next = head
        f,s = dummy,dummy
     

        count = 0
        while count != n:
            count += 1
            f = f.next
        
        while f.next != None:
            f = f.next
            s = s.next
        s.next = s.next.next
        return dummy.next
        


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna