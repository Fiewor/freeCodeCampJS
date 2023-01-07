// https://www.hackerrank.com/test/3fmlgi1ase7/questions/a2b68fq8p7b

function palindromeIndex(s) {
  // Write your code here
  let i = 0,
    j = s.length - 1;
  while (i < j) {
    if (s[i] != s[j]) {
      if (isPalindrome(s, i + 1, j)) return i;
      else return j;
    }
    i++;
    j--;
  }
  return -1;
}

function isPalindrome(str, start, end) {
  let i = start,
    j = end;
  while (i < j) {
    if (str[i] !== str[j]) return false;
    i++;
    j--;
  }
  return true;
}

console.log(
  palindromeIndex("quyjjdcgsvvsgcdjjyq")
  // palindromeIndex("hgygsvlfcwnswtuhmyaljkqlqjjqlqkjlaymhutwsnwcwflvsgygh")
);
