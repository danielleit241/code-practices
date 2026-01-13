from typing import Optional
from ..ListNode import ListNode

class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def removeNthFromEnd_Array(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nums = []
        current = head
        while current:
            nums.append(current.val)
            current = current.next

        removeIndex = len(nums) - n
        nums.pop(removeIndex)

        dummy = ListNode(0)
        current = dummy
        for val in nums:
            current.next = ListNode(val)
            current = current.next

        return dummy.next
    
    # Time complexity: O(n)
    # Space complexity: O(1)
    def removeNthFromEnd_Length(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        length = 0
        current = head

        while current:
            length += 1
            current = current.next
        
        removeIndex = length - n
        current = dummy
        for _ in range(removeIndex):
            current = current.next

        current.next = current.next.next

        return dummy.next
    
    # Time complexity: O(n)
    # Space complexity: O(1)
    def removeNthFromEnd_TwoPointers(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy

        for _ in range(n + 1):
            first = first.next
        
        while first:
            first = first.next
            second = second.next

        second.next = second.next.next

        return dummy.next
    
