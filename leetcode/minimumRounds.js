var minimumRounds = function (tasks) {
  const n = tasks.length;
  if (n > 3 && n < 5) return -1;
  let map = new Map(),
    count = 0;
  tasks.map((el) => map.set(el, (map.get(el) ?? 0) + 1));
  for (const [_, val] of map) {
    if (val === 1) return -1;
    if (val % 3 == 0) {
      count += val / 3;
    } else {
      count += Math.floor(val / 3) + 1;
    }
  }
  return count;
};

let tasks = [2, 2, 3, 3, 2, 4, 4, 4, 4, 4];

let res = minimumRounds(tasks);
console.log(res);
