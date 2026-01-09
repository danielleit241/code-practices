from statistics import median

class Solution:
    def findMedianSortedArrays_Sorted1(self, nums1: list[int], nums2: list[int]) -> float:
        return median(sorted(nums1 + nums2))
    
    def findMedianSortedArrays_Sorted2(self, nums1: list[int], nums2: list[int]) -> float:
        nums = sorted(nums1 + nums2)
        length = len(nums)
        mid = length // 2

        if length % 2 == 0:
            return (nums[mid - 1] + nums[mid]) / 2.0
        else:
            return nums[mid]

    def findMedianSortedArrays_Merge(self, nums1: list[int], nums2: list[int]) -> float:
        merged = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1

        while i < len(nums1):
            merged.append(nums1[i])
            i += 1
        while j < len(nums2):
            merged.append(nums2[j])
            j += 1

        length = len(merged)
        mid = length // 2
        if length % 2 == 0:
            return (merged[mid - 1] + merged[mid]) / 2.0
        else:
            return merged[mid]
        
    def findMedianSortedArrays_BinarySearch(self, nums1: list[int], nums2: list[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(A) > len(B):
            A, B = B, A

        left, right = 0, len(A) - 1
        while True:
            mA = (left + right) // 2
            mB = half - mA - 2

            aLeft = A[mA] if mA >= 0 else float('-infinity')
            aRight = A[mA + 1] if (mA + 1) < len(A) else float('infinity')

            bLeft = B[mB] if mB >= 0 else float('-infinity')
            bRight = B[mB + 1] if (mB + 1) < len(B) else float('infinity') 

            if aLeft <= bRight and bLeft <= aRight:
                if total % 2:
                    return min(aRight, bRight)
                else:
                    return (max(aLeft, bLeft) + min(aRight, bRight)) / 2
            elif aLeft > bRight:
                right = mA - 1
            else:
                left = mA + 1
