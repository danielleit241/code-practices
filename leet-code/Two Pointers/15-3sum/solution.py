class Solution:
    def threeSum_BruteForce(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        res = set()
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                        res.add(triplet)
        return list(res)

    # Time Complexity: O(n^2)
    # Space Complexity: O(n)
    def threeSum_Set(self, nums: list[int]) -> list[list[int]]:
        if set(nums) == {0}:
            return [[0,0,0]]

        seen_triplets = set()
        n = len(nums)
        res = []
        for i in range(n - 2):
            seen = {}
            for j in range(i + 1, n):
                current = nums[j]
                target = - current - nums[i]
                if target in seen:
                    triplets = tuple(sorted([current, target, nums[i]]))
                    if triplets not in seen_triplets:
                        res.append(triplets)
                        seen_triplets.add(triplets)
                seen[current] = j
        return res
              

    # Time Complexity: O(n^2)
    # Space Complexity: O(log n) for sorting
    def threeSum_TwoPointers(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            target = -nums[i]
            left = i + 1
            right = n - 1
            while left < right:
                sum = nums[left] + nums[right]
                if sum == target:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif sum < target:
                    left += 1
                elif sum > target:
                    right -= 1
        return res

solution = Solution()
print(solution.threeSum_Set([-1, 0, 1, 2, -1, -4]))