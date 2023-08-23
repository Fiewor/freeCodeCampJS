const f = (n, arr) => {
  if (n === 0) return arr[0];
  let pick = arr[n];
  if (n > 1) pick += f(n - 2, arr);
  let nonPick = f(n - 1, arr);
  return Math.max(pick, nonPick);
};

const fMemo = (n, arr, dp = {}) => {
  if (n === 0) return arr[0];
  if (dp[n]) return dp[n];

  let pick = arr[n];
  if (n > 1) pick += f(n - 2, arr);
  let nonPick = f(n - 1, arr);
  dp[n] = Math.max(pick, nonPick);
  return dp[n];
};

const houseRobber = (arr) => {
  let withoutLast = fMemo(arr.length - 2, arr.slice(0, arr.length - 1));
  let withoutFirst = fMemo(arr.length - 2, arr.slice(1, arr.length));

  return Math.max(withoutFirst, withoutLast);
};

const tab = (arr) => {
  let n = arr.length;
  let dp = Array(n).fill(0);
  dp[0] = arr[0];

  for (let i = 1; i < n; i++) {
    let pick = dp[i];

    if (pick > 1) pick += dp[i - 2];
    let nonPick = dp[i - 1];
    dp[i] = Math.max(pick, nonPick);
  }

  return dp[n - 1];
};

const spaceOp = (arr) => {
  let n = arr.length,
    prev = arr[0],
    prev2 = 0;

  for (let i = 1; i < n; i++) {
    let pick = arr[i];
    if (i > 1) pick += prev2;
    let nonPick = prev;
    let curr = Math.max(pick, nonPick);
    prev2 = prev;
    prev = curr;
  }

  return prev;
};

const houseRobberTab = (arr) => {
  let n = arr.length,
    withoutFirst = [],
    withoutLast = [];

  for (let i = 0; i < n; i++) {
    if (i !== 0) withoutFirst.push(arr[i]);
    if (i !== n - 1) withoutLast.push(arr[i]);
  }

  return Math.max(tab(withoutLast), tab(withoutFirst));
  // return Math.max(spaceOp(withoutLast), spaceOp(withoutFirst));
};

console.log(houseRobberTab([1, 2, 3, 1]));
console.log(houseRobber([2, 3, 2]));
console.log(houseRobber([1, 2, 3, 1]));
