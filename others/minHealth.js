const minHealth = (arr, armor) => {
  // ? Link: https://leetcode.ca/2022-04-16-2214-Minimum-Health-to-Beat-Game/
  //! Dynamic Programming approach
  // let yes = 1, no = 1;
  // for (let i = arr.length - 1; i >= 0; --i) {
  //   // yes -> min health needed if you use the armor once
  //   // no -> min health needed if you don't use armor

  //   // use Health in current level -> no + Math.max(0, arr[i] - armor)
  //   // use in Health in previous level -> yes + arr[i]
  //   let newYes = Math.min(no + Math.max(0, arr[i] - armor), yes + arr[i]);
  //   let newNo = no + arr[i];

  //   yes = newYes;
  //   no = newNo;
  // }
  // return Math.min(yes, no);

  //!  Greedy approach -> We greedily use the armor at the level with the greatest damage.
  // without armor we need -> 1 + sum(arr)
  // armor can take damage of -> min(max(A), armor), saving us this amount of health

  // (1 + sum(arr)) - (min(max(A), armor))
  let sum = 0,
    max = Number.MIN_SAFE_INTEGER;
  for (let i = 0; i < arr.length; i++) {
    sum += arr[i];
    if (arr[i] > max) max = arr[i];
  }
  return 1 + sum - Math.min(max, armor);
};

let arr = [2, 7, 4, 3],
  armor = 4;
let result = minHealth(arr, armor);
console.log("result: ", result);
