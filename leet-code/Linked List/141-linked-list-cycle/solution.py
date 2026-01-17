from typing import Optional
from ..ListNode import ListNode

class Solution:
    # Time Complexity: O(N^2)
    # Space Complexity: O(1)
    def hasCycle_BruteForce(self, head: Optional[ListNode]) -> bool:
        current = head
        while current:
            runner = head
            while runner != current:
                if runner == current.next:
                    return True
                runner = runner.next
            current = current.next
        return False

    # Time Complexity: O(N)
    # Space Complexity: O(N)
    def hasCycle_HashSet(self, head: Optional[ListNode]) -> bool:
        visited = set()
        current = head
        while current:
            if current in visited:
                return True
            visited.add(current)
            current = current.next

        return False

    # Time Complexity: O(N)
    # Space Complexity: O(1)
    def hasCycle_FastSlowPointer(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False