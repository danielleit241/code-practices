public class Solution{
    public int LongestConsecutive_Sort(int[] nums){
        if (nums.Length == 0) return 0;
        nums = nums.Distinct().ToArray();
        Array.Sort(nums);

        int longest, current = 1;

        for(int i = 0; i < nums.Length - 1; i++){
            if(nums[i] + 1 == nums[i + 1]){
                current++;
            } else {
                current = 1;
            }
            longest = Math.Max(longest, current);
        }
        return longest;
    }

    public int LongestConsecutive_Set(int[] nums){
        if (nums.Length == 0) return 0;
        HashSet<int> numSet = new HashSet<int>(nums);
        int longest = 0;
        foreach(int num in numSet){
            if(!numSet.Contains(num - 1)){
                int current = 1;
                int nextNum = num + 1;
                while(numSet.Contains(nextNum)){
                    current++;
                    nextNum++;
                }
                longest = Math.Max(longest, current);
            }
        }
        return longest;
    }
}