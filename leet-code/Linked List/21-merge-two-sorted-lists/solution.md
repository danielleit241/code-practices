# 21. Merge Two Sorted Lists

- Cho hai danh sách liên kết đã được sắp xếp `list1` và `list2`, hãy gộp hai danh sách này thành một danh sách được sắp xếp. Danh sách mới được tạo bằng cách nối các node từ hai danh sách ban đầu.

## 1. Các cách giải với độ phức tạp O(n + m)

### 1.1 Tạo node mới

**Ý tưởng:** Tạo các node mới cho danh sách kết quả bằng cách so sánh giá trị của các node từ hai danh sách đầu vào.

**Cách hoạt động:**

1. Xử lý trường hợp đặc biệt:
   - Nếu `list1` rỗng, trả về `list2`
   - Nếu `list2` rỗng, trả về `list1`
2. Tạo node dummy `res` với giá trị 0 và con trỏ `curr` trỏ đến node dummy
3. Duyệt qua cả hai danh sách khi cả hai đều còn node:
   - So sánh giá trị của node hiện tại ở `list1` và `list2`
   - Tạo node mới với giá trị nhỏ hơn và nối vào `curr.next`
   - Di chuyển con trỏ của danh sách có node được chọn
   - Di chuyển `curr` sang node tiếp theo
4. Nối phần còn lại của danh sách chưa hết vào cuối
5. Trả về `res.next` (bỏ qua node dummy)

**Độ phức tạp:**

- Thời gian: O(n + m) - với n, m là số node của `list1` và `list2`
- Không gian: O(n + m) - do tạo các node mới cho kết quả

```python
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        res = ListNode(0)
        curr = res

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = ListNode(list1.val)
                list1 = list1.next
            else:
                curr.next = ListNode(list2.val)
                list2 = list2.next
            curr = curr.next

        curr.next = list1 if list1 else list2

        return res.next
```

### 1.2 Sử dụng lại node có sẵn

**Ý tưởng:** Thay vì tạo node mới, tái sử dụng các node từ hai danh sách ban đầu bằng cách thay đổi con trỏ `next`.

**Cách hoạt động:**

1. Xử lý trường hợp đặc biệt:
   - Nếu `list1` rỗng, trả về `list2`
   - Nếu `list2` rỗng, trả về `list1`
2. Tạo node dummy `res` với giá trị 0 và con trỏ `curr` trỏ đến node dummy
3. Duyệt qua cả hai danh sách khi cả hai đều còn node:
   - So sánh giá trị của node hiện tại ở `list1` và `list2`
   - Nối trực tiếp node có giá trị nhỏ hơn vào `curr.next`
   - Di chuyển con trỏ của danh sách có node được chọn
   - Di chuyển `curr` sang node tiếp theo
4. Nối phần còn lại của danh sách chưa hết vào cuối
5. Trả về `res.next` (bỏ qua node dummy)

**Độ phức tạp:**

- Thời gian: O(n + m) - với n, m là số node của `list1` và `list2`
- Không gian: O(1) - chỉ sử dụng con trỏ, không tạo node mới

```python
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        res = ListNode(0)
        curr = res

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        curr.next = list1 if list1 else list2

        return res.next
```

### 1.3 Đệ quy (Recursive)

**Ý tưởng:** Sử dụng đệ quy để so sánh và nối các node. Mỗi lần đệ quy chọn node nhỏ hơn và gọi đệ quy cho phần còn lại.

**Cách hoạt động:**

1. Base cases:
   - Nếu `list1` rỗng, trả về `list2`
   - Nếu `list2` rỗng, trả về `list1`
2. So sánh giá trị đầu của hai danh sách:
   - Nếu `list1.val < list2.val`:
     - `list1.next` = kết quả merge của `list1.next` và `list2`
     - Trả về `list1`
   - Ngược lại:
     - `list2.next` = kết quả merge của `list1` và `list2.next`
     - Trả về `list2`
3. Đệ quy sẽ tự động xử lý đến khi gặp base case

**Độ phức tạp:**

- Thời gian: O(n + m) - duyệt qua tất cả các node
- Không gian: O(n + m) - do stack của đệ quy

```python
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val < list2.val:
            list1.next = self.mergeTwoLists_Recursive(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists_Recursive(list1, list2.next)
            return list2
```

---
