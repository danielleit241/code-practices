# 150. Evaluate Reverse Polish Notation

- Bạn được cung cấp một mảng các chuỗi (token) biểu diễn một biểu thức số học dưới dạng ký hiệu **Ba Lan ngược (Reverse Polish Notation)**.
  > Đánh giá biểu thức đó. Trả về một số nguyên biểu thị giá trị của biểu thức.
- Lưu ý rằng:
  - Các toán tử hợp lệ là `'+'`, `'-'`, `'*'` và `'/'`.
  - Mỗi toán hạng có thể là một số nguyên hoặc một biểu thức khác.
  - Phép chia giữa hai số nguyên luôn làm tròn về 0.
  - Sẽ không có phép chia cho 0.
  - Đầu vào biểu diễn một biểu thức số học hợp lệ dưới dạng ký hiệu Ba Lan ngược.
  - Kết quả và tất cả các phép tính trung gian có thể được biểu diễn dưới dạng số nguyên 32 bit.

## 1. Các cách giải với độ phức tạp O(n²)

### 1.1 Brute Force

**Ý tưởng:**
Duyệt qua mảng tokens nhiều lần, mỗi lần tìm toán tử đầu tiên, thực hiện phép tính với hai toán hạng trước đó, thay thế ba phần tử (hai toán hạng + toán tử) bằng kết quả, và lặp lại quá trình cho đến khi chỉ còn một phần tử.

**Cách hoạt động:**

1. Tiếp tục vòng lặp while khi mảng còn nhiều hơn 1 phần tử
2. Duyệt qua mảng để tìm toán tử đầu tiên
3. Khi tìm thấy toán tử, lấy hai phần tử trước đó làm toán hạng
4. Thực hiện phép tính tương ứng
5. Tạo mảng mới bằng cách ghép: phần trước toán hạng thứ nhất + kết quả + phần sau toán tử
6. Lặp lại cho đến khi chỉ còn 1 phần tử

**Độ phức tạp:**

- Thời gian: O(n²) - trong trường hợp xấu nhất phải duyệt mảng nhiều lần và mỗi lần phải tái tạo mảng
- Không gian: O(n) - cho việc tạo mảng mới mỗi lần

```python
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        while len(tokens) > 1:
            for i in range(len(tokens)):
                if tokens[i] in "+-*/":
                    operator = tokens[i]
                    left = int(tokens[i - 2])
                    right = int(tokens[i - 1])
                    if operator == '+':
                        result = left + right
                    elif operator == '-':
                        result = left - right
                    elif operator == '*':
                        result = left * right
                    else:
                        result = int(left / right)

                    tokens = tokens[:i - 2] + [str(result)] + tokens[i + 1:]
                    break
        return int(tokens[0])
```

## 2. Các cách giải với độ phức tạp O(n)

### 2.1 Recursion (Đệ quy)

**Ý tưởng:**
Xử lý các token từ cuối mảng (sử dụng pop). Nếu gặp số thì trả về giá trị, nếu gặp toán tử thì đệ quy để lấy hai toán hạng (bên phải trước, bên trái sau do tính chất của stack), sau đó thực hiện phép tính.

**Cách hoạt động:**

1. Hàm đệ quy `dfs()` lấy token từ cuối mảng bằng `pop()`
2. Nếu token là số, chuyển sang int và trả về
3. Nếu token là toán tử:
   - Gọi đệ quy để lấy toán hạng bên phải
   - Gọi đệ quy để lấy toán hạng bên trái
   - Thực hiện phép tính tương ứng và trả về kết quả
4. Do xử lý từ cuối, thứ tự đệ quy sẽ đúng với cấu trúc RPN

**Độ phức tạp:**

- Thời gian: O(n) - mỗi token được xử lý đúng một lần
- Không gian: O(n) - stack đệ quy có thể sâu tới n trong trường hợp xấu nhất

```python
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        def dfs():
            token = tokens.pop()
            if token not in "+-*/":
                return int(token)

            right = dfs()
            left = dfs()

            if token == '+':
                return left + right
            elif token == '-':
                return left - right
            elif token == '*':
                return left * right
            else:
                return int(left / right)

        return dfs()
```

### 2.2 Stack

**Ý tưởng:**
Sử dụng stack để lưu trữ các số. Khi gặp toán tử, lấy ra (pop) hai số từ stack, thực hiện phép tính, và đẩy kết quả trở lại stack. Đây là cách tiếp cận tối ưu và tự nhiên nhất cho bài toán RPN.

**Cách hoạt động:**

1. Khởi tạo một stack rỗng và danh sách các toán tử
2. Duyệt qua từng token trong mảng:
   - Nếu token là số: chuyển sang int và đẩy vào stack
   - Nếu token là toán tử:
     - Pop số thứ hai (num2) - đây là toán hạng bên phải
     - Pop số thứ nhất (num1) - đây là toán hạng bên trái
     - Thực hiện phép tính: num1 operator num2
     - Đẩy kết quả vào stack
3. Cuối cùng, stack chỉ còn một phần tử là kết quả cuối cùng

**Độ phức tạp:**

- Thời gian: O(n) - duyệt qua mảng một lần, mỗi thao tác push/pop là O(1)
- Không gian: O(n) - stack có thể chứa tối đa n phần tử

```python
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        numStack = []
        operators = ['+', '-', '*', '/']
        for token in tokens:
            if token not in operators:
                numStack.append(int(token))
            else:
                num2 = numStack.pop()
                num1 = numStack.pop()
                if token == '+':
                    numStack.append(num1 + num2)
                elif token == '-':
                    numStack.append(num1 - num2)
                elif token == '*':
                    numStack.append(num1 * num2)
                else:
                    numStack.append(int(num1 / num2))

        return numStack[-1]
```
