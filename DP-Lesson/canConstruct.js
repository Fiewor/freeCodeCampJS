// the function should return a boolean indicating whether or not the 'target' can be constructed by concatenating elements of the 'wordbank' array
// you may resuse elements of 'wordBank' as many times as needed

function canConstruct(target, wordBank, memo = {}) {
  // ! memoized solution
  if (memo[target]) return memo[target];
  if (target === "") return true;
  for (const word of wordBank) {
    // if word is a prefix
    if (target.startsWith(word)) {
      const suffix = target.slice(word.length);
      if (canConstruct(suffix, wordBank, memo)) {
        memo[target] = true;
        return memo[target];
      }
    }
  }
  memo[target] = false;
  return memo[target];

  // ! recursive solution
  //   if (target === "") return true;
  //   for (const word of wordBank) {
  //     if (target.startsWith(word)) {
  //       // word is a prefix
  //       const suffix = target.slice(word.length);
  //       if (canConstruct(suffix, wordBank)) return true;
  //     }
  //   }
  //   return false;
}

//! complexity
//? brute-force
// m = target.length
// n = wordBank.length
//* time complexity -> O(n^m*m)
//? explanantion
//* height (the max no. of stack frames you would need on the call stack before getting to the base case)
// height is at most m cause distance from root (targetString) to farthest leaf is at most m (if you have to remove one character at each level to get to base case)
//* branching factor (i.e. from one level of the tree to the next, how does the number of nodes change)
// this factor is dictated by how many words we have in the wordBank
// at worst, we would need to branch out to n nodes at each level (e.g. in this case, if all words in wordBank are prefixes of target)
// in general, visualizing your recursion as a call tree shows that the time complexity is branching factor to the height power
//* *m is added for the extra slie operation that is at most

// space complexity - O(m^2)
// m for height of call stack

//? memoization
// time complexity - O(n *m^2)
// space complexity - O(m^2)

console.log(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]));
console.log(
  canConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])
);
console.log(
  canConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])
);
