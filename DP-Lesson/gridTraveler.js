const gridTraveler_rec = (m, n) => {
  //!recursive solution
  if (n === 0 || m === 0) return 0;
  if (n === 1 && m === 1) return 1;
  return (
    gridTraveler_rec(m - 1, n) + // downwards
    gridTraveler_rec(m, n - 1) // rightwards
  );
};
const gridTraveler_memo = (m, n, memo = {}) => {
  // ! memoization solution
  let key = `${m},${n}`,
    similar = `${n},${m}`; // because 1x2 takes the same number of steps as 2x1 (in general, order doesn't matter)
  if (memo[key] || memo[similar]) return memo[key];
  if (n === 0 || m === 0) return 0;
  if (n === 1 && m === 1) return 1;
  // don't forget to pass down memo by reference
  memo[key] =
    gridTraveler_memo(m - 1, n, memo) + gridTraveler_memo(m, n - 1, memo);
  memo[similar] =
    gridTraveler_memo(m - 1, n, memo) + gridTraveler_memo(m, n - 1, memo);
  return memo[key];
};

function gridTraveler_tab(m, n) {
  // ! tabulation attempt
  const table = Array(m + 1)
    .fill()
    .map(() => Array(n + 1).fill(0));
  table[1][1] = 1; // cause there's only one way to move if you have a 1x1 grid

  for (let i = 0; i <= m; i++) {
    for (let j = 0; j <= n; j++) {
      let curr = table[i][j];
      if (i + 1 <= m) table[i + 1][j] += curr; // down neighbour
      if (j + 1 <= n) table[i][j + 1] += curr; // right neighbour
    }
  }
  return table[m][n];
}

console.log(gridTraveler_memo(3, 3));
console.log(gridTraveler_tab(4, 3));

//! Memoization recipe
//* make it work - correctness
//? visualize it as a tree (for memoization - top-down approach)
//? implement the tree using recursion
//? test it

//* make it efficient - efficiency
//? add a memo object
// key - argument to function call
// value - return value to function calls
//? make sure object is shared among recursive calls
// e.g. by passing them along as args
// remember the default, top-level empty object at top-level (initial call)
//? add base case to return memo values i.e. if(args in memo) return stored memo value
//? store return values into the memo
//? return

//! tabulation recipe
// visualize the problem as a table
// figure out size the table based on the inputs
// initialize the table with default values
// seed the triviala
