# [11. Container with most water](https://leetcode.com/problems/container-with-most-water/description/)

## Các cách giải với độ phức tạp O(n²)

### Brute force

**Ý tưởng:** Dùng hai vòng lặp để tìm được maxArea

**Các hoạt động:**

1. Duyệt tất cả các cặp cột (i, j) với i < j
2. Tính diện tích = min(chiều cao i, chiều cao j) × (j - i)
3. Cập nhật diện tích lớn nhất
4. Trả về kết quả

**Độ phức tạp:**

- Thời gian: O(n²)
- Không gian: O(1)

<details open>
<summary><b>🐍 Python Version</b> (Click để đóng)</summary>

```python
class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_area = 0
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                area = min(height[i], height[j]) * (j - i)
                if area > max_area:
                    max_area = area

        return max_area
```

</details>

## Các cách giải với độ phức tạp O(n)

**Ý tưởng:** Dùng hai con trỏ trái phải để tìm kiếm chiều cao lớn nhất cũng như độ rộng lớn nhất

**Cách hoạt động:**

1. Khởi tạo left = 0, right = cuối mảng
2. Tính diện tích = min(height[left], height[right]) × (right - left)
3. Cập nhật diện tích lớn nhất
4. Di chuyển con trỏ có chiều cao thấp hơn (cột thấp hơn là điểm nghẽn)
5. Lặp lại cho đến khi left >= right

**Độ phức tạp:**

- Thời gian: O(n)
- Không gian: O(1)

<details open>
<summary><b>🐍 Python Version</b> (Click để đóng)</summary>

```python
class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            area = min(height[left], height[right]) * (right - left)
            if area > max_area:
                max_area = area

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
```

</details>
