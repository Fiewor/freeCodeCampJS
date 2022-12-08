// https://www.hackerrank.com/challenges/one-month-preparation-kit-two-arrays/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D%5B%5D=preparation-kits&playlist_slugs%5B%5D%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D%5B%5D=one-month-week-one

function twoArrays(k: number, A: number[], B: number[]): string {
  // works too:
  // return A.some(i => A.filter(n => n === i).length > B.filter(x => x >= k - i).length) ? "NO" : "YES";

  A = A.sort((a, b) => a - b).reverse();
  B = B.sort((a, b) => a - b);
  for (let i = 0; i < A.length; i++) {
    if (A[i] + B[i] < k) return "NO";
  }
  return "YES";
}

let // k = 10,
  //     A = [2, 1, 3],
  //     B = [7, 8, 9];

  // k = 5,
  // A = [1, 2, 2, 1],
  // B = [3, 3, 3, 4];

  k = 1,
  A = [0, 1],
  B = [0, 2];
console.log(twoArrays(k, A, B));
