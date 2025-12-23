# [15. 3Sum](https://leetcode.com/problems/3sum/)

- Cho một mảng số nguyên `nums`, hãy trả về tất cả các bộ ba `[nums[i], nums[j], nums[k]]` sao cho `i != j`, `i != k`, và `j != k`, và `nums[i] + nums[j] + nums[k] == 0`.
  > Lưu ý rằng tập hợp các kết quả không được chứa các bộ ba trùng lặp.

## 1. Các cách giải với độ phức tạp O(n³)

### 1.1. Brute Force

**Ý tưởng:** Dùng 3 vòng lặp lồng nhau để kiểm tra tất cả các bộ ba có thể.

**Cách hoạt động:**

1. Chọn phần tử đầu tiên trong mảng
2. Với mỗi phần tử đầu tiên, chọn phần tử thứ hai ở phía sau nó
3. Với mỗi cặp phần tử đầu và thứ hai, chọn phần tử thứ ba ở phía sau phần tử thứ hai
4. Kiểm tra tổng của ba phần tử có bằng 0 không, nếu có thì lưu lại
5. Sử dụng tập hợp để loại bỏ các bộ ba trùng lặp

**Độ phức tạp:**

- Thời gian: O(n³)
- Không gian: O(n)

<details open>
<summary><b>🐍 Python Version</b> (Click để đóng)</summary>

```python
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        res = set()
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                        res.add(triplet)
        return list(res)
```

</details>

---

## 2. Các cách giải với độ phức tạp O(n²)

### 2.1. Hash Set

**Ý tưởng:** Cố định một phần tử, sau đó dùng hash set để tìm hai phần tử còn lại (biến bài toán thành Two Sum).

**Cách hoạt động:**

1. Xử lý trường hợp đặc biệt: nếu mảng toàn số 0 thì trả về kết quả ngay
2. Chọn phần tử đầu tiên làm điểm cố định
3. Với mỗi phần tử đầu tiên, tạo một bảng băm để lưu các phần tử đã gặp
4. Duyệt qua các phần tử phía sau:
   - Tính giá trị cần tìm để tổng ba số bằng 0
   - Nếu giá trị cần tìm có trong bảng băm, ta tìm được bộ ba hợp lệ
   - Thêm bộ ba vào kết quả (sử dụng tập hợp để tránh trùng lặp)
   - Lưu phần tử hiện tại vào bảng băm

**Độ phức tạp:**

- Thời gian: O(n²)
- Không gian: O(n)

<details open>
<summary><b>🐍 Python Version</b> (Click để đóng)</summary>

```python
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        if set(nums) == {0}:
            return [[0,0,0]]

        seen_triplets = set()
        n = len(nums)
        res = []
        for i in range(n - 2):
            seen = {}
            for j in range(i + 1, n):
                current = nums[j]
                target = - current - nums[i]
                if target in seen:
                    triplets = tuple(sorted([current, target, nums[i]]))
                    if triplets not in seen_triplets:
                        res.append(triplets)
                        seen_triplets.add(triplets)
                seen[current] = j
        return res
```

</details>

---

### 2.2. Two Pointers

**Ý tưởng:** Sắp xếp mảng trước, sau đó cố định một phần tử và dùng kỹ thuật two pointers để tìm hai phần tử còn lại.

**Cách hoạt động:**

1. Sắp xếp mảng tăng dần
2. Chọn phần tử đầu tiên làm điểm cố định:
   - Bỏ qua các phần tử trùng lặp liên tiếp
   - Đặt con trỏ trái ngay sau phần tử cố định
   - Đặt con trỏ phải ở cuối mảng
3. Sử dụng hai con trỏ để tìm cặp còn lại:
   - Tính tổng ba phần tử
   - Nếu tổng bằng 0: tìm được bộ ba hợp lệ, lưu kết quả và di chuyển cả hai con trỏ
     - Bỏ qua các giá trị trùng lặp khi di chuyển con trỏ
   - Nếu tổng nhỏ hơn 0: di chuyển con trỏ trái sang phải (tăng tổng)
   - Nếu tổng lớn hơn 0: di chuyển con trỏ phải sang trái (giảm tổng)

**Độ phức tạp:**

- Thời gian: O(n²)
- Không gian: O(1)

<details open>
<summary><b>🐍 Python Version</b> (Click để đóng)</summary>

```python
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = -nums[i]
            left = i + 1
            right = n - 1
            while left < right:
                sum = nums[left] + nums[right]
                if sum == target:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif sum < target:
                    left += 1
                elif sum > target:
                    right -= 1
        return res
```

</details>
