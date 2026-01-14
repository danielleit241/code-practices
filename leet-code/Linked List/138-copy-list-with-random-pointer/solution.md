# 138. Copy List with Random Pointer

- Cho một danh sách liên kết đặc biệt, trong đó mỗi node có hai con trỏ: `next` (trỏ tới node tiếp theo) và `random` (có thể trỏ tới bất kỳ node nào trong danh sách hoặc null). Hãy tạo một bản sao sâu (deep copy) của danh sách này.

## 1. Các cách giải với độ phức tạp O(N)

### 1.1 Hash Map

**Ý tưởng:**

- Duyệt qua danh sách gốc và tạo một node mới cho mỗi node, lưu ánh xạ từ node cũ sang node mới bằng một hash map.
- Duyệt lại lần nữa để gán các con trỏ `next` và `random` cho node mới dựa trên ánh xạ đã lưu.

**Cách hoạt động:**

1. Nếu danh sách rỗng, trả về None.
2. Tạo một hash map `map` để ánh xạ node cũ sang node mới.
3. Duyệt lần 1: với mỗi node `curr` trong danh sách gốc, tạo node mới với giá trị tương ứng và lưu vào `map[curr]`.
4. Duyệt lần 2: với mỗi node `curr`, gán:
   - `map[curr].next = map.get(curr.next)`
   - `map[curr].random = map.get(curr.random)`
5. Trả về node mới đầu tiên: `map.get(head)`

**Độ phức tạp:**

- Thời gian: O(N) — duyệt qua danh sách hai lần.
- Không gian: O(N) — dùng hash map để lưu ánh xạ node cũ → node mới.

```python
class Solution:
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
```

---
