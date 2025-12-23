# 347. [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/description/)

- Cho một mảng số nguyên nums và một số nguyên k, hãy trả về k phần tử xuất hiện nhiều nhất. Bạn có thể trả về câu trả lời theo bất kỳ thứ tự nào.

## 1. Các cách giải với độ phức tạp O(nlogn)

### 1.1 Sort + Map

**Ý tưởng:** Dùng Hashmap lưu trữ key: giá trị trong mảng - value: số lần xuất hiện. Sau đó sắp xếp số lần xuất hiện sau đó lấy top K.

**Cách hoạt động:**

1. Tạo một Hashmap với key là giá trị trong mảng và value là tần xuất xuất hiện của giá trị đó.
2. Sắp xếp Hashmap dựa trên tần xuất xuất hiện
3. Lấy ra top K sau khi đã sắp xếp

**Độ phức tạp:**

- Thời gian: O(n log n) - trong đó n là số phần tử trong mảng
- Không gian: O(n)

```python
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        map = {}
        for num in nums:
            map[num] = map.get(num, 0) + 1
        sorted_map = sorted(map.items(), key=lambda x: x[1], reverse=True)
        return [item[0] for item in sorted_map[:k]]
```

### 1.2 Counter

**Ý tưởng:** Dùng counter trong collections để đếm

**Cách hoạt động:**

1. Dùng counter để đếm giá trị : tần xuất
2. Sắp xếp các giá trị của counter sau khi đếm và chuyển sang dict
3. Lấy ra top K sau khi đã sắp xếp

**Độ phức tạp:**

- Thời gian: O(n log n) - trong đó n là số phần tử trong mảng
- Không gian: O(n)

```python
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = Counter(nums)
        map = dict(sorted(count.items(), key=lambda x: x[1], reverse=True))
        return list(map.keys())[:k]
```

## 2. Các cách giải có độ phức tạp O(n)

### 2.1 Hashmap + Max

**Ý tưởng:** Dùng Hashmap lưu trữ key: giá trị trong mảng - value: số lần xuất hiện. Sau đó dùng biến Max để xác định số lần xuất hiện lớn nhất

**Cách hoạt động:**

1. Tạo một Hashmap với key là giá trị trong mảng và value là tần xuất xuất hiện của giá trị đó.
2. Dùng hàm max để tìm key có giá trị lớn nhất (tần xuất lớn nhất) trong K lần
3. Lưu vào kết quả và xóa luôn giá trị lớn nhất vừa tìm thấy
4. Trả về kết quả cuối cùng

**Độ phức tạp:**

- Thời gian: O(n × k) - trong đó n là số phần tử trong mảng, k là số phần tử cần lấy
- Không gian: O(n)

```python
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        map = {}
        for num in nums:
            map[num] = map.get(num, 0) + 1
        result = []
        for _ in range(k):
            max_key = max(map, key=map.get) # Dùng hàm max để tìm key có value lớn nhất
            result.append(max_key)
            del map[max_key]
        return result
```

### 2.2 Bucket sort

**Ý tưởng:** Thay vì sắp xếp các phần tử theo tần xuất xuất hiện, ta tạo ra các "thùng" (bucket) tương ứng với mỗi tần xuất có thể có. Mỗi thùng sẽ chứa các số có cùng tần xuất xuất hiện. Sau đó duyệt ngược từ thùng có tần xuất cao nhất để lấy ra k phần tử.

**Cách hoạt động:**

1. Đầu tiên, tạo một hashmap để đếm tần xuất xuất hiện của mỗi số trong mảng.
2. Tạo một mảng bucket có độ dài bằng (độ dài mảng + 1). Mỗi vị trí i trong bucket sẽ chứa danh sách các số xuất hiện đúng i lần. Ví dụ: bucket[3] chứa các số xuất hiện 3 lần.
3. Duyệt qua hashmap và đặt mỗi số vào bucket tương ứng với tần xuất của nó.
4. Duyệt ngược mảng bucket từ cuối về đầu (từ tần xuất cao xuống thấp), lấy các số ra cho đến khi đủ k phần tử.

**Độ phức tạp:**

- Thời gian: O(n) - trong đó n là số phần tử trong mảng
- Không gian: O(n)

```python
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        map_count = {}
        freq = [[] for _ in range(len(nums) + 1)]
        for num in nums:
            map_count[num] = 1 + map_count.get(num, 0)

        for num, count in map_count.items():
            freq[count].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
```

**Ví dụ minh họa:**

Giả sử có mảng: [1, 1, 1, 2, 2, 3] và k = 2

Bước 1: Đếm tần xuất

- 1 xuất hiện 3 lần
- 2 xuất hiện 2 lần
- 3 xuất hiện 1 lần

Bước 2: Tạo bucket array có độ dài 7 (6 + 1)

- bucket[0] = [] (không có số nào xuất hiện 0 lần)
- bucket[1] = [3] (số 3 xuất hiện 1 lần)
- bucket[2] = [2] (số 2 xuất hiện 2 lần)
- bucket[3] = [1] (số 1 xuất hiện 3 lần)
- bucket[4] = []
- bucket[5] = []
- bucket[6] = []

Bước 3: Duyệt ngược từ bucket[6] về bucket[1]

- bucket[6] rỗng, bỏ qua
- bucket[5] rỗng, bỏ qua
- bucket[4] rỗng, bỏ qua
- bucket[3] có [1], lấy ra → kết quả = [1]
- bucket[2] có [2], lấy ra → kết quả = [1, 2]
- Đã đủ k = 2 phần tử, dừng lại

Kết quả cuối cùng: [1, 2]
