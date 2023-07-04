// https://leetcode.com/problems/daily-temperatures/

// top-down approach
var dailyTemperatures = function (temperatures) {
  let n = temperatures.length;
  let stack = new Array();
  let res = new Array(n).fill(0);
  for (let i = 0; i < n; i++) {
    while (stack.length && temperatures[i] > temperatures[stack.at(-1)]) {
      let idx = stack.pop();
      res[idx] = i - idx;
    }
    stack.push(i);
  }
  return res;
};

// bottom-up approach -

// var dailyTemperatures = function(temperatures) {
//     let n = temperatures.length, stack = []
//     let res = new Array(n).fill(0)

//     for(let i = n - 1; i >= 0; i--){
//       while(stack.length && temperatures[i] >= temperatures[stack.at(-1)]){
//         stack.pop()
//       }
//       res[i] = stack.at(-1) - i || 0
//       stack.push(i)
//     }
//     return res
// };

let temperatures = [73, 74, 75, 71, 69, 72, 76, 73];
let res = dailyTemperatures(temperatures);
console.log(res);
