# 33. Search in Rotated Sorted Array

- Có một mảng số nguyên nums được sắp xếp theo thứ tự tăng dần (với các giá trị riêng biệt).

  Trước khi được truyền vào hàm, nums có thể được xoay tại một chỉ số pivot không xác định k (1 <= k < nums.length) sao cho mảng kết quả là [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (indexed từ 0). Ví dụ, [0,1,2,4,5,6,7] có thể được xoay tại chỉ số pivot 3 và trở thành [4,5,6,7,0,1,2].

  Cho mảng nums sau khi có thể đã bị xoay và một số nguyên target, trả về chỉ số của target nếu nó có trong nums, hoặc -1 nếu không có.

  > Bạn phải viết một thuật toán có độ phức tạp thời gian O(log n).

## 1. Cách giải với độ phức tạp O(n)

### 1.1 Linear Search

**Ý tưởng:**
Duyệt tuần tự qua từng phần tử trong mảng để tìm target.

**Cách hoạt động:**

1. Duyệt qua từng phần tử trong mảng với chỉ số i
2. Nếu `nums[i] == target`, trả về i
3. Nếu duyệt hết mảng mà không tìm thấy, trả về -1

**Độ phức tạp:**

- Thời gian: O(n) - trong trường hợp xấu nhất phải duyệt qua toàn bộ n phần tử
- Không gian: O(1) - chỉ sử dụng một số biến cố định

```python
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        for i, num in enumerate(nums):
            if num == target:
                return i
        return -1
```

## 2. Cách giải với độ phức tạp O(log n)

### 2.1 Binary Search

**Ý tưởng:**
Sử dụng binary search với logic đặc biệt: xác định nửa nào được sắp xếp, sau đó kiểm tra target có nằm trong nửa đó không để quyết định hướng tìm kiếm.

**Cách hoạt động:**

1. Khởi tạo `left = 0`, `right = len(nums) - 1`
2. Trong khi `left <= right`:
   - Tính `mid = left + (right - left) // 2`
   - Nếu `nums[mid] == target`: trả về mid
   - Xác định nửa nào được sorted:
     - **Nếu nửa trái sorted** (`nums[left] <= nums[mid]`):
       - Nếu `nums[left] <= target < nums[mid]`: target trong đoạn sorted bên trái
         - `right = mid - 1`
       - Ngược lại: target ở bên phải
         - `left = mid + 1`
     - **Nếu nửa phải sorted** (ngược lại):
       - Nếu `nums[mid] < target <= nums[right]`: target trong đoạn sorted bên phải
         - `left = mid + 1`
       - Ngược lại: target ở bên trái
         - `right = mid - 1`
3. Nếu không tìm thấy, trả về -1

**Độ phức tạp:**

- Thời gian: O(log n)
- Không gian: O(1)

```python
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid

            # Kiểm tra nửa trái có sorted không
            if nums[left] <= nums[mid]:
                # Nửa trái sorted
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # Nửa phải sorted
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1
```
