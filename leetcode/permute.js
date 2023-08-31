// https://leetcode.com/problems/permutations/

var permute = function (nums) {
  let res = [];

  if (nums.length === 1) return [nums.slice()];

  for (let i = 0; i < nums.length; i++) {
    let n = nums.shift();
    let perms = permute(nums);

    for (const perm of perms) {
      perm.push(n);
    }
    res.push(...perms);
    nums.push(n);
  }

  return res;
};

//! another approach
// const permute = (nums, set = [], ans = []) => {
//   if (!nums.length) ans.push([...set]);

//   for (let i = 0; i < nums.length; i++) {
//     const newNums = nums.filter((_, index) => index !== i);
//     set.push(nums[i]);
//     permute(newNums, set, ans);
//     set.pop();
//   }

//   return ans;
// };

permute([1, 2, 3]);
