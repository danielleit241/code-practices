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

    def minEatingSpeed_BinarySearch(self, piles: list[int], h: int) -> int:
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
    