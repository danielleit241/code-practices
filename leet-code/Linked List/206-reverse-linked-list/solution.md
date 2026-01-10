# 206. Reverse Linked List

- Cho phần tử đầu tiên của một **danh sách liên kết đơn**, hãy đảo ngược danh sách đó và trả về danh sách đã đảo ngược.

## 1. Các cách giải với độ phức tạp O(n)

### 1.1 Array + Reverse

**Ý tưởng:** Dùng một mảng để lưu trữ các giá trị của các node trong danh sách liên kết, sau đó đảo ngược mảng và gán lại các giá trị cho các node trong danh sách liên kết.

**Cách hoạt động:**

1. Khởi tạo một mảng rỗng `values` để lưu trữ các giá trị của các node.
2. Duyệt qua Linked List và thêm các giá trị của các node vào mảng `values`.
3. Đảo ngược mảng `values`.
4. Duyệt lại Linked List và gán các giá trị từ mảng `values` cho các node.
   - Trả về phần tử đầu tiền của Linked List đã được đảo ngược.

**Độ phức tạp:**

- Thời gian: O(n) - với n là số lượng node trong danh sách liên kết.
- Không gian: O(n) - do sử dụng mảng phụ để lưu trữ các giá trị.

```python
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        values = []
        curr = head
        while curr:
            values.append(curr.val)
            curr = curr.next

        values.reverse()
        curr = head
        for val in values:
            curr.val = val
            curr = curr.next

        return head
```

### 1.2 Two Pointers

**Ý tưởng:** Sử dụng hai con trỏ để đảo ngược liên kết giữa các node trong danh sách liên kết.
**Cách hoạt động:**

1. Khởi tạo hai con trỏ `prev` và `curr`. `prev` được đặt là `None` và `curr` được đặt là `head`.
2. Duyệt qua danh sách liên kết cho đến khi `curr` là `None`:
   - Lưu trữ con trỏ tiếp theo của `curr` trong một biến tạm thời `nextNode`.
   - Đặt con trỏ `next` của `curr` trỏ về `prev`.
   - Di chuyển `prev` lên `curr`.
   - Di chuyển `curr` lên `nextNode`.
3. Khi vòng lặp kết thúc, `prev` sẽ trỏ đến phần tử đầu tiên của danh sách liên kết đã được đảo ngược.

**Độ phức tạp:**

- Thời gian: O(n) - với n là số lượng node trong danh sách liên kết.
- Không gian: O(1) - không sử dụng bộ nhớ phụ đáng kể.

```python
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            nextNode = curr.next  # Lưu lại node tiếp theo
            curr.next = prev      # Đảo ngược liên kết
            prev = curr           # Di chuyển prev lên curr
            curr = nextNode       # Di chuyển curr lên node tiếp theo

        return prev
```
