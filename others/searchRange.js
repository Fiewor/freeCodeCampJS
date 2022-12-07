// https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

function searchRange(nums, target) {
  if (!nums.includes(target)) return [-1, -1];
  console.log(nums.length);
  // if (nums.length === 1 && nums[0] === target) return [0, 0];
  let arr = [],
    start = 0,
    end = nums.length - 1;
  while (start <= end) {
    let mid = Math.floor((start + end) / 2);
    mid;
    if (nums[mid] === target) {
      if (nums[mid - 1] === target) {
        arr.push(mid - 1);
      }

      !arr.includes(mid) && arr.push(mid);
      start = mid + 1;
    }
    if (mid < target) start = mid + 1;
    // start
    else end = mid;
  }
  return [arr[0], arr.at(-1)];
}

let nums = [5, 7, 7, 8, 8, 10],
  target = 8;
let res;
// = searchRange([1, 3], 1);
// searchRange([1, 3], 1);
console.log(res);
