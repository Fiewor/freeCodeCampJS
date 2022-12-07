// Question: https://www.hackerrank.com/challenges/one-month-preparation-kit-sparse-arrays/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D%5B%5D=preparation-kits&playlist_slugs%5B%5D%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D%5B%5D=one-month-week-one

function matchingStrings(strings: string[], queries: string[]): number[] {
  // O(n^2) solution
  let stringCopy = strings.slice(),
    result = new Array(queries.length).fill(0);

  for (let i = 0; i < queries.length; i++) {
    for (let j = 0; j < strings.length; j++) {
      if (queries[i] == strings[j]) result[i]++;
    }
  }

  return result;
}

let strings = ["ab", "ab", "abc"],
  queries = ["ab", "abc", "bc"];

console.log(matchingStrings(strings, queries));
