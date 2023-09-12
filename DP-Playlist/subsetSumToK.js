const f = (n, k, arr) => {
  if (k === 0) return true;
  if (n === 0) return k === arr[0];
  else {
    let noTake = f(n - 1, k, arr);
    let take = false;
    if (arr[n] <= k) take = f(n - 1, k - arr[n], arr); // you can only take current element if it's not greater than target

    return take || noTake;
  }
};

const fDp = (n, k, arr, dp = {}) => {
  if (k === 0) return true;
  if (n === 0) return k === arr[0];
  else {
    if (dp[(n, k)]) return dp[(n, k)];
    let noTake = f(n - 1, k, arr, dp);
    let take = false;
    if (arr[n] <= k) take = f(n - 1, k - arr[n], arr);

    dp[(n, k)] = take || noTake;
    return dp[(n, k)];
  }
};

const subsetSumToK = (arr, k) => {
  let n = arr.length;
  // return f(n - 1, k, arr);
  return fDp(n - 1, k, arr);
};

const subsetSumToKTab = (arr, k) => {
  let n = arr.length;
  let tab = Array(n).fill(Array(k).fill(false));

  for (let i = 1; i < n; i++) tab[i][0] = true;

  tab[0][arr[0]] = true;

  for (let i = 1; i < n; i++) {
    for (let target = 1; target <= k; target++) {
      let take = false;

      if (arr[i] <= target) take = tab[i - 1][target - arr[i]];
      let noTake = tab[n - 1][target];

      tab[i][target] = take || noTake;
    }
  }

  return tab[n - 1][k];
};

const subsetSumToKSpaceOp = (arr, k) => {
  let n = arr.length;
  let prev = Array(n).fill(false),
    curr = Array(k).fill(false);

  prev[0] = true;
  curr[0] = true;

  if (arr[0] <= k) prev[arr[0]] = true; // only do this if array element is less than target

  for (let i = 1; i < n; i++) {
    for (let target = 1; target <= k; target++) {
      let take = false;

      if (arr[i] <= target) take = prev[target - arr[i]];
      let noTake = prev[target];

      curr[target] = take || noTake;
    }
    prev = curr;
  }

  return prev[k];
};

let arr = [2, 3, 1, 1],
  k = 4;
console.log(subsetSumToK(arr, k));
console.log(subsetSumToKTab(arr, k));
console.log(subsetSumToKSpaceOp(arr, k));
