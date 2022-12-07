const solve = (arr: number[]): number[] => {
  let helper: number[] = [];
  return mini(arr, helper, 0, arr.length - 1);
};

const mini = (
  arr: number[],
  helper: number[],
  low: number,
  high: number
): number[] => {
  let mid = Math.floor((low + high) / 2);
  if (low < high) {
    mini(arr, helper, low, mid);
    mini(arr, helper, mid + 1, high);
  }
  return sort(arr, helper, low, mid, high);
};

const sort = (
  arr: number[],
  helper: number[],
  low: number,
  mid: number,
  high: number
): number[] => {
  // copy elements of original array into helper array
  for (let i = 0; i < arr.length; i++) {
    helper[i] = arr[i];
  }
  let helperLeft = low;
  let helperRight = mid + 1;
  let curr = low;
  while (helperLeft <= mid && helperRight <= high) {
    if (helper[helperLeft] <= helper[helperRight]) {
      arr[curr] = helperLeft;
      helperLeft++;
    } else {
      arr[curr] = helperRight;
      helperRight++;
    }
    curr++;
  }

  // copy remainder from left side of helper into arr
  let rem = mid - helperLeft;
  for (let i = 0; i <= rem; i++) {
    arr[curr + i] = helper[helperLeft + i];
  }

  return arr;
};

let unsorted = [6, 3, 8, 9, 1, 5, 0];
let ans = solve(unsorted);
console.log(ans);
