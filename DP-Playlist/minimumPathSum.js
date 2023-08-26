function f(i, j, n, triangle) {
  if (i === n - 1) {
    return triangle[n - 1][j];
  } else {
    let down = triangle[i][j] + f(i + 1, j, n, triangle);
    let diagonal = triangle[i][j] + f(i + 1, j + 1, n, triangle);
    return Math.min(down, diagonal);
  }
}

function fMemo(i, j, n, triangle, dp = {}) {
  if (i === n - 1) {
    return triangle[n - 1][j];
  } else {
    if (dp[(i, j)]) return dp[(i, j)];
    let down = triangle[i][j] + f(i + 1, j, n, triangle, dp);
    let diagonal = triangle[i][j] + f(i + 1, j + 1, n, triangle, dp);
    dp[(i, j)] = Math.min(down, diagonal);
    return dp[(i, j)];
  }
}

function minimumPathSum(triangle) {
  let n = triangle.length;
  return fMemo(0, 0, n, triangle);
}

function minimumPathSumTab(triangle) {
  let n = triangle.length;
  let tab = Array(n).fill(Array(n).fill(0));

  for (let i = 0; i < n; i++) {
    tab[n - 1][i] = triangle[n - 1][i];
  }

  for (let i = n - 2; i >= 0; i--) {
    for (let j = i; j >= 0; j--) {
      let down = triangle[i][j] + tab[i + 1][j];
      let diagonal = triangle[i][j] + tab[i + 1][j + 1];

      tab[i][j] = Math.min(down, diagonal);
    }
  }

  return tab[0][0];
}

let minimumPathSumSpaceOp = (triangle) => {
  let n = triangle.length;
  let front = Array(n).fill(0);

  for (let i = 0; i < n; i++) {
    front[i] = triangle[n - 1][i];
  }

  for (let i = n - 2; i >= 0; i--) {
    for (let j = i; j >= 0; j--) {
      let down = triangle[i][j] + front[j];
      let diagonal = triangle[i][j] + front[j + 1];

      front[j] = Math.min(down, diagonal);
    }
  }
  return front[0];
};

let triangle = [[1], [2, 3], [3, 6, 7], [8, 9, 6, 10]];

console.log(minimumPathSum(triangle));
console.log(minimumPathSumSpaceOp(triangle));
