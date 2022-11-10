var topKFrequent = function (words, k) {
  // frequency counter
  let map = new Map();
  words.map((el) => {
    map.set(el, (map.get(el) ?? 0) + 1);
  });
  let result = [...map.keys()].sort((a, b) => {
    if (map.get(a) === map.get(b)) return a > b ? 1 : -1;
    if (map.get(a) < map.get(b)) return 1;
    return -1;
  });
  // .slice(0, k);
  console.log(result);
  //
};

let words = ["i", "love", "leetcode", "i", "love", "coding"];
k = 3;

topKFrequent(words, k);
