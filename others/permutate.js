/**
 * @param {number[]} nums
 * @return {number[][]}
 */
const permutate = (str) => {
  let res = [];

  if (str.length === 1) return [str];

  for (let i = 0; i < str.length; i++) {
    let char = str[i];
    let rest = str.substring(0, i) + str.substring(i + 1);

    let perms = permutate(rest);

    for (const perm of perms) {
      res.push(char + perm);
    }
  }

  return res;
};

console.log(permutate("abc"));
