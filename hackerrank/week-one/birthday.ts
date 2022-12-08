// https://www.hackerrank.com/challenges/one-month-preparation-kit-the-birthday-bar/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D%5B%5D=preparation-kits&playlist_slugs%5B%5D%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D%5B%5D=one-month-week-one

function birthday(s: number[], d: number, m: number): number {
  let start = 0,
    sum = 0,
    count = 0;
  for (let i = 0; i < s.length; i++) {
    sum += s[i];
    if (i - start + 1 === m) {
      if (sum === d) {
        count++;
      }
      sum -= s[start];
      start++;
    }
  }
  return count;
}

let s = [2, 2, 1, 3, 2],
  d = 4,
  m = 2;
console.log(birthday(s, d, m));
