var search = function (nums, target) {
  let start = 0,
    end = nums.length - 1;
  while (start <= end) {
    let mid = start + Math.floor((end - start + 1) / 2);
    if (nums[mid] === target) return mid;
    if (nums[mid] < target) start = mid;
    else end = mid - 1;
  }
  return -1;
};

let result = search([2, 5]);
console.log(result);
