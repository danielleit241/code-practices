# [659. Endcode and Decode strings (Premium)](https://leetcode.com/problems/encode-and-decode-strings/description/)

- Hãy thiết kế một thuật toán để mã hóa một danh sách các chuỗi thành một chuỗi duy nhất. Chuỗi đã mã hóa sau đó được giải mã trở lại thành danh sách các chuỗi ban đầu.

## Các cách giải có độ phức tạp O(N)

**Ý tưởng:** Sử dụng định dạng "độ dài#chuỗi" để mã hóa mỗi chuỗi trong danh sách. Ví dụ: chuỗi "abc" sẽ được mã hóa thành "3#abc". Khi giải mã, ta đọc độ dài trước, sau đó lấy chính xác số ký tự đó sau dấu "#". Cách này đảm bảo có thể xử lý được cả chuỗi có chứa ký tự đặc biệt hay khoảng trắng.

**Cách hoạt động:**

**Mã hóa (Encode):**

1. Nếu danh sách rỗng, trả về chuỗi rỗng
2. Khởi tạo chuỗi kết quả rỗng
3. Duyệt qua từng chuỗi trong danh sách:
   - Thêm độ dài của chuỗi vào kết quả
   - Thêm ký tự phân cách "#"
   - Thêm nội dung chuỗi đó
4. Trả về chuỗi đã được mã hóa

**Giải mã (Decode):**

1. Nếu chuỗi đầu vào rỗng, trả về danh sách rỗng
2. Khởi tạo danh sách kết quả và con trỏ i = 0
3. Trong khi i chưa đến cuối chuỗi:
   - Tìm vị trí j của ký tự "#" tiếp theo (bắt đầu từ i)
   - Lấy độ dài từ đoạn s[i:j] và chuyển sang số nguyên
   - Lấy chuỗi con có độ dài đó ngay sau dấu "#" và thêm vào kết quả
   - Di chuyển con trỏ i đến vị trí sau chuỗi vừa lấy
4. Trả về danh sách các chuỗi đã giải mã

**Độ phức tạp:**

- **Thời gian:** O(n) - với n là tổng số ký tự của tất cả các chuỗi, mỗi ký tự chỉ được xử lý một lần
- **Không gian:** O(n) - để lưu trữ chuỗi kết quả khi mã hóa hoặc danh sách kết quả khi giải mã

<details open>
<summary><b>🐍 Python Version</b> (Click để đóng)</summary>

```python
class Solution:
    def encode(self, strs: list[str]) -> str:
        if not strs:
            return ""
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s;
        return res

    def decode(self, s: str) -> list[str]:
        if not s:
            return []
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j+1:j+1+length])
            i = j + 1 + length
        return res
```

</details>

<details open>
<summary><b>💠 CSharp Version</b> (Click để đóng)</summary>

```csharp
public class Solution {

    public string Encode(IList<string> strs)
    {
        StringBuilder builder = new StringBuilder();
        foreach(var s in strs)
        {
            builder.Append(s.Length).Append("#").Append(s);
        }
        return builder.ToString();
    }

    public List<string> Decode(string s)
    {
        List<string> res = new List<string>();
        var i = 0;
        while(i < s.Length)
        {
            var j = i;
            while(s[j] != '#')
            {
                j++;
            }
            var length = int.Parse(s.Substring(i, j - i));
            res.Add(s.Substring(j + 1, length));
            i = j + 1 + length;
        }
        return res;
   }
}
```

</details>
