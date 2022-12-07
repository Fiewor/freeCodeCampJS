//? https://leetcode.com/problems/longest-common-prefix/

var longestCommonPrefix = function (strs) {
  if (strs.length == 0) return "";
  let pre = strs[0];
  for (let i = 1; i < strs.length; i++) {
    while (strs[i].indexOf(pre) != 0) pre = pre.substring(0, pre.length - 1);
  }
  console.log("flow".indexOf("flow"));
  return pre;

  //! compare two strings
  // let count = 0;

  // strs = strs.sort();
  // let first = strs[0];
  // let last = strs[strs.length - 1];
  // let length = last.length;

  // while (length) {
  //   if (first[count] === last[count]) count++;
  //   length--;
  // }

  // return !count ? "" : strs[0].substring(0, count);
};

const strs = ["flower", "flow", "flight"];
// ["dog", "racecar", "car"];
// ["aaa","aa","aaa"]
// strs =
let res = longestCommonPrefix(strs);
console.log(res);
