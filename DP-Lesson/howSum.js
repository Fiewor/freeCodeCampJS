// return an array containing any combinations of elements that add up to exactly the targetSum
// if no such combination, return null
// if multiple possible combinations, return anyone

//? asks the question - how will you do it? (combinatoric problem)

function howSum(targetSum, numbers, memo = {}) {
  //! recursive solution
  //   if (targetSum === 0) return [];
  //   if (targetSum < 0) return null;
  //   for (const num of numbers) {
  //     const rem = targetSum - num;
  //     const result = howSum(rem, numbers);
  //     if (result) return [...result, num];
  //   }
  //   return null;

  //! memoized solution
  if (memo[targetSum]) return memo[targetSum];
  else {
    if (targetSum === 0) return [];
    if (targetSum < 0) return null;
    for (const num of numbers) {
      const rem = targetSum - num;
      const result = howSum(rem, numbers, memo);
      if (result) {
        memo[targetSum] = [...result, num];
        return memo[targetSum];
      }
    }
    memo[targetSum] = null;
    return null;
  }
}

console.log(howSum(7, [5, 3, 4, 7]));
