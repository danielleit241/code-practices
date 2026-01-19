from typing import Optional
from ..ListNode import ListNode

class Solution:
    def mergeKLists_BruteForce(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        values = []

        for lst in lists:
            while lst:
                values.append(lst.val)
                lst = lst.next

        values.sort()

        dummy = ListNode(0)
        curr = dummy

        for val in values:
            curr.next = ListNode(val)
            curr = curr.next

        return dummy.next
    
    def mergeKLists_Heap(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        import heapq

        minHeap = []

        for i, lst in enumerate(lists):
            if lst:
                heapq.heappush(minHeap, (lst.val, i, lst))

        dummy = ListNode(0)
        curr = dummy

        while minHeap:
            val, i, node = heapq.heappop(minHeap)
            curr.next = node
            curr = curr.next

            if node.next:
                heapq.heappush(minHeap, (node.next.val, i, node.next))

        return dummy.next

    def mergeKLists_MergeSort(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                mergedLists.append(self.mergeTwoLists(l1, l2))

            lists = mergedLists

        return lists[0]
    
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy

        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next

            curr = curr.next

        curr.next = l1 if l1 else l2

        return dummy.next