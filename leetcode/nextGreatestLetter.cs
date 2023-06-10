// https://leetcode.com/problems/find-smallest-letter-greater-than-target/


public class Solution {
    public char NextGreatestLetter(char[] letters, char target) {
        int min = int.MaxValue;
        char res = letters[0];

        foreach(char letter in letters){
            int diff = letter - target;
            if(diff > 0 && diff < min){
                min = diff;
                res = letter;
            }
        }

        return res;
    }
}
