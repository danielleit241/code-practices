# 143. Reorder List

- Cho một danh sách liên kết đơn `head`, hãy sắp xếp lại danh sách theo định dạng:

  ```
  L₀ → L₁ → L₂ → ... → Ln-1 → Ln
  ```

  thành:

  ```
  L₀ → Ln → L₁ → Ln-1 → L₂ → Ln-2 → ...
  ```

  > Bạn không được thay đổi giá trị trong các node của danh sách, chỉ được thay đổi các con trỏ.

## 1. Các cách giải với độ phức tạp O(n²)

### 1.1 Brute Force

**Ý tưởng:** Với mỗi node ở vị trí lẻ (bắt đầu từ node đầu), tìm node cuối cùng của danh sách và chèn nó vào ngay sau node hiện tại.

**Cách hoạt động:**

1. Khởi tạo con trỏ `left` tại `head`
2. Với mỗi vị trí lẻ (khi `left` và `left.next` tồn tại):
   - Duyệt từ `left` đến cuối danh sách để tìm node cuối (`tail`) và node trước nó (`prev`)
   - Nếu `tail` trùng với `left` hoặc `left.next`, tức là danh sách đã được sắp xếp → dừng
   - Tách node cuối: `prev.next = None`
   - Chèn `tail` vào sau `left`:
     - `tail.next = left.next`
     - `left.next = tail`
   - Di chuyển `left` sang `tail.next` (bỏ qua node vừa chèn)
3. Lặp lại cho đến khi không còn cặp nào cần sắp xếp

**Độ phức tạp:**

- Thời gian: O(n²) - mỗi lần lặp phải duyệt đến cuối danh sách
- Không gian: O(1) - chỉ sử dụng các con trỏ

```python
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        left = head
        while left and left.next:
            prev = None
            curr = left

            # Tìm node cuối và node trước nó
            while curr.next:
                prev = curr
                curr = curr.next

            tail = curr

            # Điều kiện dừng
            if tail == left or tail == left.next:
                return

            # Tách node cuối
            prev.next = None

            # Chèn tail vào sau left
            tail.next = left.next
            left.next = tail

            # Di chuyển left
            left = tail.next
```

## 2. Các cách giải với độ phức tạp O(n)

### 2.1 Fast and Slow Pointer

**Ý tưởng:** Chia danh sách làm hai phần, đảo ngược phần thứ hai, sau đó xen kẽ các node từ hai phần.

**Cách hoạt động:**

**Bước 1: Tìm điểm giữa của danh sách**

- Sử dụng kỹ thuật fast/slow pointer
- `slow` di chuyển 1 bước, `fast` di chuyển 2 bước
- Khi `fast` đến cuối, `slow` sẽ ở giữa

**Bước 2: Chia danh sách thành hai phần**

- Phần 1: từ `head` đến `mid`
- Phần 2: từ `mid.next` đến cuối
- Ngắt liên kết: `mid.next = None`

**Bước 3: Đảo ngược phần thứ hai**

- Sử dụng kỹ thuật two pointers để đảo ngược
- `prev` bắt đầu từ `None`, `curr` từ `second`
- Lặp: lưu `next`, đảo `curr.next = prev`, di chuyển `prev` và `curr`

**Bước 4: Xen kẽ các node từ hai phần**

- `p1` trỏ đến phần đầu, `p2` trỏ đến phần thứ hai (đã đảo)
- Lặp khi `p2` còn tồn tại:
  - Lưu node tiếp theo của cả hai: `next1`, `next2`
  - Nối `p1.next = p2`
  - Nối `p2.next = next1`
  - Di chuyển `p1 = next1`, `p2 = next2`

**Độ phức tạp:**

- Thời gian: O(n) - mỗi bước duyệt qua danh sách một lần
- Không gian: O(1) - chỉ sử dụng các con trỏ

```python
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Bước 1: Tìm điểm giữa
        mid, fast = head, head
        while fast and fast.next:
            mid = mid.next
            fast = fast.next.next

        # Bước 2: Chia danh sách
        second = mid.next
        mid.next = None

        # Bước 3: Đảo ngược phần thứ hai
        prev = None
        curr = second
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # Bước 4: Xen kẽ hai phần
        p1, p2 = head, prev
        while p2:
            next1, next2 = p1.next, p2.next
            p1.next = p2
            p2.next = next1
            p1, p2 = next1, next2
```
