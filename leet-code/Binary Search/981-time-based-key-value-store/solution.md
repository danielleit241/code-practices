# 981. Time Based Key-Value Store

- Thiết kế một cấu trúc dữ liệu dựa trên thời gian lưu trữ các cặp key-value với nhiều giá trị cho cùng một key tại các timestamp khác nhau và truy xuất giá trị của key tại một timestamp nhất định.

- Cài đặt class `TimeMap`:

  - `TimeMap()`: Khởi tạo đối tượng của cấu trúc dữ liệu
  - `void set(String key, String value, int timestamp)`: Lưu trữ key `key` với value `value` tại timestamp `timestamp`
  - `String get(String key, int timestamp)`: Trả về giá trị được set cho `key` tại timestamp bằng hoặc trước đó. Nếu có nhiều giá trị, trả về giá trị có timestamp lớn nhất. Nếu không có giá trị, trả về chuỗi rỗng `""`

  > Tất cả các timestamp của lệnh `set` đều khác nhau và được gọi theo thứ tự tăng dần

## 1. Các cách giải với độ phức tạp O(n)

### 1.1 Hashmap + Linear Search

**Ý tưởng:** Sử dụng hashmap để lưu trữ danh sách các cặp (value, timestamp) cho mỗi key, sau đó duyệt tuyến tính để tìm giá trị phù hợp.

**Cách hoạt động:**

1. **set(key, value, timestamp):**
   - Thêm (value, timestamp) vào danh sách của key trong hashmap
2. **get(key, timestamp):**
   - Nếu key không tồn tại, trả về ""
   - Duyệt qua danh sách từ cuối về đầu
   - Tìm cặp đầu tiên có timestamp <= timestamp cho trước
   - Trả về value tương ứng hoặc "" nếu không tìm thấy

**Độ phức tạp:**

- Thời gian:
  - `set`: O(1)
  - `get`: O(n) - trong trường hợp xấu nhất phải duyệt qua tất cả timestamps
- Không gian: O(n) - lưu trữ tất cả các cặp (value, timestamp)

```python
class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        values = self.store[key]

        for i in range(len(values) - 1, -1, -1):
            if values[i][1] <= timestamp:
                return values[i][0]

        return ""
```

## 2. Các cách giải với độ phức tạp O(log n)

### 2.1 Hashmap + Binary Search

**Ý tưởng:** Sử dụng dict {} thông thường để lưu trữ danh sách các cặp (value, timestamp) cho mỗi key. Do timestamps được thêm theo thứ tự tăng dần, ta có thể dùng binary search để tìm giá trị phù hợp.

**Cách hoạt động:**

1. **init():**

   - Khởi tạo `self.store = {}` - dict rỗng

2. **set(key, value, timestamp):**

   - Kiểm tra nếu key chưa tồn tại, khởi tạo list rỗng
   - Thêm (value, timestamp) vào list của key

3. **get(key, timestamp):**
   - Nếu key không tồn tại, trả về ""
   - Áp dụng binary search trên list timestamps:
     - Nếu timestamp nhỏ nhất > timestamp cho trước: trả về ""
     - Nếu timestamp lớn nhất <= timestamp cho trước: trả về value cuối cùng
     - Ngược lại: binary search để tìm value có timestamp lớn nhất <= timestamp cho trước

**Độ phức tạp:**

- Thời gian:
  - `set`: O(1)
  - `get`: O(log n) - binary search
- Không gian: O(n)

```python
class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        values = self.store[key]

        left, right = 0, len(values) - 1

        if values[0][1] > timestamp:
            return ""
        if values[-1][1] <= timestamp:
            return values[-1][0]

        res = ""

        while left <= right:
            mid = left + (right - left) // 2

            if values[mid][1] <= timestamp:
                res = values[mid][0]
                left = mid + 1
            else:
                right = mid - 1

        return res
```
