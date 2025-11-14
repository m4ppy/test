# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#limit : one pass
dd
#approach 1 : two pointer
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        root = prev = ListNode()
        prev.next = head

        #set prev pointer(pointing before left index)
        for _ in range(left - 1):
            prev = prev.next

        #current points left index
        current = prev.next

        for _ in range(right - left):
            next = current.next



            #Loop 1
            # pre  cur  nex
            #  1 -> 2 -> 3 -> 4 -> 5 -> 6

            # pre  Scur  nex
            #  1 -> 2 -> 3 -> 4 -> 5 -> 6

            #Loop 3
            # pre  cur  nex
            #  1 -> 2 -> 3 -> 4 -> 5 -> 6
