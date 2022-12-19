// https://www.hackerrank.com/challenges/one-month-preparation-kit-grid-challenge/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D%5B%5D=preparation-kits&playlist_slugs%5B%5D%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D%5B%5D=one-month-week-two

function gridChallenge(grid: string[]): string {
  // Write your code here
  for (let i = 0; i < grid.length; i++) {
    grid[i] = [...grid[i]].sort().join("");
  }
  for (let i = 0; i < grid.length; i++) {
    for (let j = 1; j < grid[i].length; j++) {
      if (grid[j - 1][i] > grid[j][i]) return "NO";
    }
  }
  return "YES";
}

let grid = ["kc", "iu"];
// ["uxf", "vof", "hmp"];
// ['abc', 'hjk', 'mpq', 'rtv']
// ["zzz", "ade", "efg"];
console.log(gridChallenge(grid));
