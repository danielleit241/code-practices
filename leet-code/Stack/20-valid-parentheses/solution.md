# 20 Valid Parentheses

- Cho một chuỗi s chỉ chứa các ký tự `'(', ')'`, `'{', '}'`, `'[' và ']'`, hãy xác định xem chuỗi đầu vào có hợp lệ hay không.

- Một chuỗi đầu vào hợp lệ nếu:
  1. Dấu ngoặc mở phải được đóng bởi cùng loại ngoặc.
  2. Dấu ngoặc mở phải được đóng theo đúng thứ tự.
  3. Mỗi dấu ngoặc đóng đều có một dấu ngoặc mở tương ứng cùng loại.

## Các cách giải với độ phức tạp O(n²)

### Brute force

**Ý tưởng:** Liên tục tìm và loại bỏ các cặp ngoặc khớp nhau trong chuỗi cho đến khi không còn cặp nào nữa. Nếu chuỗi cuối cùng rỗng thì hợp lệ.

**Các hoạt động:**

1. Lặp lại việc tìm kiếm các cặp ngoặc khớp: '()', '[]', '{}' trong chuỗi
2. Mỗi khi tìm thấy một cặp khớp, xóa cặp đó khỏi chuỗi
3. Tiếp tục cho đến khi không còn cặp nào có thể xóa
4. Kiểm tra xem chuỗi còn lại có rỗng hay không

**Độ phức tạp:**

- Thời gian: O(n²)
- Không gian: O(1)

```python
class Solution:
    def isValid_BruteForce(self, s: str) -> bool:
        while '()' in s or '[]' in s or '{}' in s:
            s = s.replace('()', '')
            s = s.replace('[]', '')
            s = s.replace('{}', '')

        return s == ''
```

## Các cách giải với độ phức tạp O(n)

### Stack

**Ý tưởng:**

- Sử dụng stack để lưu trữ các dấu ngoặc mở và một hashmap để ánh xạ các dấu ngoặc đóng với dấu ngoặc mở tương ứng.
- Khi gặp dấu ngoặc đóng, kiểm tra xem nó có khớp với dấu ngoặc mở ở đỉnh stack hay không.

**Các hoạt động:**

1. Khởi tạo một stack rỗng và hashmap ánh xạ dấu ngoặc đóng sang dấu ngoặc mở tương ứng
2. Duyệt qua từng ký tự trong chuỗi:
   - Nếu gặp dấu ngoặc đóng: kiểm tra stack có rỗng không, sau đó pop phần tử đỉnh stack và so sánh với dấu ngoặc mở tương ứng
   - Nếu gặp dấu ngoặc mở: đẩy vào stack
3. Nếu bất kỳ lúc nào stack rỗng khi gặp dấu đóng hoặc dấu không khớp, trả về False
4. Cuối cùng, kiểm tra stack có rỗng không (đảm bảo tất cả dấu mở đã được đóng)

**Độ phức tạp:**

- Thời gian: O(n) - duyệt qua chuỗi một lần
- Không gian: O(n) - trong trường hợp xấu nhất, stack chứa tất cả các dấu ngoặc mở

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openToClose = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }

        for c in s:
            if c in openToClose:
                if not stack or stack.pop() != openToClose[c]:
                    return False
            else:
                stack.append(c)

        return not stack
```
