# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        p1 = list1
        p2 = list2

        merge = ListNode()
        merger = merge
        while p1 != None and p2 != None :
            if p1.val <= p2.val:
                merger.next = p1
                merger = merger.next
                p1 = p1.next
            else:
                merger.next = p2
                merger = merger.next
                p2 = p2.next
        if p1 == None :
            merger.next = p2
        elif p2 == None :
            merger.next = p1
        return merge.next

            

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna