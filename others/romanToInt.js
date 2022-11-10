var romanToInt = (roman) => {
  let list = { I: 1, II: 2, III: 3, IV: 4, V: 5, VI: 6 };

  return list["roman"];
  // convert roman to number
  // "I" - 1
  // "II" - 2
  // "III" - 3
  // "IV" - 4
  // "V" - 5
};
let result = romanToInt("II");
console.log(result);
