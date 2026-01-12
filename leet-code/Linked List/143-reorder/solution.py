from typing import Optional
from ..ListNode import ListNode

class Solution:
    # Time complexity: O(n^2)
    # Space complexity: O(1)
    def reorderList_BruteFroce(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        left = head
        while left and left.next:
            prev = None
            curr = left

            while curr.next:
                prev = curr
                curr = curr.next

            tail = curr
            
            if tail == left and tail == left.next:
                return
            
            prev.next = None
            tail.next = left.next
            left.next = tail
            left = tail.next

    # Time complexity: O(n)
    # Space complexity: O(1)
    def reorderList_FastAndSlowPointer(self, head: Optional[ListNode]) -> None:
        mid, fast = head, head

        while fast and fast.next:
            mid = mid.next
            fast = fast.next.next

        second = mid.next
        mid.next = None

        prev = None
        curr = second
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        p1, p2 = head, prev
        while p2:
            next1, next2 = p1.next, p2.next
            p1.next = p2
            p2.next = next1
            p1, p2 = next1, next2