// Question: https://www.hackerrank.com/challenges/one-month-preparation-kit-lonely-integer/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D%5B%5D=preparation-kits&playlist_slugs%5B%5D%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D%5B%5D=one-month-week-one

function lonelyInteger(a: number[]): number {
  // using bitwise XOR
  let ans = 0;
  for (const el of a) {
    ans ^= el;
  }
  return ans;
}

let a = [1, 2, 3, 4, 3, 2, 1];
console.log(lonelyInteger(a));
