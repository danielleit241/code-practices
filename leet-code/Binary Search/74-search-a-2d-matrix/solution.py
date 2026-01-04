class Solution:
    # Time Complexity: O(m * n)
    # Space Complexity: O(1)
    def searchMatrix_Linear(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        for row in matrix:
            for val in row:
                if val == target:
                    return True
        return False

    # Time Complexity: O(log(m * n))
    # Space Complexity: O(1)
    def searchMatrix_BinarySearch(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, (rows * cols) - 1

        while left <= right:
            mid = left + (right - left) // 2
            val = matrix[mid // cols][mid % cols]

            if val == target:
                return True
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False
    
    # Time Complexity: O(log(m * n))
    # Space Complexity: O(1)
    def searchMatrix_BinarySearch_UpperBound(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, (rows * cols)

        while left < right:
            mid = left + (right - left) // 2
            val = matrix[mid // cols][mid % cols]

            if val <= target:
                left = mid + 1
            else:
                right = mid
        
        if left == 0:
            return False
        return matrix[(left - 1) // cols][(left - 1) % cols] == target

    # Time Complexity: O(log(m * n))
    # Space Complexity: O(1)
    def searchMatrix_BinarySearch_LowerBound(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, (rows * cols)

        while left < right:
            mid = left + (right - left) // 2
            val = matrix[mid // cols][mid % cols]

            if val < target:
                left = mid + 1
            else:
                right = mid

        if left == (rows * cols):
            return False   
        return matrix[left // cols][left % cols] == target