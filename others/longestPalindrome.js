// function longestPalindrome(words) {
//   // palindrome must be mirrorred over the center
//   //   for every string is there a mirror(reverse) of that string in the word array?
//   //   for every mirrorable string, output is Min(occurences of string) + min(occurences of reverse)
//   //   if word is already a plaindrome, if occurences = 1, use it in middle
//   //   if occurences is even, use at both ends of plaindrome

//   //   step 1: get a count of occurences
//   let map = new Map(), count = 0, palFound = false;
//   words.map((el) => map.set(el, (map.get(el) ?? 0) + 1));

//   console.log(words.length*2)

//   // loop through words
//   for (let i = 0; i < words.length; i++) {
//     if (words[i][0] === words[i][1]) {
//       //     // it's a palindrome
//       let occurenceofCurr = map.get(words[i]);
//       palFound;
//       if (occurenceofCurr === 1) {
//         if (!palFound) count += occurenceofCurr * 2;
//         if (palFound && occurenceofCurr % 2 === 0) count += occurenceofCurr * 2;
//       }
//       palFound = true;
//     }
//     let curr = words[i];
//     if (words.includes(curr[1] + curr[0]) && curr[0] !== curr[1]) {
//       count += map.get(curr) * 2;
//     }
//   }
//   return !count ? 0 : count;
// }

function longestPalindrome(words) {
  let map = new Map(),
    unpaired = 0,
    ans = 0;
  for (const word of words) {
    if (!map.has(word)) map.set(word, 0);
    if (word[0] === word[1]) {
      if (map.get(word) > 0) {
        ans += 4;
        unpaired--;
        map.set(word, map.get(word) - 1);
      } else {
        unpaired++;
        map.set(word, map.get(word) + 1);
      }
    }
    let rev = map[1] + map[0];
    if (map.has(rev) && map.get(rev) > 0) {
      ans += 4;
      map.set(word, map.get(word) - 1);
    } else {
      map.set(word, map.get(word) + 1);
    }
  }
  if (unpaired > 0) ans += 2;
  return ans;
}

let words =
  // [
  //   "dd",
  //   "aa",
  //   "bb",
  //   "dd",
  //   "aa",
  //   "dd",
  //   "bb",
  //   "dd",
  //   "aa",
  //   "cc",
  //   "bb",
  //   "cc",
  //   "dd",
  //   "cc",
  // ];
  // ["cc", "ll", "xx"];
  // ["ab","ty","yt","lc","cl","ab"]
  ["lc", "cl", "gg"];
let ans = longestPalindrome(words);
console.log(ans);
