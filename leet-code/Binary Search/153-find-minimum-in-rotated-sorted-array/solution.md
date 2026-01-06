# 153. Find Minimum in Rotated Sorted Array

- Cho một mảng có độ dài n được sắp xếp theo thứ tự tăng dần, sau đó được xoay từ 1 đến n lần. Ví dụ, mảng nums = [0,1,2,4,5,6,7] có thể trở thành:

  - [4,5,6,7,0,1,2] nếu xoay 4 lần.
  - [0,1,2,4,5,6,7] nếu xoay 7 lần.

  Cho một mảng số nguyên nums được sắp xếp theo thứ tự tăng dần và có thể đã được xoay, hãy trả về phần tử nhỏ nhất của mảng này.

  > Bạn phải viết một thuật toán chạy trong thời gian O(log n).

## 1. Cách giải với độ phức tạp O(n)

### 1.1 Linear Search

**Ý tưởng:**
Duyệt tuần tự qua từng phần tử trong mảng và tìm giá trị nhỏ nhất.

**Cách hoạt động:**

1. Khởi tạo biến `res = float('inf')` để lưu giá trị nhỏ nhất
2. Duyệt qua từng phần tử trong mảng
3. Cập nhật `res` bằng giá trị nhỏ hơn giữa `res` và phần tử hiện tại
4. Trả về `res`

**Độ phức tạp:**

- Thời gian: O(n) - phải duyệt qua toàn bộ n phần tử
- Không gian: O(1) - chỉ sử dụng một số biến cố định

```python
class Solution:
    def findMin(self, nums: list[int]) -> int:
        res = float('inf')
        for num in nums:
            res = min(res, num)
        return res
```

## 2. Cách giải với độ phức tạp O(log n)

### 2.1 Binary Search

**Ý tưởng:**
Tận dụng tính chất của rotated sorted array: mảng được chia thành 2 phần sorted. Sử dụng binary search để tìm điểm "break" (pivot point) nơi phần tử nhỏ nhất nằm.

**Cách hoạt động:**

1. Trường hợp đặc biệt: Nếu `nums[left] < nums[right]`, mảng không bị rotate, trả về `nums[left]`
2. Khởi tạo `left = 0`, `right = len(nums) - 1`
3. Trong khi `left < right`:
   - Tính `mid = left + (right - left) // 2`
   - Nếu `nums[mid] > nums[right]`:
     - Phần tử nhỏ nhất ở bên phải
     - `left = mid + 1`
   - Ngược lại:
     - Phần tử nhỏ nhất ở bên trái hoặc là mid
     - `right = mid`
4. Trả về `nums[left]`

**Độ phức tạp:**

- Thời gian: O(log n)
- Không gian: O(1)

```python
class Solution:
    def findMin(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1

        # Nếu mảng không bị rotate
        if nums[left] < nums[right]:
            return nums[left]

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[right]:
                # Min ở bên phải
                left = mid + 1
            else:
                # Min ở bên trái hoặc là mid
                right = mid

        return nums[left]
```
