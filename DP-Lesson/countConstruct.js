// function should return the number of ways that the 'target' can be constructed by concatenating elements of the 'wordBank' array
// you may reuse elements of 'wordBank' as many times as needed

function countConstruct(target, wordBank, memo = {}) {
  // !memoization solution
  if (memo[target]) return memo[target];
  if (target === "") return 1;
  let count = 0;

  for (const word of wordBank) {
    if (target.indexOf(word) === 0) {
      const suffix = target.slice(word.length);
      count += countConstruct(suffix, wordBank, memo);
    }
  }

  memo[target] - count;
  return memo[target];
  //! recursive solution
  //   let count = 0;
  //   if (target === "") return 1;
  //   else {
  //     for (const word of wordBank) {
  //       if (target.indexOf(word) === 0) {
  //         const suffix = target.slice(word.length);
  //         count += countConstruct(suffix, wordBank);
  //       }
  //     }
  //   }
  //   return count;
}
//! brute force complexity
// time complexity - O(n^m*m) <-exponential
// space complexity - O(m^2)
//! memoized complexity
// time complexity - O(m^2*n) <- polynomial
// space complexity - O(m^2)
console.log(countConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]));
console.log(countConstruct("purple", ["purp", "p", "ur", "le", "purple"]));
