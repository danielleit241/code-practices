# 2. Add Two Numbers

- Cho hai danh sách liên kết đại diện cho hai số nguyên không âm, trong đó mỗi node chứa một chữ số và các chữ số được lưu trữ theo thứ tự ngược (chữ số ít quan trọng nhất ở đầu danh sách). Hãy cộng hai số này và trả về kết quả dưới dạng một danh sách liên kết mới.

## 1. Các cách giải với độ phức tạp O(max(N, M))

### 1.1 Đệ quy

**Ý tưởng:** Sử dụng đệ quy để cộng từng cặp node tương ứng của hai danh sách liên kết, đồng thời xử lý phần nhớ (carry) khi tổng vượt quá 9. Đệ quy sẽ tiếp tục cho đến khi cả hai danh sách và phần nhớ đều hết.

**Cách hoạt động:**

1. Định nghĩa hàm đệ quy `addLists(l1, l2, carry)` để cộng hai node `l1` và `l2` cùng với phần nhớ `carry`.
2. Nếu cả `l1`, `l2` và `carry` đều là None hoặc 0, trả về None (điều kiện dừng).
3. Tính tổng `total = carry + (l1.val if l1 else 0) + (l2.val if l2 else 0)`.
4. Tạo node mới với giá trị `total % 10`.
5. Gọi đệ quy cho các node tiếp theo và phần nhớ mới `total // 10`.

**Độ phức tạp:**

- Thời gian: O(max(N, M)) — duyệt qua cả hai danh sách.
- Không gian: O(max(N, M)) — do ngăn xếp đệ quy

```python
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def addLists(n1: Optional[ListNode], n2: Optional[ListNode], carry: int) -> Optional[ListNode]:
            if not n1 and not n2 and carry == 0:
                return None

            val1 = n1.val if n1 else 0
            val2 = n2.val if n2 else 0

            total = val1 + val2 + carry
            new_carry = total // 10
            node = ListNode(total % 10)

            next1 = n1.next if n1 else None
            next2 = n2.next if n2 else None
            node.next = addLists(next1, next2, new_carry)

            return node

        return addLists(l1, l2, 0)
```

### 1.2 Pointer Iterative

**Ý tưởng:** Sử dụng hai con trỏ để duyệt qua hai danh sách liên kết, cộng từng cặp node cùng với phần nhớ (carry) và xây dựng danh sách kết quả một cách tuần tự.

**Cách hoạt động:**

1. Tạo một node giả `dummy` để dễ dàng xây dựng danh sách kết quả.
2. Sử dụng hai con trỏ đầu danh sách `l1` và `l2` để duyệt, cùng với biến `carry` để lưu phần nhớ.
3. Trong vòng lặp, tính tổng `total = carry + (l1.val if l1 else 0) + (l2.val if l2 else 0)`.
4. Tạo node mới với giá trị `total % 10` và cập nhật `carry = total // 10`.
5. Di chuyển các con trỏ `l1` và `l2` về node tiếp theo.
6. Sau khi vòng lặp kết thúc, nếu còn phần nhớ `carry`, tạo thêm một node mới.

**Độ phức tạp:**

- Thời gian: O(max(N, M)) — duyệt qua cả hai danh sách.
- Không gian: O(1) — không sử dụng bộ nhớ phụ ngoài danh sách kết quả.

```python
class Solution:
    def addTwoNumbers_Pointer(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry:
            current.next = ListNode(carry)

        return dummy.next
```
