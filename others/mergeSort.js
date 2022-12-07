// mergeSort algorithm from "Cracking the Coding Interview"

const mergeSort = (arr) => {
  let helper = [];
  return merger(arr, helper, 0, arr.length - 1);
};

const merger = (arr, helper, low, high) => {
  low;
  high;
  if (low < high) {
    let mid = Math.floor((low + high) / 2);
    merger(arr, helper, low, mid); // sort left half
    merger(arr, helper, mid + 1, high); // sort right half
  }
  return merge(arr, helper, low, mid, high); // merge them
};

const merge = (arr, helper, low, mid, high) => {
  // copy both halves into helper array
  for (let i = low; i <= high; i++) {
    helper[i] = arr[i];
  }
  helper;
  let helperLeft = low;
  let helperRight = mid + 1;
  let current = low;
  // iterate through helper array
  // compare left and right half
  // copying back the smaller element from the two halves
  // into the original array
  while (helperLeft <= mid && helperRight <= high) {
    if (helper[helperLeft] <= helper[helperRight]) {
      arr[current] = helperLeft;
      helperLeft++;
    } else {
      // if right element is smaller than left element
      arr[current] = helperRight;
      helperRight++;
    }
    current++;
  }
  //   copy the rest of the left side of the arr into the target arr
  let remaining = mid - helperLeft;
  for (let i = 0; i <= remaining; i++) {
    arr[current + 1] = helper[helperLeft + i];
  }

  return arr;
};

let arr = [1, 4, 65, 2, 2, 5, 3, 90, 1, 7];

let res = mergeSort(arr);
console.log(res);
