const minWindow = (s, t) => {
  let map = new Map();
  t.split("").map((el) => map.set(el, (map.get(el) ?? 0) + 1));

  let counter = t.length,
    start = 0,
    end = 0,
    minStart = 0,
    minLen = Number.MAX_SAFE_INTEGER;

  while (end < s.length) {
    if (map[s[end]] > 0) counter--;
    map[s[end]]--;
    end++;
    while (counter === 0) {
      if (end - start < minLen) {
        minStart = start;
        minLen = end - start;
      }
      map[s[start]]++;
      if (m[s[start]] > 0) counter++;
      start++;
    }
  }
  return minLen === Number.MAX_SAFE_INTEGER
    ? ""
    : s.substring(minStart, minLen);
};

let res = minWindow("aaa", "aaa");
console.log(res);
