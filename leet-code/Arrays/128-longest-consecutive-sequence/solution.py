class Solution:
    # Time Complexity: O(N log N) due to sorting
    # Space Complexity: O(N) for the set
    def longestConsecutive_Sort(self, nums: list[int]) -> int:
        if not nums:
            return 0

        nums = sorted(set(nums))
        longest_streak = 1
        current_streak = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                current_streak += 1
            else:
                current_streak = 1
            longest_streak = max(longest_streak, current_streak)
        return longest_streak   
    

    # Time Complexity: O(N)
    # Space Complexity: O(N) for the set
    def longestConsecutive_Set(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        nums_set = set(nums)
        longest = 0
        for num in nums_set:
            if num - 1 not in nums_set:
                current = 1
                next_num = num + 1
                while next_num in nums_set:
                    current += 1
                    next_num += 1
                longest = max(longest, current)
        return longest
    