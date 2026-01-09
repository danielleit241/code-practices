# 4. Median of Two Sorted Arrays

- Cho hai mảng đã được sắp xếp `nums1` và `nums2` có kích thước lần lượt là `m` và `n`, hãy trả về trung vị của hai mảng đã sắp xếp.

  > Độ phức tạp thời gian chạy tổng thể phải là O(log (m+n)).

## 1. Các cách giải với độ phức tạp O((m+n)log(m+n))

### 1.1 Sử dụng hàm có sẵn (Sorted1)

**Ý tưởng:**
Kết hợp và sắp xếp hai mảng, sau đó sử dụng hàm `median()` có sẵn trong Python để tính trung vị.

**Cách hoạt động:**

1. Kết hợp hai mảng `nums1` và `nums2` thành một mảng
2. Sắp xếp mảng kết hợp
3. Sử dụng hàm `statistics.median()` để tính trung vị

**Độ phức tạp:**

- Thời gian: O((m+n)log(m+n)) - do sắp xếp
- Không gian: O(m+n) - cho mảng kết hợp

```python
class Solution:
    def findMedianSortedArrays_Sorted1(self, nums1: list[int], nums2: list[int]) -> float:
        return median(sorted(nums1 + nums2))
```

### 1.2 Sắp xếp và tính trung vị thủ công (Sorted2)

**Ý tưởng:**
Kết hợp và sắp xếp hai mảng, sau đó tính trung vị theo cách thủ công dựa vào độ dài mảng.

**Cách hoạt động:**

1. Kết hợp và sắp xếp hai mảng `nums1` và `nums2`
2. Tính chỉ số giữa: `mid = length // 2`
3. Nếu độ dài mảng là số chẵn: trả về trung bình cộng của hai phần tử giữa
4. Nếu độ dài mảng là số lẻ: trả về phần tử ở giữa

**Độ phức tạp:**

- Thời gian: O((m+n)log(m+n)) - do sắp xếp
- Không gian: O(m+n) - cho mảng kết hợp

```python
class Solution:
    def findMedianSortedArrays_Sorted2(self, nums1: list[int], nums2: list[int]) -> float:
        nums = sorted(nums1 + nums2)
        length = len(nums)
        mid = length // 2

        if length % 2 == 0:
            return (nums[mid - 1] + nums[mid]) / 2.0
        else:
            return nums[mid]
```

## 2. Các cách giải với độ phức tạp O(m+n)

### 2.1 Merge hai mảng đã sắp xếp

**Ý tưởng:**
Tận dụng tính chất hai mảng đã được sắp xếp để merge chúng thành một mảng duy nhất theo thứ tự, sau đó tính trung vị.

**Cách hoạt động:**

1. Khởi tạo hai con trỏ `i = 0` và `j = 0` cho hai mảng
2. So sánh từng phần tử của hai mảng và thêm phần tử nhỏ hơn vào mảng `merged`:
   - Nếu `nums1[i] < nums2[j]`: thêm `nums1[i]` và tăng `i`
   - Ngược lại: thêm `nums2[j]` và tăng `j`
3. Thêm các phần tử còn lại (nếu có) từ mảng chưa duyệt hết
4. Tính trung vị từ mảng đã merge:
   - Nếu độ dài là số chẵn: `(merged[mid-1] + merged[mid]) / 2`
   - Nếu độ dài là số lẻ: `merged[mid]`

**Độ phức tạp:**

- Thời gian: O(m+n) - duyệt qua cả hai mảng một lần
- Không gian: O(m+n) - cho mảng merged

```python
class Solution:
    def findMedianSortedArrays_Merge(self, nums1: list[int], nums2: list[int]) -> float:
        merged = []
        i, j = 0, 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1

        while i < len(nums1):
            merged.append(nums1[i])
            i += 1
        while j < len(nums2):
            merged.append(nums2[j])
            j += 1

        length = len(merged)
        mid = length // 2
        if length % 2 == 0:
            return (merged[mid - 1] + merged[mid]) / 2.0
        else:
            return merged[mid]
```

## 3. Các cách giải với độ phức tạp O(log(min(m,n)))

### 3.1 Binary Search (Tối ưu - TODO)

**Ý tưởng:**
Để đạt được độ phức tạp O(log(m+n)), cần sử dụng binary search trên mảng nhỏ hơn để phân vùng hai mảng sao cho:

- Phân vùng bên trái có (m+n+1)/2 phần tử
- Tất cả phần tử ở phân vùng trái ≤ tất cả phần tử ở phân vùng phải

**Cách hoạt động:**

1. Đảm bảo `nums1` là mảng nhỏ hơn (nếu không, hoán đổi)
2. Sử dụng binary search trên `nums1` để tìm điểm phân vùng hợp lệ
3. Với mỗi phân vùng của `nums1`, tính phân vùng tương ứng của `nums2`
4. Kiểm tra điều kiện: `maxLeft1 <= minRight2` và `maxLeft2 <= minRight1`
5. Tính trung vị dựa trên các giá trị tại điểm phân vùng

**Độ phức tạp:**

- Thời gian: O(log(min(m,n))) - binary search trên mảng nhỏ hơn
- Không gian: O(1) - chỉ sử dụng một số biến cố định
