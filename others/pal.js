function palindromeIndex(s) {
  console.log(s.replace(/\W/gi, "").toLowerCase());
  // Write your code here
  let start = 0,
    end = s.length - 1;

  while (start < end) {
    if (s[start] !== s[end]) {
      if (start == end - 1) return start;
      end = end - 1;
      while (start < end) {
        if (s[start] !== s[end]) return start;
        return end + 1;
      }
    }
    start++;
    end--;
  }
  return -1;
}
// let input = "aaab";
let input = "A man, a, plan, a canal. Panama!";
// let input = "abcgdcba";
let result = palindromeIndex(input);
console.log(result);
