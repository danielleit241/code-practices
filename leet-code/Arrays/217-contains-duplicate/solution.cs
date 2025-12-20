public class Solution{
    public bool ContainsDuplicateUsingHashSet(int[] nums){
        HashSet<int> seen = new HashSet<int>();
        foreach(int num in nums){
            if(seen.Contains(num)){
                return true;
            }
            seen.Add(num);
        }
        return false;
    }

    public bool ContainsDuplicatUsingDict(int[] nums){
        Dictionary<int, int> countMap = new Dictionary<int, int>();
        foreach(int num in nums){
            if(countMap.ContainsKey(num)){
                return true;
            }
            countMap[num] = 1;
        }    
        return false;
    }

    public bool ContainsDuplicateCompareLength(int[] nums){
        HashSet<int> uniqueNums = new HashSet<int>(nums);
        return uniqueNums.Count < nums.Length;
    }
}