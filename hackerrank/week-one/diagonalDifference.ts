// https://www.hackerrank.com/challenges/one-month-preparation-kit-diagonal-difference/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D%5B%5D=preparation-kits&playlist_slugs%5B%5D%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D%5B%5D=one-month-week-one
function diagonalDifference(arr: number[]): number {
  let ltr = 0,
    rtl = 0;
  for (let i = 0; i < arr.length; i++) {
    for (let j = 0; j < arr.length; j++) {
      if (i === j) {
        ltr += arr[i][j];
        rtl += arr[i][arr.length - 1 - j];
      }
    }
  }
  return Math.abs(ltr - rtl);
}

let matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [9, 8, 9],
];
console.log(diagonalDifference(matrix));
