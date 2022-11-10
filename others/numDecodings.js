const numDecodings = (s) => {
  if (!s || !s.length) return 0;

  let dp = new Array(s.length + 1).fill(0);
  dp[0] = 1;
  console.log(s[1]);
  dp[1] = s[0] === "0" ? 0 : 1;

  for (let i = 2; i <= dp.length; i++) {
    let first = +s.substring(i - 1, i);
    first;
    let second = +s.substring(i - 2, i);
    second;
    if (first >= 1 && first <= 9) {
      i;
      dp[i] += dp[i - 1];
      console.log(dp[i]);
    }
    if (second >= 10 && second <= 26) {
      dp[i] += dp[i - 2];
      console.log(dp[i]);
    }
  }
  dp;
  return dp[s.length];
};

let result = numDecodings("06");
console.log(result);
