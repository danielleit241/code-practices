class Solution:
    # Time Complexity: O(N)
    # Space Complexity: O(N)
    def findDuplicate_Set(self, nums: list[int]) -> int:
        setNums = set()
        for num in nums:
            if num in setNums:
                return num
            setNums.add(num)

    # Time Complexity: O(N)
    # Space Complexity: O(N)
    def findDuplicate_HashMap(self, nums: list[int]) -> int:
        countMap = {}
        for num in nums:
            if num in countMap:
                return num
            countMap[num] = 1

    # Time Complexity: O(N)
    # Space Complexity: O(1)
    def findDuplicate_FastSlowPointer(self, nums: list[int]) -> int:
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow