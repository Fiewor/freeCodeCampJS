function permuteUnique(nums, set = [], ans = []) {
  if (!nums.length) ans.push([...set]);

  for (let i = 0; i < nums.length; i++) {
    const newNums = nums.filter((_, index) => index !== i);
    set.push(nums[i]);
    permuteUnique(newNums, set, ans);
    set.pop();
  }

  return ans;
}

const res = permuteUnique([1, 2, 3]);
console.log(res);
