function findMedian(arr: number[]): number {
  // Write your code here
  arr = arr.sort((a, b) => a - b);
  return arr[Math.floor(arr.length / 2)];
}

let nums = [1, 3, 2, 5, 4];
