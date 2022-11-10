const towerBreaker = (n: number, m: number): number => {
  // ! Working solution: passed all testcases
  if (m === 1) return 2;
  if (n % 2 === 0) return 2;
  return 1;

  // ! My idea: didn't cut it
  // let x = m,
  //   count = 0;
  // for (let i = 1; i < m; i++) {
  //   // i is what's removed
  //   let y = x - i; // y is what's left after removal
  //   console.log(y);
  //   if (y >= 1 && y < x && x % y === 0) {
  //     // (x % y) <- height of tower divided by
  //     console.log(y);
  //     i;
  //     // if what is left after reduction is greater than 1 and greater than leftover
  //     x -= i;
  //     x;
  //     count++;
  //   }
  // }
  // return count + (1 % n) === 0 ? 1 : 2;
};

let n = 3,
  m = 7;

let res = towerBreaker(n, m);
console.log(res);
