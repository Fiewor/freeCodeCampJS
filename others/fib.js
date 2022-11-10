const fib = (num) => {
  return num < 3 ? 1 : fib(num - 1) + fib(num - 2);
};

let result = fib(5);
console.log(result);
