# [128. Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/description/)

Cho một mảng các số nguyên chưa được sắp xếp nums, hãy trả về độ dài của chuỗi các phần tử liên tiếp dài nhất.

Bạn phải viết một thuật toán chạy trong thời gian O(n).

## 1. Các cách giải với độ phức tạp O(nlogn)

### Sort

**Ý tưởng:** Sắp xếp mảng đã cho sẵn, sau đó đếm các phần tử liền kề liên tiếp nhau.

**Cách hoạt động:**

1. Kiểm tra mảng đã cho có rỗng hay không -> nếu rỗng thì trả về 0
2. Nếu mảng không rỗng ta bắt đầu sắp xếp mảng theo chiều hướng tăng dần và loại bỏ các số trùng lặp
3. Khởi tạo 2 biến: `longest_streak` (chuỗi dài nhất) và `current_streak` (chuỗi hiện tại) đều bằng 1
4. Duyệt qua mảng đã sắp xếp từ vị trí thứ 2:
   - Nếu số hiện tại bằng số trước đó cộng 1, tăng `current_streak` lên 1 nếu không thì đặt lại `current_streak` về 1
   - Sau đó, cập nhật `longest_streak` nếu `current_streak` lớn hơn
5. Cuối cùng, so sánh và trả về giá trị lớn nhất giữa `longest_streak` và `current_streak`

**Độ phức tạp:**

- **Thời gian:** O(n log n) - do phải sắp xếp mảng
- **Không gian:** O(n) - do tạo set để loại bỏ phần tử trùng lặp

<details open>
<summary><b>🐍 Python Version</b> (Click để đóng)</summary>

```python
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0

        nums = sorted(set(nums))
        longest_streak = 1
        current_streak = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                current_streak += 1
            else:
                current_streak = 1
            longest_streak = max(longest_streak, current_streak)
        return longest_streak
```

</details>

<details open>
<summary><b>💠 CSharp Version</b> (Click để đóng)</summary>

```csharp
public class Solution{
    public int LongestConsecutive_Sort(int[] nums){
        nums = nums.Distinct().ToArray();
        Array.Sort(nums);

        int longest, current = 1;

        for(int i = 0; i < nums.Length - 1; i++){
            if(nums[i] + 1 == nums[i + 1]){
                current++;
            } else {
                current = 1;
            }
            longest = Math.Max(longest, current);
        }
        return longest;
    }
}
```

</details>

## 2. Các cách giải với độ phức tạp O(n)

**Ý tưởng:** Sử dụng HashSet để lưu trữ tất cả các số trong mảng, sau đó bắt đầu đếm chuỗi liên tiếp khi gặp số đầu tiên của chuỗi đó (số mà không có số trước nó trong set).

**Cách hoạt động:**

1. Kiểm tra nếu mảng rỗng thì trả về 0
2. Tạo một HashSet chứa tất cả các số trong mảng để tra cứu nhanh
3. Khởi tạo biến `longest` để lưu độ dài chuỗi liên tiếp dài nhất
4. Duyệt qua từng số trong HashSet:
   - Kiểm tra xem số đó có phải là số đầu tiên của một chuỗi không (bằng cách kiểm tra xem số trước nó có tồn tại trong set hay không)
   - Nếu đúng là số đầu tiên:
     - Khởi tạo biến `current` bằng 1 (độ dài chuỗi hiện tại)
     - Liên tục kiểm tra và đếm các số tiếp theo (num+1, num+2, ...) có trong set không
     - Mỗi khi tìm thấy số tiếp theo, tăng `current` lên 1
     - Cập nhật `longest` nếu `current` lớn hơn
5. Trả về `longest`

**Độ phức tạp:**

- **Thời gian:** O(n) - mỗi số chỉ được duyệt qua tối đa 2 lần (1 lần trong vòng lặp chính, 1 lần khi đếm chuỗi)
- **Không gian:** O(n) - sử dụng HashSet để lưu trữ n phần tử

<details open>
<summary><b>🐍 Python Version</b> (Click để đóng)</summary>

```python
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0
        nums_set = set(nums)
        longest = 0
        for num in nums_set:
            if num - 1 not in nums_set:
                current = 1
                next_num = num + 1
                while next_num in nums_set:
                    current += 1
                    next_num += 1
                longest = max(longest, current)
        return longest
```

</details>

<details open>
<summary><b>💠 CSharp Version</b> (Click để đóng)</summary>

```csharp
public class Solution{
    public int LongestConsecutive(int[] nums) {
        if (nums.Length == 0) return 0;
        HashSet<int> set = new(nums);
        var res = 0;
        foreach(var num in set)
        {
            if(!set.Contains(num - 1))
            {
                var longChars = 1;
                var next = num + 1;
                while(set.Contains(next))
                {
                    longChars += 1;
                    next += 1;
                }
                res = Math.Max(res, longChars);
            }
        }
        return res;
    }
}
```

</details>
