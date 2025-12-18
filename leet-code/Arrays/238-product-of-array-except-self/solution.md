# 238 [Product of Array Expect Self](https://leetcode.com/problems/product-of-array-except-self/description/)

- Cho một mảng số nguyên nums, hãy trả về một mảng answer sao cho answer[i] bằng tích của tất cả các phần tử của nums ngoại trừ nums[i].
- Tích của bất kỳ tiền tố hoặc hậu tố nào của nums được đảm bảo nằm trong một số nguyên 32 bit.
  > Bạn phải viết một thuật toán chạy trong thời gian O(n) và không sử dụng phép chia.

## 1. Các cách giải với độ phức tạp O(n²)

### 1.1. BruteForce

**Ý tưởng:** Chạy hai vòng lặp và lần lượt nhân tất cả các giá trị ngoại trừ giá trị hiện tại.

**Các hoạt động:**

1. Tạo một mảng kết quả mới, ban đầu tất cả các ô đều có giá trị 1
2. Với mỗi vị trí trong mảng:
   - Xét tất cả các vị trí khác trong mảng gốc
   - Lấy tích của tất cả các số ở những vị trí đó (bỏ qua vị trí hiện tại)
   - Lưu kết quả vào vị trí tương ứng trong mảng kết quả
3. Trả về mảng kết quả đã tính

**Độ phức tạp:**

- Thời gian: O(n²) - hai vòng lặp lồng nhau
- Không gian: O(n) - mảng result để lưu kết quả

```python
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [1] * n
        for i in range(n):
            for j in range(n):
                if i != j:
                    result[i] *= nums[j]
        return result
```

## 2. Các cách giải với độ phức tạp O(n)

### 2.1 Two pass

**Ý tưởng:** Sử dụng hai lần duyệt mảng. Lần đầu tính tích của tất cả các phần tử bên trái (prefix product), lần thứ hai tính tích của các phần tử bên phải (suffix product) và nhân với kết quả đã có.

**Các hoạt động:**

1. Tạo mảng kết quả với tất cả giá trị ban đầu là 1
2. **Lượt đi thứ nhất (từ trái sang phải):**
   - Tại mỗi vị trí, lưu tích của tất cả các số bên trái nó
   - Ví dụ: vị trí thứ 3 sẽ chứa tích của số thứ 1 và thứ 2
3. **Lượt đi thứ hai (từ phải sang trái):**
   - Giữ một biến để nhớ tích của các số bên phải
   - Tại mỗi vị trí, nhân kết quả hiện tại với tích các số bên phải
   - Cập nhật biến nhớ bằng cách nhân thêm số hiện tại
4. Trả về mảng kết quả (đã chứa tích cả hai phía)

**Độ phức tạp:**

- Thời gian: O(n) - hai lần duyệt mảng
- Không gian: O(1) - không tính mảng output, chỉ sử dụng biến right

```python
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [1] * n
        for i in range(1, n):
            res[i] = res[i-1] * nums[i-1]
        right = 1
        for i in range(n - 1, -1, -1):
            res[i] *= right
            right *= nums[i]
        return res
```

### 2.2 Division

**Ý tưởng:** Tính tích của tất cả các phần tử trong mảng, sau đó chia tích này cho từng phần tử để có kết quả. Cần xử lý đặc biệt trường hợp có số 0 trong mảng.

**Các hoạt động:**

1. Tính tích của tất cả các số trong mảng (trừ số 0) và đếm có bao nhiêu số 0
   - Nhân tất cả các số khác 0 với nhau
   - Đếm xem có bao nhiêu số 0
2. Xét từng vị trí để tính kết quả:
   - Nếu có từ 2 số 0 trở lên: mọi vị trí đều cho kết quả 0 (vì tích luôn chứa ít nhất 1 số 0)
   - Nếu có đúng 1 số 0:
     - Vị trí của số 0: cho kết quả là tích tất cả số còn lại
     - Vị trí khác: cho kết quả 0 (vì tích chứa số 0)
   - Nếu không có số 0: lấy tích tổng chia cho số ở vị trí đó
3. Trả về mảng kết quả

**Lưu ý:** Phương pháp này sử dụng phép chia, không tuân thủ yêu cầu của đề bài.

**Độ phức tạp:**

- Thời gian: O(n) - hai lần duyệt mảng
- Không gian: O(1) - chỉ sử dụng các biến phụ, kết quả lưu trực tiếp vào mảng đầu vào

```python
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        total_product = 1
        zero_count = 0
        for num in nums:
            if num != 0:
                total_product *= num
            else:
                 zero_count += 1
        n = len(nums)
        for i in range(n):
            if zero_count > 1:
                nums[i] = 0
            elif zero_count == 1:
                if nums[i] == 0:
                    nums[i] = total_product
                else:
                    nums[i] = 0
            else:
                nums[i] = total_product // nums[i]
        return nums
```
