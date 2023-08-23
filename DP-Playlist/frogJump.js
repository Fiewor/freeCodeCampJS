const f = (n, heights, memo = { 0: 0 }) => {
  if (n === 0) return 0;
  if (memo[n]) return memo[n];

  let right = Number.MAX_SAFE_INTEGER;
  let left = f(n - 1, heights, memo) + Math.abs(heights[n] - heights[n - 1]);
  if (n > 1)
    right = f(n - 2, heights, memo) + Math.abs(heights[n] - heights[n - 2]);
  memo[n] = Math.min(left, right);

  return memo[n];
};

const frogJump = (n, heights) => {
  return f(n - 1, heights, {});
};

const frogJumpTab = (n, heights) => {
  let prev = 0,
    prev2 = 0;
  for (let i = 1; i < heights.length; i++) {
    let fs = prev + Math.abs(heights[i] - heights[i - 1]);
    let ss = Number.MAX_SAFE_INTEGER;

    if (i > 1) ss = prev2 + Math.abs(heights[i] - heights[i - 2]);
    curr = Math.min(fs, ss);
    prev2 = prev;
    prev = curr;
  }

  return prev;
};

const helper = (n, k, heights) => {
  if (n === 0) return 0;

  let minSteps = Number.POSITIVE_INFINITY;

  for (let j = 1; j <= k; j++) {
    if (n - j >= 0) {
      if (dp[n]) return dp[n];
      let jump =
        helper([n - j], k, heights) + Math.abs(heights[n] - heights[n - j]);
      dp[n] = Math.min(minSteps, jump);
      minSteps = dp[n];
    }
  }

  return minSteps;
};

const frogJumpWithKStepsMemo = (n, k, heights, dp = {}) => {
  return helper(n - 1, k, heights, dp);
};

const frogJumpWithKSteps = (n, k, heights) => {
  return helper(n - 1, k, heights);
};

const frogJumpWithKStepsTab = (n, k, heights) => {
  let dp = Array(n + 1).fill(0);

  for (let i = 1; i <= n; i++) {
    let minSteps = Number.MAX_SAFE_INTEGER;

    for (let j = 1; j < k; j++) {
      if (i - j >= 0) {
        let jump = dp[i - j] + Math.abs(heights[i] - heights[i - j]);
        minSteps(minSteps, jump);
      }
    }

    dp[i] = minSteps;
  }

  return dp[n - 1];
};

let resu = frogJump(6, [30, 10, 60, 10, 60, 50]);
let res = frogJumpWithKStepsTab(6, [30, 10, 60, 10, 60, 50]);

const ans = frogJumpWithKSteps(3, 2, [30, 10, 60]);

console.log(res);
