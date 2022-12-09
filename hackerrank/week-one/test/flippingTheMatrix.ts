/*
 * Complete the 'flippingMatrix' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts 2D_INTEGER_ARRAY matrix as parameter.
 */

function flippingMatrix(matrix: number[][]): number {
  // Write your code here
  let n = matrix.length / 2,
    total = 0,
    max = 0;
  for (let row = 0; row < n; row++) {
    for (let col = 0; col < n; col++) {
      max = Number.NEGATIVE_INFINITY;

      max = Math.max(matrix[row][col], max);
      console.log(2 * n - col - 1);
      max = Math.max(matrix[row][2 * n - col - 1], max);
      max = Math.max(matrix[2 * n - row - 1][col], max);
      max = Math.max(matrix[2 * n - row - 1][2 * n - col - 1], max);

      total += max;
    }
  }
  return total;
}

let arr = [
  [1, 2, 5, 6],
  [3, 4, 7, 8],
  [3, 4, 7, 8],
  [1, 2, 5, 6],
];

console.log(flippingMatrix(arr));
