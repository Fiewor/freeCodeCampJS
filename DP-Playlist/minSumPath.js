function f(i, j, grid) {
  if (i === 0 && j === 0) return grid[i][j];
  if (i < 0 || j < 0) return Number.MAX_SAFE_INTEGER;

  let up = grid[i][j] + f(i - 1, j, grid),
    left = grid[i][j] + f(i, j - 1, grid);

  return Math.min(up, left);
}

function fMemo(i, j, arr, dp = {}) {
  if (i === 0 && j === 0) return arr[i][j];
  if (i < 0 || j < 0) return Number.MAX_SAFE_INTEGER;
  if (dp[i + "," + j]) return dp[i + "," + j];
  let up = arr[i][j] + fMemo(i - 1, j, arr, dp),
    left = arr[i][j] + fMemo(i, j - 1, arr, dp);

  dp[i + "," + j] = Math.min(up, left);
  return dp[i + "," + j];
}

function minSumPath(grid) {
  let n = grid.length;
  let m = grid[0].length;

  // return f(n - 1, m - 1, grid);
  return fMemo(n - 1, m - 1, grid);
}

function minSumPathTab(grid) {
  let n = grid.length;
  let m = grid[0].length;

  let tab = Array(n).fill(Array(m).fill(0));

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      if (i === 0 && j === 0) {
        tab[i][j] = grid[0][0];
      } else {
        let up = grid[i][j],
          left = grid[i][j];

        if (i > 0) {
          up += tab[i - 1][j];
        } else {
          up += Number.MAX_SAFE_INTEGER;
        }
        if (j > 0) {
          left += tab[i][j - 1];
        } else {
          left += Number.MAX_SAFE_INTEGER;
        }

        tab[i][j] = Math.min(up, left);
      }
    }
  }

  return tab[n - 1][m - 1];
}

function minSumPathSpaceOp(grid) {
  let n = grid.length,
    m = grid[0].length,
    prev = Array(m).fill(0);

  for (let i = 0; i < n; i++) {
    let curr = Array(m).fill(0);

    for (let j = 0; j < m; j++) {
      if (i === 0 && j === 0) {
        curr[j] = grid[0][0];
      } else {
        let up = grid[i][j],
          left = grid[i][j];

        if (i > 0) {
          up += prev[j]; // requiring previous row's j column
        } else {
          up += Number.MAX_SAFE_INTEGER;
        }

        if (j > 0) {
          left += curr[j - 1]; // current row's j -1 column
        } else {
          left += Number.MAX_SAFE_INTEGER;
        }
        curr[j] = Math.min(up, left);
      }
    }
    prev = curr;
  }
  return prev[m - 1];
}

let grid = [
  [5, 9, 6],
  [11, 5, 2],
];

console.log(minSumPath(grid));
console.log(minSumPathTab(grid));
console.log(minSumPathSpaceOp(grid));
