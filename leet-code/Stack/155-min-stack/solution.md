# 155. Min Stack

- Thiết kế một ngăn xếp hỗ trợ các thao tác push, pop, top và lấy phần tử nhỏ nhất trong thời gian không đổi.
- Triển khai lớp MinStack:
  - `MinStack()` khởi tạo đối tượng ngăn xếp.
  - `void push(int val)` đẩy phần tử val vào ngăn xếp.
  - `void pop()` loại bỏ phần tử ở đỉnh ngăn xếp.
  - `int top()` lấy phần tử ở đỉnh ngăn xếp.
  - `int getMin()` lấy phần tử nhỏ nhất trong ngăn xếp.

## 1. Các cách giải với độ phức tạp O(n)

### 1.1 Brute Force

**Ý tưởng**: Dùng một stack tạm để chứa tất cả các phần tử từ top -> bot đồng thời tìm giá trị min, sau đó duyệt lại stack tạm và lưu lại vào stack theo trình tự bot -> top.

**Cách hoạt động:**

- `MinStack()`:
  1. Khởi tạo một stack rỗng
- `void push(int val)`:
  1. Thêm val vào cuối stack
- `void pop()`:
  1. Xóa phần tử cuối cùng của stack
- `int top()`:
  1. Trả về phần tử cuối cùng của stack
- `int getMin()`:
  1. Tạo stack tạm để lưu các phần tử
  2. Duyệt qua tất cả phần tử trong stack, tìm giá trị nhỏ nhất và lưu vào stack tạm
  3. Đẩy lại tất cả phần tử từ stack tạm về stack gốc
  4. Trả về giá trị nhỏ nhất

**Độ phức tạp:**

- Thời gian: O(1) cho push, pop, top; O(n) cho getMin
- Không gian: O(n) cho stack tạm trong getMin

```python
class Solution:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        if not self.stack:
            return
        self.stack.pop()

    def top(self) -> int:
        if not self.stack:
            return None
        return self.stack[-1]

    def getMin(self) -> int:
        if not self.stack:
            return None
        tmp = []
        mini = self.stack[-1]
        while len(self.stack):
            mini = min(mini, self.stack[-1])
            tmp.append(self.stack.pop())

        while len(tmp):
            self.stack.append(tmp.pop())
        return mini
```

## 2. Các cách giải với độ phức tạp O(1)

### 2.1 Two Stacks

**Ý tưởng**: Sử dụng hai stack song song - một stack lưu giá trị thực tế, một stack lưu giá trị nhỏ nhất tại mỗi vị trí tương ứng. Khi push/pop, cả hai stack đều được cập nhật đồng bộ.

**Cách hoạt động:**

- `MinStack()`:
  1. Khởi tạo hai stack rỗng: stack chính và min_stack
- `void push(int val)`:
  1. Thêm val vào stack chính
  2. Nếu min_stack rỗng, thêm val vào min_stack
  3. Ngược lại, thêm min(val, min_stack[-1]) vào min_stack
- `void pop()`:
  1. Xóa phần tử cuối cùng của cả hai stack
- `int top()`:
  1. Trả về phần tử cuối cùng của stack chính
- `int getMin()`:
  1. Trả về phần tử cuối cùng của min_stack (đây là giá trị nhỏ nhất hiện tại)

**Độ phức tạp:**

- Thời gian: O(1) cho tất cả các thao tác
- Không gian: O(n) cho cả hai stack

```python
class Solution:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.stack[-1]))

    def pop(self) -> None:
        if not self.stack:
            return
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        if not self.stack:
            return None
        return self.stack[-1]

    def getMin(self) -> int:
        if not self.min_stack:
            return None
        return self.min_stack[-1]
```

### 2.2 One Stacks

**Ý tưởng**: Tối ưu hóa không gian bằng cách chỉ dùng một stack. Thay vì lưu giá trị thực, ta lưu **hiệu số** giữa giá trị hiện tại và giá trị min. Khi hiệu số âm, nghĩa là đã có giá trị min mới. Biến min được cập nhật riêng.

**Cách hoạt động:**

- `MinStack()`:
  1. Khởi tạo stack rỗng và min = infinity
- `void push(int val)`:
  1. Nếu stack rỗng: thêm 0 vào stack, gán min = val
  2. Ngược lại: thêm (val - min) vào stack
  3. Nếu val < min, cập nhật min = val
- `void pop()`:
  1. Lấy giá trị pop từ stack
  2. Nếu pop < 0 (nghĩa là min cũ đang bị xóa), khôi phục lại min cũ: min = min - pop
- `int top()`:
  1. Lấy giá trị top từ stack
  2. Nếu top > 0: giá trị thực = top + min
  3. Nếu top ≤ 0: giá trị thực = min
- `int getMin()`:
  1. Trả về biến min

**Độ phức tạp:**

- Thời gian: O(1) cho tất cả các thao tác
- Không gian: O(n) chỉ cho một stack, tiết kiệm hơn phương pháp Two Stacks

```python
class Solution:
    def __init__(self):
        self.stack = []
        self.min = float('inf')

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min = val
        else:
            self.stack.append(val - self.min)
            if val < self.min:
                self.min = val

    def pop(self) -> None:
        if not self.stack:
            return

        pop = self.stack.pop()
        if pop < 0:
            self.min = self.min - pop

    def top(self) -> int:
        if not self.stack:
            return None
        top = self.stack[-1]
        if top > 0:
            return top + self.min
        else:
            return self.min

    def getMin(self) -> int:
        return self.min
```
