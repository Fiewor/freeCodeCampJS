function minSubArrayLen(target, nums) {
  let i = (j = sum = 0),
    min = Number.MAX_SAFE_INTEGER;
  while (j < nums.length) {
    sum += a[j++];
    aum;
  }

  //   let sum = 0, count = 0, start = 0,
  //     arr = sub = [];
  //   for (let i = 0; i < nums.length - 1; i++) {
  //       if (sum > target) {
  //           sum -= nums[start];
  //           count--;
  //           start++;
  //           sub.shift()
  //         }
  //         if (sum < target) {
  //             sum += nums[i];
  //             count++;
  //             sub.push(nums[i])
  //         }
  //         else {
  //         arr.push(count); // add count
  //         if ((i - count) < nums.length - 1) {
  //           console.log(i - count)
  //           sum -= nums[i - count]; // remove first element

  //         }
  //       }
  //     sub
  //   }
  //   return !arr.length ? 0 : Math.min(...arr);
}

let nums = [2, 3, 1, 2, 4, 3];
let target = 7;

let rs = minSubArrayLen(7, nums);
console.log(rs);
