//? https://leetcode.com/problems/maximum-subarray/

const maxSubArray = (nums) => {
  // kadane's algorithm
  let maxSoFar = nums[0],
    maxEndingHere = nums[0];

  for (let i = 0; i < nums.length; i++) {
    maxEndingHere = Math.max(maxEndingHere + nums[i], nums[i]);
    maxSoFar = Math.max(maxSoFar, maxEndingHere);
  }
  return maxSoFar;

  // a probably more understandable rewrite
  // let curMax = 0,
  //   maxTillNow = Number.MIN_SAFE_INTEGER;

  // for (const num of nums) {
  //   curMax = Math.max(num, curMax + num);
  //   maxTillNow = Math.max(maxTillNow, curMax);
  // }

  // return maxTillNow;

  // let dp = new Array(nums.length).fill(0);
  // dp[0] = nums[0];
  // let max = dp[0];

  // for (let i = 1; i < nums.length; i++) {
  //   dp[i] = Math.max(nums[i] + dp[i - 1], nums[i]);
  //   max = Math.max(max, dp[i]);
  // }
  // return max;
};

const nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4];
// [5, 4, -1, 7, 8];
let ans = maxSubArray(nums);
console.log(ans);
