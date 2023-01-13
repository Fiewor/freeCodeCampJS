//? asks the question - can you do it? yes or no (decision problem)

function canSum(targetSum, numbers, memo = {}) {
  //   //! recursive solution
  //   if (targetSum === 0) return true;
  //   if (targetSum < 0) return false;
  //   else {
  //     for (const num of numbers) {
  //       const rem = targetSum - num;
  //       if (canSum(rem, numbers)) return true;
  //     }
  //     return false;
  //   }

  //! memoization solution
  if (memo[targetSum]) return memo[targetSum];
  else {
    if (targetSum === 0) return true;
    if (targetSum < 0) return false;
    else {
      for (const num of numbers) {
        const rem = targetSum - num;
        if (canSum(rem, numbers, memo)) {
          memo[targetSum] = true;
          return true;
        }
      }
      memo[targetSum] = false;
      return false;
    }
  }
}

console.log(canSum(7, [2, 4]));
console.log(canSum(300, [7, 14]));
