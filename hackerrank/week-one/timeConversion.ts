function timeConversion(s) {
  let arr = s.split(":");
  let period = arr.at(-1);

  if (/PM/.test(period)) {
    if (arr[0] !== "12") arr[0] = 12 + +arr[0];
  }

  if (/AM/.test(period)) {
    if (12 + +arr[0] === 24) arr[0] = "00";
  }

  arr[arr.length - 1] = arr[arr.length - 1].replace(/(P|A)M/, "");
  return arr.join(":");
}

let s = "11:05:45PM";
console.log(timeConversion(s));
