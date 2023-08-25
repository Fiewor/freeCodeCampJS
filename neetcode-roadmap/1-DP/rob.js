// https://leetcode.com/problems/house-robber/description/

var f = (n, nums, dp = {}) => {
  if (n === 0) return nums[0];
  if (n === 1) return Math.max(nums[0], nums[1]);
  else {
    if (dp[n]) return dp[n];

    let pick = nums[n] + f(n - 2, nums, dp);
    let noPick = f(n - 1, nums, dp);

    dp[n] = Math.max(pick, noPick);
    return dp[n];
  }
};

var rob = function (nums) {
  return f(nums.length - 1, nums);
};

var robTab = function (nums) {
  // return f(nums.length-1, nums)
  let n = nums.length;
  let tab = Array(n).fill(0);
  tab[0] = nums[0];
  tab[1] = Math.max(nums[0], nums[1]);

  for (let i = 2; i <= n; i++) {
    let pick = nums[i] + tab[i - 2];
    let noPick = tab[i - 1];

    tab[i] = Math.max(pick, noPick);
  }

  return tab[n - 1];
};

var robSpaceOp = function (nums) {
  if (nums.length === 0) return 0;
  if (nums.length === 1) return nums[0];

  let prev = nums[0],
    prev2 = Math.max(nums[0], nums[1]);

  for (let i = 2; i < nums.length; i++) {
    let temp = prev2;
    prev2 = Math.max(prev2, prev + nums[i]);
    prev = temp;
  }

  return prev2;
};

console.log(robTab([1, 2, 3, 1]));
console.log(robSpaceOp([1, 2, 3, 1]));
