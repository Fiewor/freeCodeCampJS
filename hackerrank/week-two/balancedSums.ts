// https://www.hackerrank.com/challenges/one-month-preparation-kit-sherlock-and-array/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D%5B%5D=preparation-kits&playlist_slugs%5B%5D%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D%5B%5D=one-month-week-two

function balancedSums(arr: number[]): string {
  // Write your code here
  let leftSum = 0,
    rightSum = arr.reduce((a, b) => a + b, 0);
  for (let i = 0; i < arr.length; i++) {
    rightSum -= arr[i];
    if (leftSum === rightSum) return "YES";
    leftSum += arr[i];
  }
  return "NO";
}

let array = [5, 6, 8, 11];
console.log(balancedSums(array));
