# 121. Best Time to Buy and Sell Stock

- Cho một mảng prices trong đó prices[i] là giá của một cổ phiếu nhất định vào ngày thứ i.
- Bạn muốn tối đa hóa lợi nhuận của mình bằng cách chọn một ngày để mua một cổ phiếu và chọn một ngày khác trong tương lai để bán cổ phiếu đó.
- Trả về lợi nhuận tối đa bạn có thể đạt được từ giao dịch này. Nếu bạn không thể đạt được bất kỳ lợi nhuận nào, hãy trả về 0.

## 1. Các cách giải với độ phức tạp O(n²)

### 1.1. BruteForce

**Ý tưởng:** Dùng 2 vòng lặp lồng nhau để kiểm tra tất cả các cặp ngày mua và bán có thể.

**Cách hoạt động:**

1. Duyệt qua từng ngày `i` để làm ngày mua
2. Với mỗi ngày mua `i`, duyệt qua tất cả các ngày sau đó `j` (j > i) để làm ngày bán
3. Tính lợi nhuận = `prices[j] - prices[i]`
4. Cập nhật lợi nhuận tối đa nếu tìm thấy lợi nhuận lớn hơn

**Độ phức tạp:**

- Thời gian:
  - Best O(1) - Tìm thấy ngay ở cặp đầu tiên
  - Worst O(n²) - Phải kiểm tra tất cả các cặp
- Không gian: O(1) - không dùng thêm bộ nhớ phụ

```python
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                profit = prices[j] - prices[i]
                max_profit = max(max_profit, profit)
        return max_profit
```

## 2. Các cách giải với độ phức tạp O(n)

### 2.1. One Pass (Sliding Window)

**Ý tưởng:** Duy trì giá thấp nhất đã gặp cho đến hiện tại và tính lợi nhuận với giá hiện tại.

**Cách hoạt động:**

1. Khởi tạo `min_price` = giá trị lớn nhất có thể (hoặc giá ngày đầu tiên)
2. Khởi tạo `max_profit` = 0
3. Duyệt qua từng giá trong mảng:
   - Cập nhật `min_price` nếu gặp giá thấp hơn
   - Tính lợi nhuận hiện tại = `price - min_price`
   - Cập nhật `max_profit` nếu lợi nhuận hiện tại lớn hơn
4. Trả về `max_profit`

**Độ phức tạp:**

- Thời gian: O(n) - chỉ duyệt qua mảng một lần
- Không gian: O(1) - chỉ dùng 2 biến

```python
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)

        return max_profit
```

### 2.2. Two Pointers (Sliding Window)

**Ý tưởng:** Sử dụng hai con trỏ `left` (ngày mua) và `right` (ngày bán), di chuyển chúng để tìm lợi nhuận tối đa.

**Cách hoạt động:**

1. Khởi tạo `left = 0` (ngày mua) và `right = 1` (ngày bán)
2. Khởi tạo `max_profit = 0`
3. Duyệt qua mảng với con trỏ `right`:
   - Nếu `prices[right] > prices[left]`: tính lợi nhuận và cập nhật `max_profit`
   - Nếu `prices[right] <= prices[left]`: di chuyển `left` đến `right` (vì tìm thấy giá thấp hơn để mua)
   - Di chuyển `right` sang phải
4. Trả về `max_profit`

**Độ phức tạp:**

- Thời gian: O(n) - duyệt qua mảng một lần
- Không gian: O(1) - chỉ dùng 2 con trỏ và 1 biến

```python
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        left = 0  # Buy
        right = 1  # Sell
        max_profit = 0

        while right < len(prices):
            if prices[right] > prices[left]:
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)
            else:
                left = right
            right += 1

        return max_profit
```
