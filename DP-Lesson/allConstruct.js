// the function should return a 2D array containing all of the ways that the 'target' can be constructed by concatenating elements of the 'wordBank' array
// each element of the 2D array should represent one combination that constructs the 'target'
// you may reuse elements of 'wordBank' as many times as needed

function allConstruct(target, wordBank, memo = {}) {
  if (memo[target]) return memo[target];
  //! memoization approach
  if (target === "") return [[]];
  let ans = [];
  for (const word of wordBank) {
    if (target.startsWith(word)) {
      const suffix = target.slice(word.length);
      const suffixWays = allConstruct(suffix, wordBank, memo);
      const targetWays = suffixWays.map((way) => [word, ...way]);
      ans.push(...targetWays);
    }
  }
  memo[target] = ans;
  return ans;

  //   //! recursive approach
  //   if (target === "") return [[]];
  //   let ans = [];
  //   for (const word of wordBank) {
  //     if (target.startsWith(word)) {
  //       const suffix = target.slice(word.length);
  //       const suffixWays = allConstruct(suffix, wordBank);
  //       const targetWays = suffixWays.map((way) => [word, ...way]);
  //       ans.push(...targetWays);
  //     }
  //   }
  //   return ans;
}

// time complexity - O(n^m) <- you can't really do better than this because you have to represent all the combinations
// space complexity - O(m)

console.log(
  allConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"])
);
console.log(allConstruct("purple", ["purp", "p", "ur", "le", "purpl"]));
