// https://leetcode.com/problems/contains-duplicate/

public class Solution {
    public bool ContainsDuplicate(int[] nums) {

        // hashmap solution
        var map = new Dictionary<int, int>();
        for(int i = 0; i < nums.Length; i++)
        {
            if(map.ContainsKey(nums[i])) // if(map.GetValueOrDefault(nums[i]) == 1)
                return true;
            
            map.Add(nums[i], 1);
        }
        return false;
    }

    // set solution
    HashSet<int> set = new HashSet<int>(nums);
    return set.Count != nums.Length;
}

