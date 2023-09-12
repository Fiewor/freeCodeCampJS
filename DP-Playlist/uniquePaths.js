// recursive solution
// time complexity: O(2^m*n)
// space complexity: O((m - 1) + (n - 1)) [i.e. path length]

function f(m, n) {
  if (m === 0 && n === 0) return 1; // one possible path
  if (m < 0 || n < 0) return 0; // outside grid
  return f(m - 1, n) + f(m, n - 1); // move up + left until get to 0,0
}

// DP Memoization solution
// time complexity: O(n * m)
// space complexity: O((n - 1) + (m - 1)) + O(n * m) [i.e. stack space + dp space(?)]
function fMemo(m, n, dp = {}) {
  // base cases
  if (m === 0 && n === 0) return 1; // one possible path
  if (m < 0 || n < 0) return 0; // outside grid

  if (dp[(m, n)]) return dp[(m, n)];

  dp[(m, n)] = f(m - 1, n) + f(m, n - 1); // move up + left until get to 0,0
  return dp[(m, n)];
}

function uniquePaths(m, n) {
  //   return f(m - 1, n - 1);
  return fMemo(m - 1, n - 1);
  // because 0-indexing
  // e.g. for (2,2) grid is:
  // 0 1
  // 0 1
}

// tabulation solution
// time complexity: O(n * m)
// space complexity: O(n * m)
function uniquePathsTab(m, n) {
  let tab = Array(n).fill(Array(m).fill(0));
  // tab[0][0] = 1;
  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if (i === 0 && j === 0) {
        tab[i][j] = 1;
      } else {
        let up = 0,
          left = 0;
        if (i > 0) up = tab[i - 1][j];
        if (j > 0) left = tab[i][j - 1];
        tab[i][j] = up + left;
      }
    }
  }
  tab;

  return tab[m - 1][n - 1];
}

function uniquePathsSpaceOp(m, n) {
  let prev = Array(n).fill(0);

  for (let i = 0; i < m; i++) {
    let cur = Array(m).fill(0);

    for (let j = 0; j < n; j++) {
      if (i === 0 && j === 0) {
        cur[j] = 1;
      } else {
        let up = 0,
          left = 0;
        if (i > 0) up = prev[j];
        if (j > 0) left = cur[j - 1];
        cur[j] = up + left;
      }
    }
    prev = cur;
  }
  return prev[n - 1];
}

var uniquePathsBetterSpaceOp = function (m, n) {
  let prev = Array(n).fill(1);

  for (let i = 1; i < m; i++) {
    let curr = Array(m).fill(1);

    for (let j = 1; j < n; j++) {
      curr[j] = prev[j] + curr[j - 1];
    }
    prev = curr;
  }

  return prev[n - 1];
};

console.log(uniquePaths(4, 4));
console.log(uniquePathsTab(2, 2));
console.log(uniquePathsSpaceOp(2, 2));
