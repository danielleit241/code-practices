# 875. Koko Eating Bananas

- Koko thích ăn chuối. Có `n` đống chuối, đống thứ `i` có `piles[i]` quả chuối. Các người canh đã đi và sẽ quay lại sau `h` giờ.

- Koko có thể quyết định tốc độ ăn chuối của mình là `k` quả/giờ. Mỗi giờ, cô ấy chọn một đống chuối và ăn `k` quả chuối từ đống đó. Nếu đống đó có ít hơn `k` quả chuối, cô ấy sẽ ăn hết chúng và không ăn thêm quả nào khác trong giờ đó nữa.

- Koko thích ăn chậm nhưng vẫn muốn ăn hết tất cả chuối trước khi người canh quay lại.

  > Trả về số nguyên `k` nhỏ nhất sao cho cô ấy có thể ăn hết tất cả chuối trong vòng `h` giờ.

## 1. Các cách giải với độ phức tạp O(n × maxPile)

### 1.1 Brute Force

**Ý tưởng:** Bắt đầu với `k = 1` và tăng dần tốc độ ăn cho đến khi tìm được tốc độ nhỏ nhất mà Koko có thể ăn hết tất cả chuối trong `h` giờ.

**Cách hoạt động:**

1. Bắt đầu với `k = 1`
2. Với mỗi giá trị `k`, tính tổng số giờ cần để ăn hết tất cả các đống
3. Với mỗi đống, số giờ cần = làm tròn lên(pile / k) = `(pile + k - 1) // k`
4. Nếu tổng số giờ ≤ h, trả về k
5. Ngược lại, tăng k lên 1 và lặp lại

**Độ phức tạp:**

- Thời gian: O(n × maxPile) - trong trường hợp xấu nhất phải kiểm tra từ 1 đến max(piles)
- Không gian: O(1) - chỉ sử dụng một số biến cố định

```python
class Solution:
    def minEatingSpeed_BruteForce(self, piles: list[int], h: int) -> int:
        k = 1
        while True:
            hours = 0
            for p in piles:
                hours += (p + k - 1) // k

            if hours <= h:
                return k
            k += 1
```

## 2. Các cách giải với độ phức tạp O(n × log(maxPile))

### 2.1 Binary Search

**Ý tưởng:**
Nhận thấy rằng nếu Koko có thể ăn hết với tốc độ `k`, thì cô ấy cũng có thể ăn hết với bất kỳ tốc độ nào lớn hơn `k`. Điều này tạo ra một không gian tìm kiếm đơn điệu, rất phù hợp để áp dụng binary search.

**Cách hoạt động:**

1. Đặt biên tìm kiếm: `minK = 1`, `maxK = max(piles)`
2. Trong khi `minK <= maxK`:
   - Tính `mid = minK + (maxK - minK) // 2`
   - Tính tổng số giờ cần thiết với tốc độ `mid`
   - Nếu hours ≤ h: tốc độ này hoạt động, nhưng thử tốc độ nhỏ hơn (tìm bên trái): `maxK = mid - 1`
   - Nếu hours > h: tốc độ quá chậm, cần nhanh hơn (tìm bên phải): `minK = mid + 1`
3. Trả về `minK` (tốc độ hợp lệ nhỏ nhất)

**Độ phức tạp:**

- Thời gian: O(n × log(maxPile)) - binary search log(maxPile) lần, mỗi lần tính hours mất O(n)
- Không gian: O(1) - chỉ sử dụng một số biến cố định

```python
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        minK, maxK = 1, max(piles)

        while minK <= maxK:
            mid = minK + (maxK - minK) // 2

            hours = 0
            for p in piles:
                hours += (p + mid - 1) // mid

            if hours <= h:
                maxK = mid - 1
            else:
                minK = mid + 1

        return minK
```
