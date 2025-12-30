# 22. Generate Parentheses

- Cho n cặp dấu ngoặc đơn, hãy viết một hàm để tạo ra tất cả các tổ hợp dấu ngoặc đơn hợp lệ.

  - Example 1:
    - Input: n = 3
    - Output: `["((()))","(()())","(())()","()(())","()()()"]`

## 1. Các cách giải với độ phức tạp O(4^n / √n)

### 1.1 Backtracking

**Ý tưởng:**

- Ta chỉ thêm dấu ngoặc mở `(` khi số lượng dấu mở chưa đạt `n`, và chỉ thêm dấu ngoặc đóng `)` khi số lượng dấu đóng nhỏ hơn số lượng dấu mở (đảm bảo tính hợp lệ).

**Cách hoạt động:**

1. Sử dụng một stack để xây dựng chuỗi dấu ngoặc hiện tại
2. Sử dụng đệ quy với hai tham số: `openN` (số dấu mở đã dùng) và `closedN` (số dấu đóng đã dùng)
3. Điều kiện dừng: Khi `openN == closedN == n`, ta có một chuỗi hợp lệ hoàn chỉnh
4. Quy tắc thêm dấu ngoặc:
   - Thêm `(` nếu `openN < n` (còn có thể thêm dấu mở)
   - Thêm `)` nếu `closedN < openN` (đảm bảo không có dấu đóng thừa)
5. Sau mỗi lần thêm dấu ngoặc, gọi đệ quy và sau đó backtrack (pop khỏi stack)

**Độ phức tạp:**

- Thời gian: O(4^n / √n) - Số Catalan thứ n, tổng số chuỗi hợp lệ cần sinh
- Không gian: O(n) - Độ sâu của cây đệ quy

```python
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        stack = []
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()

            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0, 0)
        return res
```
