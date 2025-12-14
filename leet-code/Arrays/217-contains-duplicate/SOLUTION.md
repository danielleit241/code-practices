# 217. Contains Duplicate

## 1. Các cách giải với độ phức tạp O(n²)

### 1.1. BruteForce

**Ý tưởng:** Dùng 2 vòng lặp lồng nhau để so sánh từng cặp phần tử trong mảng.

**Cách hoạt động:**

1. Duyệt qua từng phần tử `i` trong mảng
2. Với mỗi phần tử `i`, so sánh nó với tất cả các phần tử phía sau `j` (j > i)
3. Nếu tìm thấy 2 phần tử giống nhau thì trả về `True`, ngược lại trả về `False`

**Độ phức tạp:**

- Thời gian: O(n²) - vì có 2 vòng lặp lồng nhau
- Không gian: O(1) - không dùng thêm bộ nhớ phụ

```python
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    return True
        return False
```

---

### 1.2. Count

**Ý tưởng:** Sử dụng phương thức `count()` của Python để đếm số lần xuất hiện của từng phần tử.

**Cách hoạt động:**

1. Duyệt qua từng phần tử trong mảng
2. Sử dụng `count()` để đếm số lần phần tử đó xuất hiện
3. Nếu phần tử nào xuất hiện nhiều hơn 1 lần thì trả về `True`, ngược lại trả về `False`

**Độ phức tạp:**

- Thời gian: O(n²) - vì `count()` phải duyệt qua toàn bộ mảng cho mỗi phần tử
- Không gian: O(1) - không dùng thêm bộ nhớ phụ

```python
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        for num in nums:
            if nums.count(num) > 1:
                return True
        return False
```

---

## 2. Các cách giải với độ phức tạp O(n log n)

### 2.1. Sorting

**Ý tưởng:** Sắp xếp mảng trước, sau đó các phần tử trùng nhau sẽ nằm cạnh nhau.

**Cách hoạt động:**

1. Sắp xếp mảng theo thứ tự tăng dần
2. Duyệt qua mảng đã sắp xếp
3. So sánh mỗi phần tử với phần tử liền trước nó, nếu tồn tại thì trả về `True` ngược lại thì trả về `False`

**Độ phức tạp:**

- Thời gian: O(n log n) - do thuật toán sắp xếp (Timsort trong Python)
- Không gian: O(1) hoặc O(n) - tùy thuộc vào việc `sort()` có sắp xếp tại chỗ hay không

```python
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False
```

---

## 3. Các cách giải với độ phức tạp O(n)

### 3.1. Set

**Ý tưởng:** Sử dụng Set để lưu các phần tử đã gặp, vì Set không cho phép phần tử trùng lặp.

**Cách 1: Duyệt và kiểm tra**

**Cách hoạt động:**

1. Tạo một Set rỗng để lưu các phần tử đã thấy
2. Duyệt qua từng phần tử trong mảng
3. Nếu phần tử đã có trong Set, nghĩa là đã gặp trước đó → trả về `True`
   - Nếu chưa có, thêm phần tử vào Set
   - Nếu duyệt hết mảng mà không tìm thấy trùng lặp, trả về `False`

**Độ phức tạp:**

- Thời gian: O(n) - duyệt qua mảng 1 lần, tra cứu Set là O(1)
- Không gian: O(n) - trong trường hợp xấu nhất lưu tất cả phần tử vào Set

```python
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
```

**Cách 2: So sánh độ dài**

**Cách hoạt động:**

1. Chuyển mảng thành Set (loại bỏ các phần tử trùng lặp)
2. So sánh độ dài của mảng gốc với độ dài của Set
   - Nếu độ dài khác nhau → có phần tử trùng lặp → trả về `True`
   - Nếu độ dài bằng nhau → không có trùng lặp → trả về `False`

**Độ phức tạp:**

- Thời gian: O(n) - tạo Set từ mảng
- Không gian: O(n) - lưu trữ Set

```python
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(nums) != len(set(nums))
```

---

### 3.2. Hashmap

**Ý tưởng:** Sử dụng Dictionary (Hashmap) để theo dõi các phần tử đã gặp.

**Cách hoạt động:**

1. Tạo một Dictionary rỗng
2. Duyệt qua từng phần tử trong mảng
   - Nếu phần tử đã tồn tại trong Dictionary → trả về `True`
   - Nếu chưa có, thêm phần tử vào Dictionary với giá trị là 1
3. Nếu duyệt hết mảng mà không tìm thấy trùng lặp, trả về `False`

**Độ phức tạp:**

- Thời gian: O(n) - duyệt qua mảng 1 lần, tra cứu Dictionary là O(1)
- Không gian: O(n) - trong trường hợp xấu nhất lưu tất cả phần tử vào Dictionary

```python
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        num_count = {}
        for num in nums:
            if num in num_count:
                return True
            num_count[num] = 1
        return False
```

---

## Lưu ý

> **Performance:** Việc sử dụng **Set** sẽ nhanh hơn **Hashmap** một chút mặc dù cả hai đều có độ phức tạp O(n), vì Set chỉ lưu key thay vì lưu cả key + value như Hashmap.
