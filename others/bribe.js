const bribe = (q) => {
  let sum = 0,
    more = [];
  for (let i = 0; i < q.length; i++) {
    if (q[i] > q[i + 1]) {
      if (q[i] - q[i + 1] > 2) {
        more.push(q[i] - q[i + 1]);
      }
      sum += q[i] - q[i + 1];
    }
  }
  console.log(more)
  let result = Math.max(...more) > 2 ? "Too Chaotic" : sum;
  console.log(result);
};
// 2 2 2 2n
// let q = [5, 1, 2, 3, 7, 8, 6, 4];
let q = [1, 2, 5, 3, 7, 8, 6, 4]
//       1, 2, 3, 4, 5, 6, 7, 8
// 5 6 7 7
// 5 moved from index 4 to index 2   diff -> 2
// 7 moved from index 6 to index 4   diff -> 2
// 8 moved from index 7 to index 5   diff -> 2

// 6 moved from index 5 to index 6   diff -> -1
// 5 moved from index 4 to index 7   diff -> -3
// 3 moved from index 2 to index 3   diff -> -1

// [5, 1, 2, 3, 7, 8, 6, 4];
let ans = bribe(q);
ans;
