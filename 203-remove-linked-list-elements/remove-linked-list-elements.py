# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
   
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head
        prev , cur = dummy, head

        while cur:
            if cur.val == val:
                prev.next =cur.next #skipping cur, not moving prev
            else:
                prev = cur  #ADvancing prv keeping cur
            cur = cur.next

        return dummy.next