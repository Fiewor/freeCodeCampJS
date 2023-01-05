// https://leetcode.com/problems/delete-columns-to-make-sorted/description/
public class Solution {
    public int MinDeletionSize(string[] strs) {
        var n = strs[0].Length; var count = 0;
        for(int i = 0; i < n; i++)
        {
            for(int j = 1; j < strs.Length; j++)
            {
                if(strs[j][i] < strs[j - 1][i]) // not sorted
                {
                    count++;
                    break;
                }
            }
        }
        return count;
    }
}
