# 424. Longest Repeating Character Replacement

- Bạn được cho một chuỗi s và một số nguyên k. Bạn có thể chọn bất kỳ ký tự nào trong chuỗi và thay đổi nó thành bất kỳ ký tự tiếng Anh viết hoa nào khác. Bạn có thể thực hiện thao tác này tối đa k lần.

  > Hãy trả về độ dài của chuỗi con dài nhất chứa cùng một chữ cái mà bạn có thể nhận được sau khi thực hiện các thao tác trên.

## 1. Các cách giải với độ phức tạp O(n²)

### 1.1 Brute Force - Time Limit Exceeded !!!

**Ý tưởng:**

Duyệt qua tất cả các cửa sổ con có thể có trong chuỗi, với mỗi cửa sổ con kiểm tra xem có thể tạo thành chuỗi ký tự giống nhau hay không với tối đa k lần thay đổi.

**Cách hoạt động:**

- Với mỗi vị trí bắt đầu i, mở rộng cửa sổ sang phải (j từ i đến cuối chuỗi)
- Theo dõi tần suất xuất hiện của từng ký tự trong cửa sổ hiện tại bằng dictionary `count`
- Tính `max_freq`: tần suất của ký tự xuất hiện nhiều nhất trong cửa sổ
- Số ký tự cần thay đổi = độ dài cửa sổ - max_freq = `(j - i + 1) - max_freq`
- Nếu số ký tự cần thay đổi ≤ k, cập nhật kết quả
- Ngược lại, break vì các cửa sổ lớn hơn sẽ cần nhiều thay đổi hơn

**Độ phức tạp:**

- Thời gian: O(n²)
- Không gian: O(1)

```python
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        for i in range(len(s)):
            max_freq = 0
            count = {}
            for j in range(i, len(s)):
                count[s[j]] = count.get(s[j], 0) + 1
                max_freq = max(max_freq, count[s[j]])
                if j - i + 1 - max_freq <= k:
                    res = max(res, j - i + 1)
                else:
                    break
        return res
```

## 2. Các cách giải với độ phức tạp O(n)

### 2.1 Hashmap

**Ý tưởng:**

Sử dụng kỹ thuật **Sliding Window** với hai con trỏ left và right. Mở rộng cửa sổ khi hợp lệ, thu nhỏ khi vượt quá k lần thay đổi.

**Cách hoạt động:**

- Di chuyển con trỏ `right` để mở rộng cửa sổ, đồng thời cập nhật tần suất ký tự vào dictionary `count`
- Cập nhật `max_freq`: tần suất lớn nhất của bất kỳ ký tự nào trong cửa sổ hiện tại
- **Điều kiện hợp lệ**: `độ dài của cửa sổ - tần suất lớn nhất ≤ k`
- Khi vi phạm điều kiện (cần > k lần thay đổi), thu nhỏ cửa sổ bằng cách:
  - Giảm tần suất của `s[left]`
  - Tăng `left` để loại ký tự đầu tiên khỏi cửa sổ
- Cập nhật độ dài cửa sổ lớn nhất vào `res`

**Độ phức tạp:**

- Thời gian: O(n)
- Không gian: O(1)

```python
class Solution:
def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left, max_freq, res = 0, 0, 0
        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            max_freq = max(max_freq, count[s[right]])

            while right - left + 1 - max_freq > k:
                count[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)
        return res
```

### 2.2 Array

**Ý tưởng:**

Tương tự phương pháp Hashmap nhưng thay dictionary bằng mảng có kích thước cố định 26 (số ký tự in hoa A-Z) để tối ưu hiệu suất.

**Cách hoạt động:**

- Sử dụng mảng `count[26]` thay vì dictionary để lưu tần suất ký tự
- Chuyển đổi ký tự thành index: `ord(s[i]) - ord('A')` cho index từ 0-25
  - 'A' → 0, 'B' → 1, ..., 'Z' → 25
- Các bước còn lại hoàn toàn giống phương pháp Hashmap:
  - Mở rộng cửa sổ với con trỏ `right`
  - Thu nhỏ cửa sổ khi `(right - left + 1) - max_freq > k`
  - Theo dõi độ dài cửa sổ lớn nhất

**Độ phức tạp:**

- Thời gian: O(n)
- Không gian: O(26)

```python
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        left, max_freq, res = 0, 0, 0
        for right in range(len(s)):
            count[ord(s[right]) - ord('A')] += 1
            max_freq = max(max_freq, count[ord(s[right]) - ord('A')])

            while right - left + 1 - max_freq > k:
                count[ord(s[left]) - ord('A')] -= 1
                left += 1

            res = max(res, right - left + 1)
        return res
```
