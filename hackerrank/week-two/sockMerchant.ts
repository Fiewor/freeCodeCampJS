// https://www.hackerrank.com/challenges/one-month-preparation-kit-sock-merchant/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-two

function sockMerchant(n: number, ar: number[]): number {
  // Write your code here
  let map = new Map();
  ar.map((el) => map.set(el, (map.get(el) ?? 0) + 1));
  return [...map.values()]
    .map((el) => Math.floor(el / 2))
    .reduce((a, b) => a + b);
}

let ar = [10, 20, 20, 10, 10, 30, 50, 10, 20],
  num = 9;
// ar = [1, 2, 1, 2, 1, 3, 2],
//   num = 7;
console.log(sockMerchant(num, ar));
