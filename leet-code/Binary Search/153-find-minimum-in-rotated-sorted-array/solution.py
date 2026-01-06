class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def findMin_Linear(self, nums: list[int]) -> int:
        res = float('inf')
        for num in nums:
            res = min(res, num)
        return res
    
    # Time Complexity: O(log n)
    # Space Complexity: O(1) 
    def findMin_Binary(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        
        if nums[left] < nums[right]:
            return nums[left]
        
        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[right]:
                left = left + 1
            else:
                right = mid

        return nums[left]