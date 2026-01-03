# 704. Binary Search

- Cho một mảng các số nguyên nums được sắp xếp theo thứ tự tăng dần và một số nguyên target, hãy viết một hàm để tìm kiếm target trong nums. Nếu target tồn tại, hãy trả về chỉ số của nó. Nếu không, hãy trả về -1.

  > Bạn phải viết một thuật toán có độ phức tạp thời gian chạy O(log n).

## 1. Các cách giải với độ phức tạp O(n)

### 1.1 Linear Search

**Ý tưởng:**
Duyệt tuần tự qua từng phần tử trong mảng cho đến khi tìm thấy target hoặc hết mảng.

**Cách hoạt động:**

1. Duyệt qua từng phần tử trong mảng từ đầu đến cuối
2. So sánh từng phần tử với target
3. Nếu tìm thấy, trả về chỉ số của phần tử đó
4. Nếu duyệt hết mảng mà không tìm thấy, trả về -1

**Độ phức tạp:**

- Thời gian: O(n) - trong trường hợp xấu nhất phải duyệt qua toàn bộ mảng
- Không gian: O(1) - chỉ sử dụng một số biến cố định

```python
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        for i, n in enumerate(nums):
            if n == target:
                return i
        return -1
```

## 2. Các cách giải với độ phức tạp O(log n)

### 2.1 Binary Search

**Ý tưởng:**
Tận dụng tính chất mảng đã được sắp xếp để chia đôi không gian tìm kiếm sau mỗi lần so sánh.

**Cách hoạt động:**

1. Khởi tạo hai con trỏ `left` và `right` ở đầu và cuối mảng
2. Trong khi `left <= right`:
   - Tính chỉ số phần tử giữa: `mid = left + (right - left) // 2`
   - Nếu `nums[mid] == target`: trả về `mid`
   - Nếu `nums[mid] < target`: target nằm bên phải, `left = mid + 1`
   - Nếu `nums[mid] > target`: target nằm bên trái, `right = mid - 1`
3. Nếu không tìm thấy, trả về -1

**Độ phức tạp:**

- Thời gian: O(log n) - mỗi lần lặp giảm không gian tìm kiếm đi một nửa
- Không gian: O(1) - chỉ sử dụng một số biến cố định

```python
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1
```

### 2.2 Binary Search Upper Bound

**Ý tưởng:**
Tìm vị trí đầu tiên có giá trị lớn hơn target (upper bound), sau đó kiểm tra phần tử trước đó có phải là target không.

**Cách hoạt động:**

1. Khởi tạo `left = 0`, `right = len(nums)` (lưu ý: right = độ dài mảng, không phải độ dài - 1)
2. Trong khi `left < right`:
   - Tính `mid = left + (right - left) // 2`
   - Nếu `nums[mid] <= target`: tìm ở nửa phải, `left = mid + 1`
   - Nếu `nums[mid] > target`: tìm ở nửa trái, `right = mid`
3. Sau vòng lặp, `left` là vị trí đầu tiên > target
4. Kiểm tra phần tử tại `left - 1` có bằng target không
5. Nếu có trả về `left - 1`, ngược lại trả về -1

**Độ phức tạp:**

- Thời gian: O(log n) - binary search chuẩn
- Không gian: O(1) - chỉ sử dụng một số biến cố định

```python
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid

        if left == 0 or nums[left - 1] != target:
            return -1
        return left - 1
```

### 2.3 Binary Search Lower Bound

**Ý tưởng:**
Tìm vị trí đầu tiên có giá trị >= target (lower bound), sau đó kiểm tra phần tử đó có bằng target không.

**Cách hoạt động:**

1. Khởi tạo `left = 0`, `right = len(nums)` (lưu ý: right = độ dài mảng)
2. Trong khi `left < right`:
   - Tính `mid = left + (right - left) // 2`
   - Nếu `nums[mid] < target`: tìm ở nửa phải, `left = mid + 1`
   - Nếu `nums[mid] >= target`: tìm ở nửa trái, `right = mid`
3. Sau vòng lặp, `left` là vị trí đầu tiên >= target
4. Kiểm tra `left` có nằm trong mảng và `nums[left]` có bằng target không
5. Nếu có trả về `left`, ngược lại trả về -1

**Độ phức tạp:**

- Thời gian: O(log n) - binary search chuẩn
- Không gian: O(1) - chỉ sử dụng một số biến cố định

```python
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums)

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        if left == len(nums) or nums[left] != target:
            return -1
        return left
```
