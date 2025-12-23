# 242 Valid Anagram

- Cho hai chuỗi s và t, trả về true nếu t là một từ **anagram** của s, và false nếu ngược lại.

  > **Anagram** là một từ hoặc cụm từ được tạo thành bằng cách sắp xếp lại các chữ cái của một từ hoặc cụm từ khác, sử dụng tất cả các chữ cái ban đầu đúng một lần.

## 1. Các cách giải với độ phức tạp O(n²)

### 1.1. BruteForce

**Ý tưởng:** Chuyển s thành list, duyệt t và xóa ký tự tương ứng.

**Cách hoạt động:**

1. **Kiểm tra độ dài**: Nếu độ dài hai chuỗi khác nhau → trả về False ngay lập tức

2. **Chuyển đổi**: Tạo một danh sách mới từ chuỗi s để có thể xóa phần tử

3. **Duyệt và khớp**: Với mỗi ký tự trong chuỗi t:

   - Tìm kiếm ký tự đó trong danh sách
   - Nếu tìm thấy thì xóa ký tự khỏi danh sách
   - Nếu không tìm thấy thì không phải anagram → trả về False

4. **Kiểm tra cuối**: Nếu danh sách rỗng thì tất cả ký tự đã khớp → trả về True

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

1. **Kiểm tra độ dài**: Nếu độ dài hai chuỗi khác nhau → trả về False

2. **Tạo tập ký tự duy nhất**: Chuyển chuỗi s thành tập hợp để lấy các ký tự không trùng lặp

3. **Duyệt và so sánh**: Với mỗi ký tự duy nhất trong tập hợp:

   - Đếm số lần xuất hiện của ký tự đó trong chuỗi s
   - Đếm số lần xuất hiện của ký tự đó trong chuỗi t
   - Nếu số lần xuất hiện khác nhau → trả về False
   - Nếu ký tự không có trong t → trả về False

4. **Kết quả**: Nếu tất cả ký tự đều khớp về số lần xuất hiện → trả về True

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

**Cách hoạt động:**

1. **Sắp xếp chuỗi s**: Chuyển chuỗi thành danh sách và sắp xếp theo thứ tự alphabet

2. **Sắp xếp chuỗi t**: Làm tương tự với chuỗi t

3. **So sánh trực tiếp**: So sánh hai danh sách đã sắp xếp
   - Nếu giống hệt nhau thì là anagram → trả về True
   - Nếu khác nhau ở bất kỳ vị trí nào → trả về False

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

1. **Kiểm tra độ dài**: Nếu độ dài hai chuỗi khác nhau → trả về False

2. **Khởi tạo bảng đếm**: Tạo một bảng băm rỗng để lưu số lần xuất hiện

3. **Duyệt đồng thời**: Duyệt song song hai chuỗi s và t cùng lúc

   - Với mỗi ký tự từ s: Tăng số đếm lên 1 trong bảng
   - Với mỗi ký tự từ t: Giảm số đếm xuống 1 trong bảng
   - Nếu là anagram thì phép cộng và trừ sẽ triệt tiêu lẫn nhau thành 0

4. **Kiểm tra cân bằng**: Duyệt qua tất cả giá trị trong bảng băm
   - Nếu tất cả giá trị đều bằng 0 → là anagram → trả về True
   - Nếu bất kỳ giá trị nào khác 0 → không phải anagram → trả về False

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

1. **Kiểm tra độ dài**: Nếu độ dài hai chuỗi khác nhau → trả về False

2. **Khởi tạo mảng đếm**: Tạo mảng có 26 phần tử tương ứng 26 chữ cái, giá trị ban đầu đều là 0

3. **Duyệt đồng thời**: Duyệt song song hai chuỗi s và t cùng lúc

   - Với mỗi ký tự từ s: Tính vị trí tương ứng trong mảng và tăng giá trị lên 1
   - Với mỗi ký tự từ t: Tính vị trí tương ứng trong mảng và giảm giá trị xuống 1
   - Nếu là anagram thì phép cộng và trừ sẽ triệt tiêu lẫn nhau

4. **Kiểm tra cân bằng**: Kiểm tra tất cả 26 phần tử trong mảng
   - Nếu tất cả giá trị đều bằng 0 → là anagram → trả về True
   - Nếu có bất kỳ giá trị nào khác 0 → không phải anagram → trả về False

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
