// https://leetcode.com/problems/min-cost-climbing-stairs/description/

// Memoized DP solution
let f = function (n, cost, dp = {}) {
  if (n <= 1) return 0;
  else {
    if (dp[n]) return dp[n];

    let climbOne = cost[n - 1] + f(n - 1, cost, dp);
    let climbTwo = cost[n - 2] + f(n - 2, cost, dp);

    dp[n] = Math.min(climbOne, climbTwo);
    return dp[n];
  }
};

var minCostClimbingStairs = function (cost) {
  let n = cost.length;
  return f(n, cost);
};

function minCostClimbingStairsTab(cost) {
  let n = cost.length;

  let dp = Array(n).fill(0);

  for (let i = 2; i <= n; i++) {
    let climbOne, climbTwo;
    climbOne = cost[i - 1] + dp[i - 1];
    climbTwo = cost[i - 2] + dp[i - 2];

    dp[i] = Math.min(climbOne, climbTwo);
  }

  return dp[n];
}

console.log(minCostClimbingStairsTab([10, 15, 20]));
