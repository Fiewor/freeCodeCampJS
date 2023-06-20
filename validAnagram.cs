// https://leetcode.com/problems/valid-anagram/

// beats 93.43%
public class Solution {
    public bool IsAnagram(string s, string t) {
        if(s.Length != t.Length){
            return false;
        }

        Dictionary <char, int> sMap = new Dictionary<char, int>();
        Dictionary <char, int> tMap = new Dictionary<char, int>();

        foreach(char letter in s){
            if(sMap.ContainsKey(letter)){
                sMap[letter]++;
            }else{
                sMap[letter] = 1;
            }
        }

        foreach(char letter in t){
            if(tMap.ContainsKey(letter)){
                tMap[letter]++;
            }else{
                tMap[letter] = 1;
            }
        }

        foreach(var letter in s){
            if(!tMap.ContainsKey(letter) || sMap[letter] != tMap[letter]){
                return false;
            }
        }
        return true;
    }
}

// beats 25.47%
public class Solution {
    public bool IsAnagram(string s, string t) {
        if (s.Length != t.Length) {
            return false;
        }

        char[] sArray = s.ToCharArray();
        char[] tArray = t.ToCharArray();

        Array.Sort(sArray);
        Array.Sort(tArray);

        string sortedS = new string(sArray);
        string sortedT = new string(tArray);

        return sortedS.Equals(sortedT);
    }
}
