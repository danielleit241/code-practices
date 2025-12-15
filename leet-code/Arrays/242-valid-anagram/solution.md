# 242 Valid Anagram

- Cho hai chuỗi s và t, trả về true nếu t là một từ **anagram** của s, và false nếu ngược lại.

  > **Anagram** là một từ hoặc cụm từ được tạo thành bằng cách sắp xếp lại các chữ cái của một từ hoặc cụm từ khác, sử dụng tất cả các chữ cái ban đầu đúng một lần.

## 1. Các cách giải với độ phức tạp O(n²)

### 1.1. BruteForce

**Ý tưởng**: Chuyển s thành list, duyệt t và xóa ký tự tương ứng.

**Cách hoạt động:**

1. Kiểm tra độ dài khác nhau → `False`
2. Chuyển s thành list
3. Với mỗi ký tự trong t: tìm và xóa khỏi list, nếu không thấy → `False`
4. List rỗng → `True`

**Độ phức tạp:**

- Thời gian:
  - Best O(1)
  - Worst O(n²)
- Không gian: O(n)

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_list = list(s)
        for char in t:
            if char in s_list:
                s_list.remove(char)
            else:
                return False
        return len(s_list) == 0
```

### 1.2 Set

**Ý tưởng**: Lấy ký tự duy nhất từ s, sau đó dùng `count()` so sánh tần suất.

**Cách hoạt động:**

1. Kiểm tra độ dài khác nhau → `False`
2. Với mỗi ký tự trong `set(s)`: so sánh `s.count(i)` và `t.count(i)`
3. Nếu tất cả bằng nhau → `True`

**Độ phức tạp:**

- Thời gian:
  - Best O(1)
  - Worst O(n²)
- Không gian: O(n)

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        for i in set(s):
            if s.count(i) != t.count(i):
                return False
            if i not in t:
                return False
        return True
```

## 2. Các cách giải với độ phức tạp O(nlogn)

### 2.1 Sort

**Ý tưởng**: Anagram khi sắp xếp sẽ giống nhau. Ví dụ: "listen" → "eilnst", "silent" → "eilnst"

**Độ phức tạp:**

- Thời gian: O(nlogn) - Timsort ổn định cho mọi trường hợp
- Không gian: O(n)

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
```

## 3. Các cách giải với độ phức tạp O(n)

### 3.1 Hashmap (Dictionary)

**Ý tưởng**: Đếm tần suất ký tự. Anagram có tần suất bằng nhau.

**Cách hoạt động:**

1. Kiểm tra độ dài khác nhau → `False`
2. Duyệt song song s và t: ký tự từ s → +1, ký tự từ t → -1
3. Nếu tất cả giá trị = 0 → `True`

**Độ phức tạp:**

- Thời gian:
  - Best O(1)
  - Worst O(n)
- Không gian: O(n)

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        char_count = {}
        for char_s, char_t in zip(s, t):
            char_count[char_s] = char_count.get(char_s, 0) + 1
            char_count[char_t] = char_count.get(char_t, 0) - 1

        for count in char_count.values():
            if count != 0:
                return False
        return True
```

### 3.2 Arrays

**Ý tưởng**: Giống Hashmap nhưng dùng array 26 phần tử (a-z), tiết kiệm bộ nhớ.

**Cách hoạt động:**

1. Kiểm tra độ dài khác nhau → `False`
2. Khởi tạo array 26 phần tử = 0 (index 0='a', 1='b',...)
3. Duyệt song song: ký tự từ s → +1, ký tự từ t → -1 tại vị trí `ord(char) - ord('a')`
4. Tất cả giá trị = 0 → `True`

**Độ phức tạp:**

- Thời gian:
  - Best O(1)
  - Worst O(n)
- Không gian: O(1)

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26
        for char_s, char_t in zip(s, t):
            count[ord(char_s) - ord('a')] += 1
            count[ord(char_t) - ord('a')] -= 1

        return all(c == 0 for c in count)
```
