# 287. Find the Duplicate Number

- Cho một mảng `nums` chứa `n + 1` số nguyên, trong đó mỗi số nguyên nằm trong phạm vi từ `1` đến `n` (bao gồm cả hai đầu). Giả sử rằng có một số nguyên duy nhất bị lặp lại trong mảng, hãy tìm và trả về số nguyên đó.

## 1. Các cách giải với độ phức tạp O(N)

### 1.1 Set

**Ý tưởng:** Sử dụng một tập hợp (set) để theo dõi các số đã gặp. Khi gặp một số đã có trong tập hợp, đó chính là số bị lặp lại.

**Cách hoạt động:**

1. Khởi tạo một tập hợp rỗng.
2. Duyệt qua từng số trong mảng `nums`.
3. Nếu số đó đã có trong tập hợp, trả về số đó.
4. Nếu không, thêm số đó vào tập hợp.

**Độ phức tạp:**

- Thời gian: O(N)
- Không gian: O(N)

```python
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
```

### 1.2 Hash Map

**Ý tưởng:** Sử dụng một từ điển (hash map) để đếm số lần xuất hiện của mỗi số. Khi một số xuất hiện lần thứ hai, đó chính là số bị lặp lại.

**Cách hoạt động:**

1. Khởi tạo một từ điển rỗng.
2. Duyệt qua từng số trong mảng `nums`.
3. Nếu số đó đã có trong từ điển, trả về số đó.
4. Nếu không, thêm số đó vào từ điển với giá trị đếm là 1.

**Độ phức tạp:**

- Thời gian: O(N)
- Không gian: O(N)

```python
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count_map = {}
        for num in nums:
            if num in count_map:
                return num
            count_map[num] = 1
```

### 1.3 Fast and Slow Pointers (Floyd's Tortoise and Hare)

**Ý tưởng:** Sử dụng hai con trỏ di chuyển với tốc độ khác nhau để phát hiện chu kỳ trong mảng, tương tự như thuật toán Floyd's Tortoise and Hare.

**Cách hoạt động:**

1. Khởi tạo hai con trỏ `slow` và `fast`, cả hai đều bắt đầu từ vị trí đầu tiên của mảng.
2. Di chuyển con trỏ `slow` một bước mỗi lần và con trỏ `fast` hai bước mỗi lần cho đến khi chúng gặp nhau.
3. Khi hai con trỏ gặp nhau, đặt một con trỏ mới `finder` tại vị trí đầu tiên của mảng và di chuyển cả `finder` và `slow` một bước mỗi lần cho đến khi chúng gặp nhau lần nữa. Vị trí gặp nhau này chính là số bị lặp lại.

**Độ phức tạp:**

- Thời gian: O(N)
- Không gian: O(1)

```python
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Phase 1: Finding the intersection point in the cycle
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Phase 2: Finding the entrance to the cycle
        finder = nums[0]
        while finder != slow:
            finder = nums[finder]
            slow = nums[slow]

        return finder
```
