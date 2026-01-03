class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def linearSearch(self, nums: list[int], target: int) -> int:
        for i, n in enumerate(nums):
            if n == target:
                return i
        return -1
    
    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def binarySearch(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1
    
    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def search_LowerBound(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums)

        while left < right:
            mid = left + (right - left) // 2 # Avoids potential overflow

            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        if left == len(nums) or nums[left] != target:
            return -1
        return left
    
    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def search_UpperBound(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid

        if left == 0 or nums[left - 1] != target:
            return -1
        return left - 1