from typing import Optional
from ..Node import Node

class Solution:
    # Time Complexity: O(N)
    # Space Complexity: O(N)
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        map = {}
        curr = head
        while curr:
            map[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            map[curr].next = map.get(curr.next)
            map[curr].random = map.get(curr.random)
            curr = curr.next

        return map.get(head)