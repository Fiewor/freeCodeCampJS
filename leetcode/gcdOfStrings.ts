// https://leetcode.com/problems/greatest-common-divisor-of-strings/

function gcdOfStrings(str1: string, str2: string): string {
  if (str1 + str2 !== str2 + str1) return "";
  let maxLength = gcd(str1.length, str2.length);
  return str1.slice(0, maxLength);
}

function gcd(x: number, y: number): number {
  if (y === 0) return x;
  return gcd(y, x % y);
}

let str1 = "ABABAB", str2 = "ABAB";
console.log(gcdOfStrings(str1, str2));
