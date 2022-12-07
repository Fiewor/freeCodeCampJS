// Question: https://www.hackerrank.com/challenges/one-month-preparation-kit-plus-minus/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D%5B%5D=preparation-kits&playlist_slugs%5B%5D%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D%5B%5D=one-month-week-one

function plusMinus(arr: number[]): void {
  let zeroCount = 0,
    posCount = 0,
    negCount = 0,
    totalCount = 0;

  arr.map((el) => {
    if (el > 0) posCount++;
    if (el < 0) negCount++;
    if (el === 0) zeroCount++;
    totalCount++;
  });

  console.log((posCount / totalCount).toFixed(6));
  console.log((negCount / totalCount).toFixed(6));
  console.log((zeroCount / totalCount).toFixed(6));
}

let arr = [1, 1, 0, -1, -1];
let res = plusMinus(arr);
