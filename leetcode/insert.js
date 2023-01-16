// https://leetcode.com/problems/insert-interval/

function insert(intervals, newInterval) {
  let interval = insertArray(intervals, newInterval);
  let arr = [];
  for (let i = 0; i < interval.length; i++) {
    let currInterval = interval[i];
    // check if nextInterval overlaps with interval[i]
    while (i < interval.length && arraysOverlap(currInterval, interval[i])) {
      currInterval = mergeOverlapping(currInterval, interval[i]);
      i++;
    }
    i--;
    arr.push(currInterval);
  }
  return arr;
}

function insertArray(originalArray, arrayToInsert) {
  let index = getUpperBound(originalArray, arrayToInsert);
  if (index === originalArray.length) {
    originalArray.push(arrayToInsert);
    return originalArray;
  } else {
    let before = originalArray.slice(0, index);
    let after = originalArray.slice(index);
    return [...before, arrayToInsert, ...after];
  }
}

function getUpperBound(arr, newArr) {
  let start = 0,
    end = arr.length - 1,
    ans = arr.length;
  while (start <= end) {
    let mid = Math.floor((start + end) / 2);
    if (arr[mid][0] > newArr[0]) {
      ans = mid;
      end = mid - 1;
    } else {
      start = mid + 1;
    }
  }
  return ans;
}

function arraysOverlap(a, b) {
  return Math.min(a[1], b[1]) - Math.max(a[0], b[0]) >= 0;
}

function mergeOverlapping(a, b) {
  return [Math.min(a[0], b[0]), Math.max(a[1], b[1])];
}

let intervals = [[1, 5]],
  newInterval = [2, 3];
// intervals = [
//     [1, 2],
//     [3, 5],
//     [6, 7],
//     [8, 10],
//     [12, 16],
//   ],
//   newInterval = [4, 8];
//   intervals = [
//     [1, 3],
//     [6, 9],
//   ],
//   newInterval = [2, 5];
console.log(insert(intervals, newInterval));
