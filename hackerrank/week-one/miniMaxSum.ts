// Question: https://www.hackerrank.com/challenges/one-month-preparation-kit-mini-max-sum/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D%5B%5D=preparation-kits&playlist_slugs%5B%5D%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D%5B%5D=one-month-week-one

function miniMaxSum(arr: number[]): void {
  let minSum = 0,
    maxSum = 0;

  arr.sort((a, b) => a - b);

  for (let i = 0; i < arr.length; i++) {
    if (i != arr.length - 1) minSum += arr[i];
    if (i != 0) maxSum += arr[i];
  }

  console.log(`${minSum} ${maxSum}`);
}

let array = [1, 2, 3, 4, 5];
console.log(miniMaxSum(array));
