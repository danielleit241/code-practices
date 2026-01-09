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
        