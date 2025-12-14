class Solution:
    # Solution with O(n^2) time complexity
    def containsDuplicate_Count(self, nums: list[int]) -> bool:
        for num in nums:
            if nums.count(num) > 1:
                return True
        return False
    
    def containsDuplicate_BruteForce(self, nums: list[int]) -> bool:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    return True
        return False
    
    # Solution with O(n log n) time complexity
    def containsDuplicate_Sorting(self, nums: list[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False
    
    # Solution with O(n) time complexity 
    def containsDuplicate_Set(self, nums: list[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
    
    def containsDuplicate_HashMap(self, nums: list[int]) -> bool:
        num_count = {}
        for num in nums:
            if num in num_count:
                return True
            num_count[num] = 1
        return False
    
    def containsDuplicate_SetLength(self, nums: list[int]) -> bool:
        return len(nums) != len(set(nums))