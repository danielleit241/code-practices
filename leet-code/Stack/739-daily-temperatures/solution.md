# 739. Daily Temperatures

- Cho một mảng các số nguyên temperatures biểu thị nhiệt độ hàng ngày, hãy trả về một mảng answer sao cho answer[i] là số ngày bạn phải đợi sau ngày thứ i để có nhiệt độ ấm hơn. Nếu không có ngày nào trong tương lai mà điều này có thể xảy ra, hãy giữ answer[i] == 0.

## 1. Các cách giải với độ phức tạp O(n²)

### 1.1 Brute Force

**Ý tưởng:**
Dùng hai vòng lặp lồng nhau để kiểm tra từng ngày với tất cả các ngày tiếp theo sau nó, tìm ngày đầu tiên có nhiệt độ cao hơn.

**Cách hoạt động:**

- Với mỗi ngày i, duyệt qua tất cả các ngày j từ i+1 đến n-1
- Khi tìm thấy ngày j có nhiệt độ lớn hơn ngày i, lưu khoảng cách (j - i) vào kết quả và dừng vòng lặp
- Nếu không tìm thấy ngày nào ấm hơn, giá trị mặc định là 0

**Độ phức tạp:**

- Thời gian: O(n²) - trong trường hợp xấu nhất phải kiểm tra tất cả các cặp
- Không gian: O(n) - chỉ cần mảng kết quả

```python
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        res = [0] * n
        for i in range(n):
            for j in range(i + 1, n):
                if temperatures[j] > temperatures[i]:
                    res[i] = j - i
                    break
        return res
```

## 2. Các cách giải với độ phức tạp O(n)

### 2.1 Monotonic Stack

**Ý tưởng:**
Sử dụng một stack giảm dần (monotonic decreasing stack) để lưu trữ các chỉ số của những ngày chưa tìm được ngày ấm hơn. Khi gặp một nhiệt độ cao hơn, ta có thể xác định kết quả cho các ngày trong stack.

**Cách hoạt động:**

- Duyệt qua từng ngày với chỉ số i
- Với mỗi nhiệt độ hiện tại, kiểm tra stack:
  - Nếu nhiệt độ hiện tại lớn hơn nhiệt độ tại đỉnh stack, nghĩa là tìm được ngày ấm hơn
  - Pop chỉ số ra khỏi stack và tính khoảng cách (i - chỉ số đó)
  - Lặp lại cho đến khi stack rỗng hoặc gặp nhiệt độ lớn hơn hoặc bằng
- Thêm chỉ số hiện tại vào stack
- Stack luôn duy trì thứ tự giảm dần theo nhiệt độ

**Độ phức tạp:**

- Thời gian: O(n) - mỗi phần tử được push và pop khỏi stack đúng một lần
- Không gian: O(n) - trong trường hợp xấu nhất stack chứa tất cả các chỉ số

```python
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        stack = []
        res = [0] * n
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                colder = stack.pop()
                res[colder] = i - colder
            stack.append(i)
        return res
```
