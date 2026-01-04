# 74. Search a 2D Matrix

- Cho một ma trận số nguyên m x n với các thuộc tính sau:

  - Các số nguyên trong mỗi hàng được sắp xếp từ trái sang phải.
  - Số nguyên đầu tiên của mỗi hàng lớn hơn số nguyên cuối cùng của hàng trước đó.

  Cho một số nguyên target, trả về true nếu target nằm trong ma trận hoặc false nếu không.

  > Bạn phải viết một giải pháp có độ phức tạp thời gian O(log(m \* n)).

## 1. Cách giải với độ phức tạp O(m \* n)

### 1.1 Linear Search

**Ý tưởng:**
Duyệt tuần tự qua từng phần tử trong ma trận để tìm target.

**Cách hoạt động:**

1. Duyệt qua từng hàng trong ma trận
2. Với mỗi hàng, duyệt qua từng phần tử
3. Nếu tìm thấy target, trả về true
4. Nếu duyệt hết ma trận mà không tìm thấy, trả về false

**Độ phức tạp:**

- Thời gian: O(m \* n) - trong trường hợp xấu nhất phải duyệt qua toàn bộ ma trận
- Không gian: O(1) - chỉ sử dụng một số biến cố định

```python
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        for row in matrix:
            for val in row:
                if val == target:
                    return True
        return False
```

## 2. Các cách giải với độ phức tạp O(log(m \* n))

### 2.1 Binary Search

**Ý tưởng:**
Coi ma trận 2D như một mảng 1D đã được sắp xếp và áp dụng binary search. Sử dụng phép toán số học để chuyển đổi giữa chỉ số 1D và tọa độ 2D.

**Cách hoạt động:**

1. Khởi tạo `left = 0` và `right = (rows * cols) - 1`
2. Trong khi `left <= right`:
   - Tính chỉ số giữa: `mid = left + (right - left) // 2`
   - Chuyển đổi chỉ số 1D sang tọa độ 2D:
     - Hàng: `mid // cols`
     - Cột: `mid % cols`
   - Lấy giá trị tại vị trí đó: `val = matrix[mid // cols][mid % cols]`
   - Nếu `val == target`: trả về true
   - Nếu `val < target`: tìm ở nửa phải, `left = mid + 1`
   - Nếu `val > target`: tìm ở nửa trái, `right = mid - 1`
3. Nếu không tìm thấy, trả về false

**Độ phức tạp:**

- Thời gian: O(log(m \* n)) - binary search chuẩn
- Không gian: O(1) - chỉ sử dụng một số biến cố định

```python
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, (rows * cols) - 1

        while left <= right:
            mid = left + (right - left) // 2
            val = matrix[mid // cols][mid % cols]

            if val == target:
                return True
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
```

### 2.2 Binary Search Upper Bound

**Ý tưởng:**
Tìm vị trí đầu tiên có giá trị lớn hơn target (upper bound), sau đó kiểm tra phần tử trước đó có phải là target không.

**Cách hoạt động:**

1. Khởi tạo `left = 0`, `right = rows * cols` (lưu ý: right = tổng số phần tử)
2. Trong khi `left < right`:
   - Tính `mid = left + (right - left) // 2`
   - Chuyển đổi chỉ số sang tọa độ 2D để lấy giá trị
   - Nếu `val <= target`: tìm ở nửa phải, `left = mid + 1`
   - Nếu `val > target`: tìm ở nửa trái, `right = mid`
3. Sau vòng lặp, `left` là vị trí đầu tiên > target
4. Nếu `left == 0`: target nhỏ hơn tất cả phần tử, trả về false
5. Kiểm tra phần tử tại `left - 1` có bằng target không

**Độ phức tạp:**

- Thời gian: O(log(m \* n)) - binary search chuẩn
- Không gian: O(1) - chỉ sử dụng một số biến cố định

```python
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, (rows * cols)

        while left < right:
            mid = left + (right - left) // 2
            val = matrix[mid // cols][mid % cols]

            if val <= target:
                left = mid + 1
            else:
                right = mid

        if left == 0:
            return False
        return matrix[(left - 1) // cols][(left - 1) % cols] == target
```

### 2.3 Binary Search Lower Bound

**Ý tưởng:**
Tìm vị trí đầu tiên có giá trị lớn hơn hoặc bằng target (lower bound), sau đó kiểm tra phần tử đó có phải là target không.

**Cách hoạt động:**

1. Khởi tạo `left = 0`, `right = rows * cols`
2. Trong khi `left < right`:
   - Tính `mid = left + (right - left) // 2`
   - Chuyển đổi chỉ số sang tọa độ 2D để lấy giá trị
   - Nếu `val < target`: tìm ở nửa phải, `left = mid + 1`
   - Nếu `val >= target`: tìm ở nửa trái, `right = mid`
3. Sau vòng lặp, `left` là vị trí đầu tiên >= target
4. Nếu `left == rows * cols`: target lớn hơn tất cả phần tử, trả về false
5. Kiểm tra phần tử tại `left` có bằng target không

**Độ phức tạp:**

- Thời gian: O(log(m \* n)) - binary search chuẩn
- Không gian: O(1) - chỉ sử dụng một số biến cố định

```python
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, (rows * cols)

        while left < right:
            mid = left + (right - left) // 2
            val = matrix[mid // cols][mid % cols]

            if val < target:
                left = mid + 1
            else:
                right = mid

        if left == (rows * cols):
            return False
        return matrix[left // cols][left % cols] == target
```
