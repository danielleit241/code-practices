# 1. Two sum

- Cho một mảng các số nguyên nums và một số nguyên target, hãy trả về chỉ số của hai số đó sao cho tổng của chúng bằng target.
  > Bạn có thể giả định rằng mỗi đầu vào sẽ có chính xác một lời giải, và bạn không được sử dụng cùng một phần tử hai lần.

## 1. Các cách giải với độ phức tạp O(n²)

### 1.1. BruteForce

**Ý tưởng:** Dùng 2 vòng lặp lồng nhau để so sánh từng cặp phần tử trong mảng.

**Cách hoạt động:**

1. Duyệt qua từng phần tử `i` trong mảng
2. Với mỗi phần tử `i`, so sánh nó với tất cả các phần tử phía sau `j` (j > i)
3. Nếu cặp `nums[i] + nums[j] == target` thì trả về `True`, ngược lại trả về `False`

**Độ phức tạp:**

- Thời gian:

  - Best O(1) - Tìm thấy ngay ở cặp đầu tiên
  - Worst O(n²)

- Không gian: O(1)

```python
class Solution:
    def twoSum_Br(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
```

## 2. Các cách giải với độ phức tạp O(n log n)

### 2.1 Sort + Two pointers

**Ý tưởng:** Sort các giá trị trong mảng mà vẫn đảm bảo được thứ tự ban đầu sau đó dùng 2 con trỏ kiểm tra `trái` và `phải`

**Cách hoạt động:**

1. Sort các giá trị trong mảng ban đầu -> mà vẫn đảm bảo giữ nguyên vị trí của giá trị đó
2. Áp dụng two pointer đặt `left = 0` và `right = len(nums) - 1`
3. Kiểm tra nếu `nums[left][0] + nums[right][0]` so sánh với `target`
   - Nếu bằng `target` thì trả về vị trí của giá trị `left` và `right`
   - Nếu nhỏ hơn thì tăng `left` lên 1
   - Nếu lớn hơn thì giảm `right` về 1
   - Cho đến khi tìm được giá trị thoải mãn

**Độ phức tạp:**

- Thời gian: O(nlogn) - Timsort luôn luôn ổn định trong mọi trường hợp
- Không gian: O(n)

```python
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums = sorted([(num, i) for i, num in enumerate(nums)])
        left = 0
        right = len(nums) - 1
        while left < right:
            current_sum = nums[left][0] + nums[right][0]
            if current_sum == target:
                return [nums[left][1], nums[right][1]]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
```

## 3. Các cách giải với độ phức tạp O(n)

### 3.1 Hashmap

#### 3.1.1 Two pass

**Ý tưởng:**

- Duyệt mảng số nguyên ban đầu 2 lần
  - Lần 1: Lưu toàn bộ giá trị và index vào Hashmap
  - Lần 2: Tìm phần bù và kiểm tra phần bù có tồn tại trong Hashmap không?

**Cách hoạt động:**

1. Duyệt mảng lần đầu lưu key: nums[i] - value: i
2. Duyệt mảng lần thứ hai:

   - Tính `phần bù = target - nums[i]`
   - Kiểm tra phần bù có trong hashmap ban đầu không và đảm bảo không dùng lại cùng giá trị tại vị trí i ban đầu

3. Nếu thỏa mãn thì trả về `i và map[phần-bù]`

**Độ phức tạp:**

- Thời gian: O(n)
- Không gian: O(n)

```python
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        map = {}
        for i, num in enumerate(nums):
            map[num] = i

        for i, num in enumerate(nums):
            complement = target - num
            if complement in map and map[complement] != i:
                return [i, map[complement]]
```

#### 3.1.2 One pass

**Ý tưởng**: Cách hoạt động tương tự như với `two pass` nhưng thay vì ta duyệt mảng hai lần thì lúc này ta vừa duyệt mảng, vừa kiểm tra phần tử bù trong cùng một vòng lặp.

```python
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in map:
                return [map[complement], i]
            map[num] = i
```

- Điểm khác nhau giữa `one pass` và `two pass`:
  - Ta sẽ dùng một vòng lặp thay vì hai -> giúp cho hiệu năng tốt hơn
