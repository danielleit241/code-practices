class Solution:
    # O(n^2) Time | O(1) Space
    def twoSum_BruteForce(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    # O(nlogn) Time | O(n) Space
    def twoSum_TwoPointer(self, nums: list[int], target: int) -> list[int]:
        left = 0
        right = len(nums) - 1
        nums = sorted([(num, i) for i, num in enumerate(nums)])
        while left < right:
            current_sum = nums[left][0] + nums[right][0]
            if current_sum == target:
                return [nums[left][1], nums[right][1]]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
      
    # O(n) Time | O(n) Space
    def twoSum_HashMap_TwoPass(self, nums: list[int], target: int) -> list[int]:
        map = {}
        for i, num in enumerate(nums):
            map[num] = i
        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in map and map[complement] != i:
                return [i, map[complement]]
            
    # O(n) Time | O(n) Space
    def twoSum_HashMap_OnePass(self, nums: list[int], target: int) -> list[int]:
        map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in map:
                return [map[complement], i]
            map[num] = i
    
