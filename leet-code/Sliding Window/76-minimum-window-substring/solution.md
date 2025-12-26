# 76. Minimum Window Substring

- Cho hai chuỗi s và t có độ dài lần lượt là m và n, hãy trả về chuỗi con cửa sổ nhỏ nhất của s sao cho mọi ký tự trong t (bao gồm cả các ký tự trùng lặp) đều nằm trong cửa sổ đó. Nếu không có chuỗi con nào như vậy, hãy trả về chuỗi rỗng "".

## 1. Các cách giải với độ phức tạp O(n²)

### 1.1. BruteForce

**Ý tưởng:**

- Duyệt qua tất cả các chuỗi con có thể có của s, với mỗi chuỗi con kiểm tra xem nó có chứa đầy đủ các ký tự của t hay không.
- Ghi nhận chuỗi con ngắn nhất thỏa mãn điều kiện.

**Các hoạt động:**

1. Tạo một hashmap `map_t` chứa tần suất của các ký tự trong t.
2. Với mỗi vị trí bắt đầu i từ 0 đến len(s)-1:
   - Tạo một hashmap `window` để đếm tần suất các ký tự trong cửa sổ hiện tại.
   - Với mỗi vị trí kết thúc j từ i đến len(s)-1:
     - Thêm s[j] vào `window`.
     - Kiểm tra nếu cửa sổ [i, j] chứa đầy đủ các ký tự của t với đúng tần suất.
     - Nếu đúng, ghi nhận chuỗi con này nếu nó ngắn hơn kết quả hiện tại và thoát khỏi vòng lặp j.
3. Trả về chuỗi con ngắn nhất tìm được hoặc chuỗi rỗng nếu không tìm thấy.

**Độ phức tạp:**

- Thời gian: O(m² × n) - với m là độ dài của s, n là độ dài của t. Mỗi cặp (i, j) tốn O(n) để kiểm tra.
- Không gian: O(n) - để lưu trữ các hashmap.

```python
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        map_t = {}
        for c in t:
            map_t[c] = map_t.get(c, 0) + 1

        need = len(map_t)
        min_len = float('inf')
        min_start = 0
        for i in range(len(s)):
            window = {}
            matched = 0
            for j in range(i, len(s)):
                c = s[j]
                window[c] = window.get(c, 0) + 1

                if c in map_t and window[c] == map_t[c]:
                    matched += 1

                if matched == need:
                    if j - i + 1 < min_len:
                        min_len = j - i + 1
                        min_start = i
                    break

        return "" if min_len == float('inf') else s[min_start:min_len + min_start]
```

## 2. Các cách giải với độ phức tạp O(n)

### 2.1 Sliding Window

**Ý tưởng:**

- Áp dụng Sliding Window để tìm cửa sổ con trong chuỗi s chứa đầy đủ các ký tự của chuỗi t.
- Khi cửa sổ hợp lệ, ghi nhận kết quả rồi thu hẹp cửa sổ từ bên trái để giữ lại n − 1 ký tự trong t, tiếp tục tìm cửa sổ nhỏ hơn.

**Các hoạt động:**

1. Tạo một hashmap `map_t` chứa tất cả các phần tử của t lần lượt key = ký tự và value = tần suất.
2. Khởi tạo con trỏ `left = 0`, biến đếm `matched = 0` (số lượng ký tự đã khớp đủ tần suất), và các biến lưu kết quả `min_len`, `min_start`.
3. Duyệt con trỏ `right` từ 0 đến len(s)-1:
   - Thêm ký tự `s[right]` vào cửa sổ (hashmap `window`).
   - Nếu ký tự này thuộc t và đạt đủ tần suất yêu cầu, tăng `matched`.
   - Khi `matched == need` (cửa sổ hợp lệ):
     - Ghi nhận kết quả nếu cửa sổ hiện tại ngắn hơn.
     - Thu hẹp cửa sổ từ bên trái bằng cách tăng `left`, cập nhật `window` và `matched`.
4. Trả về chuỗi con ngắn nhất hoặc chuỗi rỗng nếu không tìm thấy.

**Độ phức tạp:**

- Thời gian: O(m + n) - với m là độ dài của s, n là độ dài của t. Mỗi ký tự trong s được duyệt tối đa 2 lần (bởi right và left).
- Không gian: O(m + n) - để lưu trữ các hashmap `map_t` và `window`.

```python
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        map_t = {}
        for c in t:
            map_t[c] = map_t.get(c, 0) + 1
        need = len(map_t)

        left, matched, min_start = 0, 0, 0
        min_len = float('inf')
        window = {}

        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c, 0) + 1

            if c in map_t and window[c] == map_t[c]:
                matched += 1

            while matched == need:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_start = left

                c_left = s[left]
                if c_left in map_t and window[c_left] == map_t[c_left]:
                    matched -= 1

                window[c_left] -= 1
                left += 1

        return "" if min_len == float('inf') else s[min_start:min_len + min_start]
```
