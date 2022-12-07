// https://www.hackerrank.com/challenges/one-month-preparation-kit-countingsort1/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D%5B%5D=preparation-kits&playlist_slugs%5B%5D%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D%5B%5D=one-month-week-one

function countingSort(arr: number[]): number[] {
  // Write your code here
  let nums = new Array(100).fill(0);
  for (const el of arr) {
    nums[el]++;
  }
  return nums;
}

let arr = [1, 1, 3, 2, 1];
console.log(countingSort(arr));
