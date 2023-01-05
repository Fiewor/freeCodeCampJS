// https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

var findMinArrowShots = function (points) {
  points.sort((a, b) => a[1] - b[1]);

  //! solution 1
  //   let num = 1,
  //     previous = 0;
  //   for (let current = 1; current < points.length; current++) {
  //     // if starting of current balloon is after the ending of previous  alloon, then you'll need a new arrow to burst the current balloon
  //     if (points[current][0] > points[previous][1]) {
  //       num++;
  //       previous = current;
  //     }
  //   }
  //   return num;

  //! solution 2
  let num = 1,
    curEnd = points[0][1],
    start,
    end;
  for (let i = 0; i < points.length; i++) {
    (start = points[i][0]), (end = points[i][1]);
    if (start > curEnd) {
      num++;
      curEnd = end;
    }
  }
  return num;
};

let points =
  // [
  //   [1, 2],
  //   [3, 4],
  //   [5, 6],
  //   [7, 8],
  // ];
  [
    [10, 16],
    [2, 8],
    [1, 6],
    [7, 12],
  ];
let res = findMinArrowShots(points);
console.log(res);
