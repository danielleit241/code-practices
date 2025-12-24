# [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

- Cho một chuỗi s, tìm độ dài của chuỗi con dài nhất không có ký tự lặp lại.

## 1. Các cách giải với độ phức tạp O(n²)

### 1.1. BruteForce - O(n²)

**Ý tưởng:** Kiểm tra tất cả các chuỗi con có thể và tìm chuỗi con dài nhất không có ký tự lặp lại.

**Cách hoạt động:**

1. Duyệt qua từng vị trí bắt đầu i
2. Với mỗi vị trí i, sử dụng set để theo dõi các ký tự đã gặp
3. Mở rộng chuỗi con sang phải cho đến khi gặp ký tự lặp lại
4. Cập nhật độ dài tối đa và chuyển sang vị trí bắt đầu tiếp theo

**Độ phức tạp:**

- Thời gian: O(n²)
- Không gian: O(m) - với m là kích thước bảng chữ cái

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            seen = set()
            for j in range(i, len(s)):
                if s[j] in seen:
                    break
                seen.add(s[j])
            res = max(res, j - i)
        return res
```

## 2. Các cách giải với độ phức tạp O(n)

### 2.1. Sliding Window với Set

**Ý tưởng:** Sử dụng kỹ thuật sliding window với hai con trỏ left và right, mở rộng window khi không có lặp và thu hẹp khi có lặp.

**Cách hoạt động:**

1. Khởi tạo `left = 0`, `max_length = 0` và một `set` để lưu các ký tự trong window
2. Duyệt qua chuỗi với con trỏ `right`:
   - Nếu `s[right]` chưa có trong set:
     - Thêm vào set
     - Cập nhật `max_length`
     - Di chuyển `right` sang phải
   - Nếu `s[right]` đã có trong set (ký tự lặp):
     - Xóa `s[left]` khỏi set
     - Di chuyển `left` sang phải
     - Lặp lại cho đến khi không còn lặp
3. Trả về `max_length`

**Độ phức tạp:**

- Thời gian: O(n)
- Không gian: O(m) - với m là kích thước bảng chữ cái

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left, right, res = 0, 0, 0
        while right < len(s):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            res = max(res, right - left + 1)
            right += 1
        return res
```

### 2.2. Sliding Window với HashMap

**Ý tưởng:** Sử dụng HashMap để lưu vị trí cuối cùng của mỗi ký tự, cho phép nhảy left pointer nhanh hơn.

**Cách hoạt động:**

1. Khởi tạo `left = 0`, `max_length = 0` và một `dict` để lưu vị trí xuất hiện gần nhất của ký tự
2. Duyệt qua chuỗi với con trỏ `right`:
   - Nếu `s[right]` đã xuất hiện và vị trí của nó >= left:
     - Di chuyển `left` đến vị trí sau vị trí xuất hiện trước đó của `s[right]`
   - Cập nhật vị trí của `s[right]` trong dict
   - Cập nhật `max_length`
3. Trả về `max_length`

**Độ phức tạp:**

- Thời gian: O(n) - chỉ duyệt qua chuỗi một lần
- Không gian: O(min(n, m)) - với m là kích thước bảng chữ cái

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        left, res = 0, 0
        for right in range(len(s)):
            if s[right] in mp:
                left = max(left, mp[s[right]] + 1)
            mp[s[right]] = right
            res = max(res, right - left + 1)
        return res
```
