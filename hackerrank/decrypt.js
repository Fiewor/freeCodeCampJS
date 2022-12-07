function decryptPassword(s) {
  // Write your code here
  let arr = s.split(""),
    map = new Map();

  for (let i = 0; i < arr.length - 1; ++i) {
    if (i + 1 == arr.length) break;
    if (/[1-9]/g.test(arr[i])) {
      map.set(arr[i], i);
      arr[i] = 0;
      //   arr.unshift(arr[i]);
    } else {
      if (/[a-z]/g.test(arr[i]) && /[A-Z]/g.test(arr[i + 1])) {
        let temp = arr[i + 1];
        arr[i + 1] = arr[i];
        arr[i] = temp;
        arr.splice(i + 2, 0, "*");
        i += 2;
      }
    }
  }

  return [...map.keys()].reverse().join("") + arr.join("");
}

let s = "aP1pL5e";
// "51Pa*0Lp*0e";
let res = decryptPassword(s);
console.log(res);
