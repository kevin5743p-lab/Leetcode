# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p1 = head
        p2 = head
        
        # Detecting a cycle first
        while p1 and p1.next:
            p1 = p1.next.next
            p2 = p2.next
            if p1 is p2:
                break
        else:
            return None

        # Detecting the exact Node
        pointer = head
        
        while pointer is not p1:
            p1 = p1.next
            pointer = pointer.next
        return p1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna