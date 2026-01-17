# 141. Linked List Cycle

- Cho một danh sách liên kết đơn, hãy xác định xem nó có chứa một chu trình hay không. Một chu trình tồn tại nếu một nút trong danh sách có thể được truy cập lại bằng cách theo dõi các con trỏ tiếp theo.

## 1. Các cách giải với độ phức tạp O(N^2)

### 1.1 Brute Force

**Ý tưởng:** Dùng hai vòng lặp lồng nhau để kiểm tra từng cặp nút trong danh sách liên kết. Nếu có hai nút trỏ đến cùng một địa chỉ, thì danh sách có chu trình.

**Cách hoạt động:**

1. Dùng một vòng lặp để duyệt qua từng nút trong danh sách liên kết.
2. Với mỗi nút hiện tại, dùng một vòng lặp khác để kiểm tra tất cả các nút tiếp theo trong danh sách.
3. Nếu tìm thấy một nút trùng với nút hiện tại, trả về True.

**Độ phức tạp:**

- Thời gian: O(N^2) vì có hai vòng lặp lồng nhau.
- Không gian: O(1) vì không sử dụng bộ nhớ bổ sung.

```python
class Solution:
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
```

## 2. Cách giải với độ phức tạp O(N)

### 2.1 Sử dụng HashSet

**Ý tưởng:** Sử dụng một tập hợp (HashSet) để lưu trữ các nút đã được thăm. Khi duyệt qua danh sách, nếu gặp lại một nút đã có trong tập hợp, thì danh sách có chu trình.

**Cách hoạt động:**

1. Tạo một tập hợp rỗng để lưu trữ các nút đã thăm.
2. Duyệt qua danh sách liên kết từ nút đầu tiên.
3. Với mỗi nút hiện tại, kiểm tra xem nó đã có trong tập hợp chưa:
   - Nếu có, trả về True (có chu trình).
   - Nếu không, thêm nút vào tập hợp và tiếp tục duyệt.
4. Nếu duyệt hết danh sách mà không gặp lại nút nào, trả về False.

**Độ phức tạp:**

- Thời gian: O(N) vì duyệt qua tất cả các nút một lần.
- Không gian: O(N) vì sử dụng bộ nhớ để lưu trữ các nút đã thăm.

```python
class Solution:
    def hasCycle_HashSet(self, head: Optional[ListNode]) -> bool:
        visited = set()
        current = head
        while current:
            if current in visited:
                return True
            visited.add(current)
            current = current.next
        return False
```

### 2.2 Fast and Slow Pointers

**Ý tưởng:** Sử dụng hai con trỏ (fast và slow) để duyệt qua danh sách liên kết với tốc độ khác nhau. Nếu có chu trình, hai con trỏ sẽ gặp nhau tại một điểm nào đó.

**Cách hoạt động:**

1. Khởi tạo hai con trỏ, `slow` và `fast`, đều trỏ đến nút đầu tiên của danh sách.
2. Di chuyển con trỏ `slow` một bước mỗi lần, trong khi con trỏ `fast` di chuyển hai bước mỗi lần.
3. Nếu có chu trình, hai con trỏ sẽ gặp nhau tại một điểm nào đó
4. Nếu con trỏ `fast` hoặc `fast.next` trở thành None, danh sách không có chu trình.

**Độ phức tạp:**

- Thời gian: O(N) vì trong trường hợp xấu nhất, chúng ta sẽ duyệt qua tất cả các nút.
- Không gian: O(1) vì không sử dụng bộ nhớ bổ sung.

```python
class Solution:
    def hasCycle_FastSlow(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        slow = head
        fast = head.next

        while fast and fast.next:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next

        return False
```
