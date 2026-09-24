# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        length = 0
        pointer = head
        while pointer != None:
            length += 1
            pointer = pointer.next
        target_node = length - n
        index = 0
        pointer = head
        if target_node == 0:
            head = pointer.next
            return head
        while pointer != None:
            if index + 1 == target_node:
                pointer.next = pointer.next.next
                return head
            index = index + 1
            pointer = pointer.next
                
            

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna