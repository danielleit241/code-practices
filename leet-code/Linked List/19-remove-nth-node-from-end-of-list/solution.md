# 19. Remove Nth Node From End of List

- Cho một danh sách liên kết đơn `head` và một số nguyên `n`, hãy xóa node thứ n tính từ cuối danh sách và trả về head mới.

## 1. Các cách giải với độ phức tạp O(n)

### 1.1 Dùng mảng lưu node

**Ý tưởng:** Lưu tất cả các node vào một mảng, sau đó xác định node cần xóa dựa vào chỉ số.

**Cách hoạt động:**

1. Duyệt qua danh sách, lưu từng node vào mảng `nodes`.
2. Tìm chỉ số node cần xóa: `remove_idx = len(nodes) - n`.
3. Nếu node cần xóa là node đầu tiên (`remove_idx == 0`), trả về `head.next`.
4. Ngược lại, cập nhật `nodes[remove_idx - 1].next = nodes[remove_idx].next` để bỏ qua node cần xóa.
5. Trả về `head`.

**Độ phức tạp:**

- Thời gian: O(n) - duyệt qua toàn bộ danh sách một lần
- Không gian: O(n) - lưu tất cả các node vào mảng

```python
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
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
```

### 1.2 Đếm độ dài danh sách

**Ý tưởng:** Duyệt qua danh sách để đếm tổng số node, sau đó duyệt lại để đến node ngay trước node cần xóa và cập nhật con trỏ next.

**Cách hoạt động:**

1. Tạo node dummy trỏ vào head để xử lý trường hợp xóa node đầu tiên.
2. Duyệt qua danh sách để đếm tổng số node (`length`).
3. Duyệt lại từ dummy, di chuyển `length - n` bước để đến node ngay trước node cần xóa.
4. Cập nhật con trỏ next để bỏ qua node cần xóa.
5. Trả về `dummy.next`.

**Độ phức tạp:**

- Thời gian: O(n) - duyệt qua danh sách hai lần
- Không gian: O(1) - chỉ dùng biến đếm

```python
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
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
```

### 1.3 Hai con trỏ (Two Pointers)

**Ý tưởng:** Sử dụng hai con trỏ cách nhau n node để xác định node cần xóa chỉ trong một lần duyệt.

**Cách hoạt động:**

1. Tạo node dummy trỏ vào head.
2. Đặt hai con trỏ `first` và `second` tại dummy.
3. Di chuyển `first` tiến lên n+1 bước.
4. Di chuyển cả hai con trỏ cho đến khi `first` đến cuối danh sách.
5. Lúc này, `second` đứng ngay trước node cần xóa. Cập nhật `second.next = second.next.next`.
6. Trả về `dummy.next`.

**Độ phức tạp:**

- Thời gian: O(n) - chỉ duyệt qua danh sách một lần
- Không gian: O(1) - chỉ dùng các con trỏ

```python
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
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
```
