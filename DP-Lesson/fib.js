// a function that returns the nth number of the fibonacci sequence
//! recursi ve approach
function fib(n) {
  if (n <= 2) return n;
  return fib(n - 1) + fib(n - 2);
}
//! memoization approach
function fib_memo(n, memo = {}) {
  if (memo[n]) return memo[n];
  if (n <= 2) return n;
  memo[n] = fib(n - 1, memo) + fib(n - 2, memo);
  return memo[n];
}

//! tabulation approach
function fib_tab(n) {
  let memo = new Array(n + 1).fill(0);
  memo[1] = 1;
  memo[2] = 1;
  let i = 3;
  while (i <= n) {
    memo[i] = memo[i - 1] + memo[i - 2];
    i++;
  }
  return memo[n];
}

function fib_tab_different(n) {
  let table = new Array(n + 1).fill(0);
  table[1] = 1;
  for (let i = 0; i <= table.length; i++) {
    table[i + 1] += table[i];
    table[i + 2] += table[i];
  }
  return table[n];
}

console.log(fib_memo(40));
console.log(fib_tab(40));
console.log(fib_tab_different(40));
