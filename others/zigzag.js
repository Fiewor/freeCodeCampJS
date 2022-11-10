function zigzag(input) {
  let arr = input;
  //Enter your code here
  let mid = (input.length + 1) / 2,
    arr1 = [],
    arr2 = [];
  // for (let i = 0; i < mid; i++) {
  //   arr1.push(input[i]);
  // }
  // for (let i = mid + 1; i < input.length; i++) {
  //   arr2.push(input[i]);
  // }
  // return [...arr1.sort(), input[mid], ...arr2.sort((a, b) => (a > b ? -1 : 1))];
  // for (let i = 0; i < input.length; i++) {
  //   if (i < mid) {
  //     // before middle index
  //     // arrange in ascending order
  //     if (input[i] > input[i + 1]) {
  //       let temp = input[i];
  //       input[i] = input[i + 1];
  //       input[i + 1] = temp;
  //     }
  //   }
  //   if (input[i] < input[i + 1]) {
  //     // after middle index it's in descending order
  //     let temp = input[i];
  //     input[i] = input[i + 1];
  //     input[i + 1] = temp;
  //   }
  // }
  // return arr;
  let n = arr.length;
  let k = (n + 1) / 2;
  for (let i = 0; i < n - 1 && k > 0; i++) {
    let pos = i;
    for (let j = i + 1; j < n; j++) {
      if (j - i > k) break;
      if (arr[j] < arr[pos]) pos = j;
    }
    let temp;
    for (let j = pos; j > i; j--) {
      temp = arr[j];
      arr[j] = arr[j - 1];
      arr[j - 1] = temp;
    }
    k -= pos - 1;
  }
  return arr;
}
let arr = [1, 2, 3, 4, 5, 6, 7];
// let arr2 = [2, 3, 5, 1, 4]
let result = zigzag(arr);
console.log(result);
// expected -> 1 2 3 7 6 5 4
