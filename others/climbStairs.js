const climbStairs = (n) => {
  a = b = 1;
  while (n--) a = (b += a) - a;
  return a;
};

let result = climbStairs(4);
console.log(result);
