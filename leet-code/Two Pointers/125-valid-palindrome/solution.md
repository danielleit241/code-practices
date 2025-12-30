# [125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)

- Cho một chuỗi `s`, hãy xác định xem nó có phải là một palindrome hay không, chỉ xét các ký tự chữ và số và bỏ qua chữ hoa chữ thường.

## 1. Các cách giải với độ phức tạp O(n)

### 1.1. Deque (Double-ended Queue)

**Ý tưởng:** Sử dụng deque để lưu các ký tự hợp lệ (chữ và số), sau đó so sánh ký tự từ hai đầu của deque.

**Cách hoạt động:**

1. Tạo hàng đợi rỗng, duyệt chuỗi và chỉ thêm các ký tự chữ/số (chuyển về chữ thường)
2. Lấy ký tự từ hai đầu hàng đợi ra so sánh:
   - Khác nhau → `False`
   - Giống nhau → tiếp tục với cặp tiếp theo
3. Hết ký tự hoặc còn 1 ký tự → `True`

**Độ phức tạp:**

- **Thời gian:** O(n) - duyệt qua chuỗi một lần
- **Không gian:** O(n) - lưu trữ các ký tự hợp lệ trong deque

<details open>
<summary><b>🐍 Python Version</b> (Click để đóng)</summary>

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        from collections import deque
        dp = deque()
        for i in range(len(s)):
            if s[i].isalnum():
               dp.append(s[i].lower())

        while len(dp) > 1:
            if dp.popleft() != dp.pop():
                return False
        return True
```

</details>

---

### 1.2. Reverse String

**Ý tưởng:** Loại bỏ các ký tự không hợp lệ và chuyển về chữ thường, sau đó so sánh chuỗi với chuỗi đảo ngược của nó.

**Cách hoạt động:**

1. Làm sạch chuỗi: loại bỏ ký tự đặc biệt, chuyển về chữ thường
2. Đảo ngược chuỗi và so sánh với chuỗi gốc
3. Giống nhau → palindrome, khác nhau → không phải

**Độ phức tạp:**

- **Thời gian:** O(n) - xử lý chuỗi và đảo ngược
- **Không gian:** O(n) - tạo chuỗi mới sau khi xử lý và chuỗi đảo ngược

<details open>
<summary><b>🐍 Python Version</b> (Click để đóng)</summary>

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        s = re.sub(r'[^a-z0-9]', '', s.lower())
        return s == s[::-1]
```

</details>

---

### 1.3. Two Pointers

**Ý tưởng:** Xử lý chuỗi trước, sau đó dùng hai con trỏ để so sánh từ hai đầu chuỗi.

**Cách hoạt động:**

1. Làm sạch chuỗi: loại bỏ ký tự đặc biệt, chuyển về chữ thường
2. Đặt con trỏ trái ở đầu, con trỏ phải ở cuối
3. So sánh ký tự tại hai con trỏ:
   - Khác nhau → `False`
   - Giống nhau → di chuyển cả hai con trỏ vào trong
4. Hai con trỏ gặp nhau → `True`

**Độ phức tạp:**

- **Thời gian:** O(n) - xử lý chuỗi và duyệt một lần
- **Không gian:** O(n) - tạo chuỗi mới sau khi xử lý

<details open>
<summary><b>🐍 Python Version</b> (Click để đóng)</summary>

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        s = re.sub(r'[^a-z0-9]', '', s.lower())
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
```

</details>

---

### 1.4. Optimized Two Pointers

**Ý tưởng:** Dùng hai con trỏ trực tiếp trên chuỗi gốc, bỏ qua các ký tự không hợp lệ trong quá trình so sánh.

**Cách hoạt động:**

1. Chuyển chuỗi về chữ thường, giữ nguyên ký tự đặc biệt
2. Đặt con trỏ trái ở đầu, con trỏ phải ở cuối
3. Di chuyển thông minh:
   - Gặp ký tự đặc biệt → bỏ qua (không so sánh)
   - Cả hai con trỏ đều ở ký tự hợp lệ → so sánh:
     - Khác nhau → `False`
     - Giống nhau → di chuyển cả hai vào trong
4. Hai con trỏ gặp nhau → `True`

**Ưu điểm:** Không cần tạo chuỗi mới, tiết kiệm bộ nhớ

**Độ phức tạp:**

- **Thời gian:** O(n) - duyệt qua chuỗi một lần
- **Không gian:** O(1) - không cần lưu trữ thêm (ngoại trừ chuỗi lowercase)

<details open>
<summary><b>🐍 Python Version</b> (Click để đóng)</summary>

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        left, right = 0, len(s) - 1
        while left < right:
            if not s[left].isalnum():
                left += 1
                continue

            if not s[right].isalnum():
                right -= 1
                continue

            if s[left] != s[right]:
                return False
            else:
                left += 1
                right -= 1
        return True
```

</details>

</details>

<details open>
<summary><b>💠 CSharp Version</b> (Click để đóng)</summary>

```csharp
public class Solution
{
    public bool IsPalindrome(string s)
    {
        int left = 0;
        int right = s.Length - 1;

        while(left < right)
        {
            while(left < right && !char.IsLetterOrDigit(s[left]))
            {
                left++;
            }
            while(left < right && !char.IsLetterOrDigit(s[right]))
            {
                right--;
            }
            if(char.ToLower(s[left]) != char.ToLower(s[right]))
            {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
}
```

</details>
