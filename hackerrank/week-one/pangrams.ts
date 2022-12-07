// https://www.hackerrank.com/challenges/one-month-preparation-kit-pangrams/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D%5B%5D=preparation-kits&playlist_slugs%5B%5D%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D%5B%5D=one-month-week-one

function pangrams(s: string): string {
  let map = new Map();
  for (let i = 0; i < s.length; i++) {
    if (map.has(s[i].toLowerCase()) || s == " ") continue;
    else map.set(s[i].toLowerCase(), 1);
  }
  if ([...map.values()].reduce((a, b) => a + b, 0) == 27) return "pangram";
  return "not pangram";
}

let str = "We promptly judged antique ivory buckles for the next prize";
console.log(pangrams(str));
