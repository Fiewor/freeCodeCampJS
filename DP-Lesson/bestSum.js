// a function taht returns an array containing the shortest combination of numbers that add up to exactly the targetSum
// if there's a tie for the shortest combination, you may return any one of the shortest

//? asks the question - what is the 'best' way to do it? (optimization problem)

//* only include memo arg in memoization approach
function bestSum(targetSum, numbers, memo = {}) {
  //! memoization approach
  if (memo[targetSum]) return memo[targetSum];
  else {
    let shortestCombination = null;
    if (targetSum === 0) return [];
    if (targetSum < 0) return null;
    else {
      for (const num of numbers) {
        const rem = targetSum - num;
        const res = bestSum(rem, numbers, memo);
        if (res) {
          const newCombination = [...res, num];
          if (
            !shortestCombination ||
            newCombination.length < shortestCombination.length
          ) {
            shortestCombination = newCombination;
          }
        }
      }
      memo[targetSum] = shortestCombination;
      return memo[targetSum];
    }
  }
  //   //! recursive approach
  //   // base case
  //   let shortestCombination = null;
  //   if (targetSum === 0) return [];
  //   if (targetSum < 0) return null;
  //   else {
  //     for (const num of numbers) {
  //       const rem = targetSum - num;
  //       const res = bestSum(rem, numbers);
  //       if (res) {
  //         const newCombination = [...res, num];
  //         if (
  //           !shortestCombination ||
  //           newCombination.length < shortestCombination.length
  //         ) {
  //           shortestCombination = newCombination;
  //         }
  //       }
  //     }
  //     return shortestCombination;
  //   }
}

//! complexity
// m - target sum
// n - numbers.length

//? brute-force---------------------------------------
//* time
// it's going to be some sort of exponential
// tree drawing, in general, has the exponential - number of nodes in a tree will be the branching factor to the height power 😣
// branching factor is n -> branch for every choice of number (given by the for loop)
// height of the tree will be the targetSum (worstcase)
//? O(n^m*m) // the *m is from the extra copying operation on line 15 (which at worstcase is m)
// exponential time (really bad)

//* space
// O(m^2) - at least m cause of the stack of the recursion
// each stack, needs to store it's own shortestCombination arrayv which is m at worst
//? so space complexity is O(m*m) => O(m^2)

//?----------------------------------------------------

//? brute-force---------------------------------------
//* time = O(m^2*n) - polynomial time (much better than bruteforce)
// memo can store at worst, m(targetSum) different keys
// each key can explore/branch into at worst every number in numbers (i.e. n)
// extra m (that results in m^2) is from the spreading operation
//* space = O(m^2) - memo keys have m possibilities, but for each of those keys, their values could be an array of length m
//?----------------------------------------------------

console.log(bestSum(7, [5, 3, 4, 7]));
console.log(bestSum(8, [2, 3, 5]));
console.log(bestSum(8, [1, 4, 5]));
console.log(bestSum(100, [1, 2, 5, 25]));
