function f(m, n, arr, dp = {}) {
  if (m === 0 && n === 0) return 1;

  if (m < 0 || n < 0) return 0;
  if (m >= 0 && n >= 0 && arr[m][n] === -1) return 0;
  if (dp[(m, n)]) return dp[(m, n)];
  else dp[(m, n)] = f(m - 1, n, arr, dp) + f(m, n - 1, arr, dp);

  return dp[(m, n)];
}

function mazeObstacles(m, n, grid) {
  return f(m - 1, n - 1, grid);
}

function mazeObstaclesTab(m, n, grid) {
  let tab = Array(m).fill(Array(n).fill(0));

  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if (i === 0 && j === 0) {
        tab[i][j] = 1;
      } else if (grid[i][j] === -1) {
        tab[i][j] = 0;
      } else {
        let up = 0,
          left = 0;
        if (i > 0) up = tab[i - 1][j];
        if (j > 0) left = tab[i][j - 1];
        tab[i][j] = up + left;
      }
    }
  }
  return tab[m - 1][n - 1];
}

function mazeObstaclesSpaceOp(m, n, grid) {
  let prev = Array(m).fill(0);

  for (let i = 0; i < m; i++) {
    const curr = Array(n).fill(0);

    for (let j = 0; j < n; j++) {
      if (i === 0 && j === 0) {
        curr[j] = 1;
      } else if (grid[i][j] === -1) {
        curr[j] = 0;
      } else {
        let up = 0,
          left = 0;
        if (i > 0) up = prev[j];
        if (j > 0) left = curr[j - 1];

        curr[j] = up + left;
      }
    }
    prev = curr;
  }
  return prev[n - 1];
}

let grid = [[0, 0, 0], [(0, -1, 0)], [(0, 0, 0)]];
console.log(mazeObstacles(2, 2, grid));
console.log(mazeObstaclesTab(2, 2, grid));
console.log(mazeObstaclesSpaceOp(2, 2, grid));
