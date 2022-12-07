const backtrack = (nums, set = [], ans = []) => {
  if (!nums.length) ans.push([...set]);

  for (let i = 0; i < nums.length; i++) {
    const newNums = nums.filter((_, index) => index !== i);
    set.push(nums[i]);
    backtrack(newNums, set, ans);
    set.pop();
  }

  return ans;
};

const permutate = (nums) => {
  // backtrack()
};

const res = backtrack([1, 2, 3]);
console.log(res);
