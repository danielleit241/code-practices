from collections import Counter

class Solution:
    # Time complexity O(n log n) and space complexity O(n)
    def topKFrequent_SortMap(self, nums: list[int], k: int) -> list[int]:
        map = {}
        for num in nums:
            map[num] = map.get(num, 0) + 1
        sorted_map = sorted(map.items(), key=lambda x: x[1], reverse=True)
        return [item[0] for item in sorted_map[:k]]
    
    # Time complexity O(n log n) and space complexity O(n)
    def topKFrequent_Counter(self, nums: list[int], k: int) -> list[int]:
        count = Counter(nums)
        map = dict(sorted(count.items(), key=lambda x: x[1], reverse=True))
        return list(map.keys())[:k]

    # Time complexity O(n*k) and space complexity O(n)
    def topKFrequent_FindMax(self, nums: list[int], k: int) -> list[int]:
        map = {}
        for num in nums:
            map[num] = map.get(num, 0) + 1
        result = []
        for _ in range(k):
            max_key = max(map, key=map.get) # Dùng hàm max để tìm key có value lớn nhất
            result.append(max_key)
            del map[max_key]
        return result
    
    # Time complexity O(n) and space complexity O(n)
    def topKFrequent_BucketSort(self, nums: list[int], k: int) -> list[int]:
        map_count = {}
        freq = [[] for _ in range(len(nums) + 1)]
        for num in nums:
            map_count[num] = 1 + map_count.get(num, 0)
        
        for num, count in map_count.items():
            freq[count].append(num)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
    

solution = Solution()
print(solution.topKFrequent_SortMap([1,1,1,2,2,3], 2))
print(solution.topKFrequent_FindMax([1,1,1,2,2,3], 2))
print(solution.topKFrequent_Counter([1,1,1,2,2,3], 2))