# 853. Car Fleet

- Có n chiếc xe ở vị trí cách điểm xuất phát (điểm 0) một khoảng cách nhất định, đang di chuyển để đến điểm đích (điểm 1).
- Bạn được cho hai mảng số nguyên position và speed, cả hai đều có độ dài n, trong đó position[i] là khoảng cách xuất phát của chiếc xe thứ i và speed[i] là tốc độ của chiếc xe thứ i tính bằng dặm trên giờ.
- Một chiếc xe không thể vượt qua chiếc xe khác, nhưng nó có thể đuổi kịp và sau đó di chuyển bên cạnh chiếc xe đó với tốc độ của chiếc xe chậm hơn.
- Một đoàn xe là một chiếc xe đơn lẻ hoặc một nhóm xe chạy cạnh nhau. Tốc độ của đoàn xe là tốc độ tối thiểu của bất kỳ chiếc xe nào trong đoàn xe.
- Nếu một chiếc xe đuổi kịp một đoàn xe tại điểm đích, nó vẫn được coi là một phần của đoàn xe.
- Hãy trả về số lượng đoàn xe sẽ đến đích.

## 1 Các cách giải với độ phức tạp O(nlogn)

### 1.1 Stack

**Ý tưởng:**

Sắp xếp các xe theo vị trí giảm dần (xe gần đích nhất trước). Tính thời gian để mỗi xe đến đích. Sử dụng stack để theo dõi thời gian đến của các đoàn xe. Nếu một xe có thời gian đến nhỏ hơn hoặc bằng xe trước đó, nó sẽ đuổi kịp và tạo thành cùng một đoàn xe (loại bỏ khỏi stack).

**Cách hoạt động:**

1. Kết hợp position và speed thành danh sách các cặp (vị trí, tốc độ)
2. Sắp xếp danh sách theo vị trí giảm dần (xe gần đích nhất đứng đầu)
3. Duyệt qua từng xe:
   - Tính thời gian để xe đó đến đích: (target - position) / speed
   - Thêm thời gian này vào stack
   - Nếu stack có >= 2 phần tử và thời gian của xe hiện tại <= xe trước đó:
     - Xe hiện tại sẽ đuổi kịp xe trước, tạo thành cùng đoàn xe
     - Loại bỏ xe hiện tại khỏi stack (pop)
4. Số lượng phần tử còn lại trong stack chính là số đoàn xe

**Độ phức tạp:**

- Thời gian: O(n log n) - do sắp xếp mảng
- Không gian: O(n) - cho stack và danh sách cars

```python
class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        cars = [(p, s) for p, s in zip(position, speed)]
        cars.sort(reverse=True)
        stack = []
        for p, s in cars:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
```

### 1.2 Iteration

**Ý tưởng:**

Tương tự phương pháp Stack nhưng thay vì sử dụng stack, chỉ cần theo dõi thời gian đến của đoàn xe trước đó. Nếu xe hiện tại mất nhiều thời gian hơn để đến đích, nó tạo thành một đoàn xe mới.

**Cách hoạt động:**

1. Kết hợp position và speed thành danh sách các cặp (vị trí, tốc độ)
2. Sắp xếp danh sách theo vị trí giảm dần
3. Khởi tạo số đoàn xe = 1 và thời gian của đoàn xe đầu tiên
4. Duyệt từ xe thứ 2 đến xe cuối cùng:
   - Tính thời gian để xe hiện tại đến đích
   - Nếu thời gian này > thời gian của đoàn xe trước:
     - Xe này không thể đuổi kịp đoàn xe trước
     - Tăng số đoàn xe lên 1
     - Cập nhật thời gian đoàn xe trước thành thời gian của xe hiện tại
   - Ngược lại: xe này sẽ đuổi kịp và hợp nhất vào đoàn xe trước
5. Trả về tổng số đoàn xe

**Độ phức tạp:**

- Thời gian: O(n log n) - do sắp xếp mảng
- Không gian: O(n) - cho danh sách cars

```python
class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        cars = [(p, s) for p, s in zip(position, speed)]
        cars.sort(reverse=True)
        fleets = 1
        prevTime = (target - cars[0][0]) / cars[0][1]
        for i in range(1, len(cars)):
            currTime = (target - cars[i][0]) / cars[i][1]
            if currTime > prevTime:
                fleets += 1
                prevTime = currTime

        return fleets
```
