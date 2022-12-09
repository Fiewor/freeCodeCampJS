// https://www.hackerrank.com/challenges/one-month-preparation-kit-flipping-bits/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D%5B%5D=preparation-kits&playlist_slugs%5B%5D%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D%5B%5D=one-month-week-one

function flippingBits(n: number): number {
  let zeros = new Array(32).fill("0").join("");
  let binary = (n >>> 0).toString(2);
  let z = 32 - binary.length;
  let ans: number[] = [];

  let remBits = zeros.slice(0, z);
  let unsigned = remBits.concat(binary);
  let arr = unsigned.split("");

  arr.map((el) => ans.push(Math.pow(0, +el)));
  return parseInt(ans.join(""), 2);
}

console.log(flippingBits(1));
