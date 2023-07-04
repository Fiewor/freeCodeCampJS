// https://leetcode.com/problems/evaluate-reverse-polish-notation/

var evalRPN = function (tokens) {
  let operators = ["+", "-", "*", "/"],
    stack = [];

  for (let i = 0; i < tokens.length; i++) {
    if (operators.includes(tokens[i])) {
      if (stack.length >= 2) {
        let first = stack.pop();
        let second = stack.pop();
        if (tokens[i] === "+") stack.push(second + first);
        if (tokens[i] === "-") stack.push(second - first);
        if (tokens[i] === "*") stack.push(second * first);
        if (tokens[i] === "/") stack.push(Math.trunc(second / first));
      }
    } else {
      stack.push(+tokens[i]);
    }
  }
  if (stack.length === 1) return stack[0];
  else return evalRPN(stack);
};

let tokens = [
  "10",
  "6",
  "9",
  "3",
  "+",
  "-11",
  "*",
  "/",
  "*",
  "17",
  "+",
  "5",
  "+",
];
//  ["4", "13", "5", "/", "+"];
// tokens = ["2", "1", "+", "3","*"];
let res = evalRPN(tokens);
console.log(res);
