function solution(year) {
  //   return Math.ceil(year/100)
  // write a function that takes creates a new property name to a cent object using the word equivalent of a number
  let cent = {},
    equiv,
    yearString = year.toString();
  let ones = [
    "",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
    "twenty",
  ];
  const centify = (num) => (cent[ones[num]] = num);
  console.log(centify(19));
  console.log(yearString[0]);
  if (year <= 100) return 1;
  year < 1000
    ? centify(yearString[0])
    : centify(`${yearString[0]}${yearString[1]}`);
  for (const key in cent) equiv = key;
  equiv;
  return yearString[yearString.length - 1] >= 1
    ? +cent[equiv] + 1
    : +cent[equiv];
}

let result = solution(1905);
console.log(result);
