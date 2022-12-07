function findWinners(matches) {
  const winMap = new Map(),
    loseMap = new Map();
  for (let i = 0; i < matches.length; i++) {
    winMap.set(matches[i][0], (winMap.get(matches[i][0]) ?? 0) + 1);
    loseMap.set(matches[i][1], (loseMap.get(matches[i][1]) ?? 0) + 1);
  }
  const winners = [...winMap.keys()]
    .filter((el) => !loseMap.has(el))
    .sort((a, b) => a - b);
  const losers = [...loseMap.keys()]
    .filter((el) => loseMap.get(el) === 1)
    .sort((a, b) => a - b);

  return [winners, losers];
}

const matches = [
  [2, 3],
  [1, 3],
  [5, 4],
  [6, 4],
];
// matches = [
//   [1, 3],
//   [2, 3],
//   [3, 6],
//   [5, 6],
//   [5, 7],
//   [4, 5],
//   [4, 8],
//   [4, 9],
//   [10, 4],
//   [10, 9],
// ];

console.log(findWinners(matches));
