# [47 Group Anagrams](https://leetcode.com/problems/group-anagrams/description/)

- Cho một mảng các chuỗi strs, hãy nhóm các từ đảo chữ lại với nhau. Bạn có thể trả về kết quả theo bất kỳ thứ tự nào.

## 1. Các cách giải với độ phức tạp O(n²)

### 1.1 Brute Force - Time Limit Exceeded !!!

**Ý tưởng:** Dùng 2 vòng lặp lồng nhau để so sánh từng cặp phần tử đã **được sắp xếp** trong mảng.

**Cách hoạt động:**

1. Tạo mảng `visited` để đánh dấu các phần tử đã được nhóm
2. Với mỗi phần tử chưa được thăm, tạo một nhóm mới và thêm phần tử đó vào
3. So sánh phần tử hiện tại (đã sắp xếp) với tất cả các phần tử phía sau (đã sắp xếp)
4. Nếu giống nhau và chưa được thăm, thêm vào nhóm hiện tại và đánh dấu đã thăm
5. Thêm nhóm vào kết quả và đánh dấu phần tử hiện tại đã thăm

**Độ phức tạp:**

- Thời gian: O(n² \* k log k) với n là số chuỗi, k là độ dài trung bình của chuỗi
- Không gian: O(n + k)

```python
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = []
        visited = [False] * len(strs)
        for i in range(len(strs)):
            if visited[i]:
                continue
            group = [strs[i]]
            for j in range(i + 1, len(strs)):
                if(sorted(group[0]) == sorted(strs[j]) and not visited[j]):
                    group.append(strs[j])
                    visited[j] = True
            anagrams.append(group)
            visited[i] = True
        return anagrams
```

## 2. Cách cách giải với độ phức tạp O(n)

## 2.1 HashMap

**Ý tưởng:** Sử dụng HashMap để nhóm các từ có cùng tần suất ký tự. Key là tuple đếm tần suất 26 chữ cái, value là danh sách các từ anagram.

**Cách hoạt động:**

1. Tạo một dictionary `anagrams` để lưu các nhóm
2. Với mỗi chuỗi trong mảng:
   - Tạo mảng đếm tần suất 26 chữ cái (a-z)
   - Đếm số lần xuất hiện của mỗi ký tự trong chuỗi
   - Chuyển mảng đếm thành tuple làm key
   - Thêm chuỗi vào danh sách tương ứng với key đó
3. Trả về tất cả các giá trị trong dictionary

**Độ phức tạp:**

- Thời gian: O(n \* k) với n là số chuỗi, k là độ dài trung bình của chuỗi
- Không gian: O(n \* k)

```python
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            anagrams[tuple(count)] = anagrams.get(tuple(count), []) + [s]
        return list(anagrams.values())
```

---

```python
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = {}
        for s in strs:
            key = ''.join(sorted(s))
            if key not in anagrams:
                anagrams[key] = []
            anagrams[key].append(s)
        return list(anagrams.values())
```
