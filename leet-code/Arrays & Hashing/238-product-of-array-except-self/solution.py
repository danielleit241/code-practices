class Solution:
    # Time Complexity: O(n^2)
    # Space Complexity: O(1)
    def productExceptSelf_BruteForce(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [1] * n
        for i in range(n):
            for j in range(n):
                if i != j:
                    result[i] *= nums[j]
        return result
    
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def productExceptSelf_Division(self, nums: list[int]) -> list[int]:
        total_product = 1
        zero_count = 0
        for num in nums:
            if num != 0:
                total_product *= num
            else:
                 zero_count += 1
        n = len(nums)
        for i in range(n):
            if zero_count > 1:
                nums[i] = 0
            elif zero_count == 1:
                if nums[i] == 0:
                    nums[i] = total_product
                else:
                    nums[i] = 0
            else:
                nums[i] = total_product // nums[i]
        return nums
    
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def productExceptSelf_TwoPass(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [1] * n
        for i in range(1, n):
            res[i] = res[i-1] * nums[i-1]
        right = 1
        for i in range(n - 1, -1, -1):
            res[i] *= right
            right *= nums[i]
        return res

        

    
solution = Solution()
print(solution.productExceptSelf_BruteForce([1, 2, 3, 4]))
print(solution.productExceptSelf_TwoPass([1, 2, 3, 4]))
print(solution.productExceptSelf_Division([1, 2, 3, 4]))
print (solution.productExceptSelf_Division([0, 0]))
