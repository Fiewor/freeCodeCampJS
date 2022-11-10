function gridCheck(grid) {
  grid = grid.map((word) => [...word].sort((a, b) => (a > b ? 1 : -1)));
  for (let i = 0; i < grid.length; i++) {
    let j = 0;
    while (j < grid.length - 1) {
      if (grid[j][i] > grid[j + 1][i]) return "NO";
      j++;
    }
  }
  return "YES";

  // const arr = grid.map(word => [...word].sort());
  //   for(var i = 0;i < arr.length - 1; i++) {
  //       for(var j = 0; j <arr[i].length; j++) {
  //           if(arr[i][j] > arr[i + 1][j]) return "NO";
  //       }
  //   }
  //   return "YES";
}

let grid = ["abc", "hjk", "mpq", "rtv"];
// ["eabcd", "fghij", "olkmn", "trpqs", "xywuv"];
let ans = gridCheck(grid);
console.log(ans);
