var findLonely = function (nums: number[]): number[] {
  let map = new Map();
  nums.map((el) => map.set(el, (map.get(el) ?? 0) + 1));
  return [...map.keys()].filter(
    (el) => map.get(el) === 1 && !map.has(el + 1) && !map.has(el - 1)
  );
};

let nums = [1, 3, 5, 3];
console.log(findLonely(nums));
