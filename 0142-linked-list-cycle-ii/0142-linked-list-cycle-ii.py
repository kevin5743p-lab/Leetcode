# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        arr = list()
        lcon = False

        f = head
        
        if head == None :
            print('There is no cycle in the linked list.')
            return None

        while f != None and f.next != None:
            if f in arr:
                return f
            arr.append(f)
            f = f.next
        if f.next == None:
            return None

        


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna