// https://leetcode.com/problems/two-sum/submissions/1136959665/

var twoSum = function (nums, target) {
  for (let i = 0; i < nums.length; i++) {
    let index = nums.indexOf(target - nums[i]);
    if (nums.includes(target - nums[i]) && index !== i) {
      return [i, index];
    }
  }
};

let nums = [3, 2, 4];
// nums = [2, 7, 11, 15],
target = 6;
//   target = 9;

console.log(twoSum(nums, target));
