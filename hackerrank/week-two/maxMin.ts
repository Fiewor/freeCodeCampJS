function maxMin(k: number, arr: number[]): number {
  // Write your code here
  let minDiff = Number.MAX_SAFE_INTEGER;
  arr.sort((a, b) => a - b);

  for (let i = 0; i < arr.length - k + 1; i++) {
    let currDiff = arr[i + k - 1] - arr[i];
    minDiff = Math.min(currDiff, minDiff);
  }

  return minDiff;
}
let arr = [1, 2, 3, 4, 10, 20, 30, 40, 100, 200],
  k = 4;
// arr = [1, 4, 7, 2], k = 3
console.log(maxMin(k, arr));
