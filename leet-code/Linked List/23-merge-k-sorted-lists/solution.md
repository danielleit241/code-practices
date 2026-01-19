# 28. Merge K Sorted Lists

- Cho một mảng gồm `k` danh sách liên kết đã được sắp xếp theo thứ tự tăng dần, hãy hợp nhất tất cả các danh sách này thành một danh sách liên kết duy nhất đã được sắp xếp và trả về nó.

## 1. Các cách giải với độ phức tạp O(N^2)

### 1.1 Brute Force

**Ý tưởng:** Duyệt tất cả các phần tử trong các danh sách liên kết, lưu chúng vào một mảng, sau đó sắp xếp mảng này và tạo lại danh sách liên kết từ mảng đã sắp xếp.

**Cách hoạt động:**

1. Tạo một mảng trống để lưu trữ tất cả các giá trị từ các danh sách liên kết.
2. Duyệt qua từng danh sách liên kết và thêm tất cả các giá trị vào mảng.
3. Sắp xếp mảng.
4. Tạo một danh sách liên kết mới từ mảng đã sắp xếp và trả về nó.

**Độ phức tạp:**

- Thời gian: O(N log N), trong đó N là tổng số phần tử trong tất cả các danh sách liên kết.
- Không gian: O(N) để lưu trữ các giá trị trong mảng.

```python
class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
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
```

## 2. Cách giải với độ phức tạp O(N log k)

### 2.1 Sử dụng Min-Heap (Priority Queue)

**Ý tưởng:** Sử dụng một min-heap để luôn giữ phần tử nhỏ nhất từ các danh sách liên kết hiện tại, sau đó thêm phần tử này vào danh sách kết quả và tiếp tục với phần tử kế tiếp từ danh sách liên kết tương ứng.

**Cách hoạt động:**

1. Tạo một min-heap.
2. Đưa phần tử đầu tiên của mỗi danh sách liên kết vào min-heap.
3. Lặp lại quá trình sau cho đến khi min-heap rỗng:
   - Lấy phần tử nhỏ nhất từ min-heap.
   - Thêm phần tử này vào danh sách kết quả.
   - Nếu phần tử này có phần tử kế tiếp trong danh sách liên kết của nó, thêm phần tử kế tiếp vào min-heap.

**Độ phức tạp:**

- Thời gian: O(N log k), trong đó N là tổng số phần tử trong tất cả các danh sách liên kết và k là số lượng danh sách liên kết.
- Không gian: O(k) để lưu trữ các phần tử trong min-heap.

```python
import heapq
class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
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
```

### 2.2 Merge theo cặp (Divide and Conquer)

**Ý tưởng:** Sử dụng phương pháp chia để trị để hợp nhất các danh sách liên kết theo cặp, giảm số lượng danh sách cần hợp nhất ở mỗi bước.

**Cách hoạt động:**

1. Trong khi còn nhiều hơn một danh sách liên kết:
   - Hợp nhất các danh sách liên kết theo cặp.
   - Lưu trữ các danh sách đã hợp nhất vào một mảng mới.
2. Trả về danh sách liên kết duy nhất còn lại.

**Ví dụ:**

- Giả sử có 4 danh sách liên kết: L1, L2, L3, L4.
- Bước 1: Hợp nhất L1 và L2 thành L12, hợp nhất L3 và L4 thành L34.
- Bước 2: Hợp nhất L12 và L34 thành danh sách liên kết cuối cùng.

**Độ phức tạp:**

- Thời gian: O(N log k), trong đó N là tổng số phần tử trong tất cả các danh sách liên kết và k là số lượng danh sách liên kết.
- Không gian: O(1) nếu không tính không gian đệ quy.

```python
class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
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
```
