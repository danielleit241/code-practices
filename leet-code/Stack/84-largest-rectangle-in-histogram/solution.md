# 84. Largest Rectangle in Histogram

- Cho một mảng các số nguyên height biểu thị chiều cao của các cột trong biểu đồ tần số, trong đó chiều rộng của mỗi cột là 1, hãy trả về diện tích của hình chữ nhật lớn nhất trong biểu đồ tần số đó.

## 1. Các cách giải với độ phức tạp O(n²)

### 1.1 Brute Force

**Ý tưởng:**

Duyệt qua tất cả các cặp chỉ số (i, j) có thể có và tính diện tích hình chữ nhật với chiều cao là giá trị nhỏ nhất trong khoảng [i, j] và chiều rộng là (j - i + 1).

**Cách hoạt động:**

1. Sử dụng 2 vòng lặp lồng nhau để duyệt qua tất cả các cặp (i, j)
2. Với mỗi cặp, tìm chiều cao nhỏ nhất trong khoảng từ i đến j
3. Tính diện tích = chiều cao nhỏ nhất × chiều rộng
4. Cập nhật diện tích lớn nhất

**Độ phức tạp:**

- Thời gian: O(n²) - hai vòng lặp lồng nhau
- Không gian: O(1) - chỉ sử dụng các biến phụ

```python
class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        n = len(heights)
        res = 0
        for i in range(n):
            min_height = heights[i]
            for j in range(i, n):
                min_height = min(min_height, heights[j])
                res = max(res, min_height * (j - i + 1))
        return res
```

## 2. Các cách giải với độ phức tạp O(n)

### 2.1 Stack

**Ý tưởng:**

Sử dụng stack để lưu trữ các chỉ số của các cột theo thứ tự tăng dần về chiều cao. Khi gặp một cột có chiều cao thấp hơn, ta tính diện tích của các hình chữ nhật có thể tạo thành với các cột trước đó.

**Cách hoạt động:**

1. Duyệt qua từng cột trong mảng heights
2. Nếu cột hiện tại thấp hơn cột ở đỉnh stack:
   - Pop các cột cao hơn ra khỏi stack
   - Với mỗi cột được pop, tính diện tích hình chữ nhật:
     - Chiều cao = heights[index_được_pop]
     - Chiều rộng = khoảng cách từ cột hiện tại đến cột trước đó trong stack
   - Cập nhật diện tích lớn nhất
3. Push chỉ số cột hiện tại vào stack
4. Sau khi duyệt xong, xử lý các cột còn lại trong stack tương tự

**Độ phức tạp:**

- Thời gian: O(n) - mỗi phần tử được push và pop tối đa 1 lần
- Không gian: O(n) - stack có thể chứa tối đa n phần tử

```python
class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []
        res = 0
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                res = max(res, height * width)
            stack.append(i)

        n = len(heights)
        while stack:
            height = heights[stack.pop()]
            width = n if not stack else n - stack[-1] - 1
            res = max(res, height * width)

        return res
```

### 2.2 Optimize Stack

**Ý tưởng:**

Tối ưu hóa phương pháp stack bằng cách thêm một cột có chiều cao 0 vào cuối mảng. Điều này giúp loại bỏ vòng lặp xử lý các phần tử còn lại trong stack sau khi duyệt hết mảng.

**Cách hoạt động:**

1. Thêm giá trị 0 vào cuối mảng heights để đảm bảo tất cả các cột trong stack đều được xử lý
2. Duyệt qua từng cột (bao gồm cả cột 0 cuối cùng)
3. Khi gặp cột thấp hơn đỉnh stack, pop và tính diện tích tương tự như cách 2.1
4. Do có cột 0 ở cuối, tất cả các cột còn lại sẽ được xử lý trong vòng lặp chính

**Độ phức tạp:**

- Thời gian: O(n) - mỗi phần tử được xử lý đúng 1 lần
- Không gian: O(n) - stack và việc thêm 1 phần tử vào mảng

```python
class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []
        heights.append(0)
        res = 0
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                res = max(res, height * width)
            stack.append(i)

        return res
```
