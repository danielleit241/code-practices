public class Solution {
    public int[] ProductExceptSelf(int[] nums) {
        var n = nums.Length;
        var res = new int[n];

        res[0] = 1;
        for(var i = 1; i < n; i++)
        {
            res[i] = res[i-1] * nums[i-1];
        }

        var right = 1;
        for(var i = n - 1; i >= 0; i--)
        {
            res[i] *= right;
            right *= nums[i];
        }
        
        return res;
    }
}
