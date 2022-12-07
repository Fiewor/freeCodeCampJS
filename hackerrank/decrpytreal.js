function decryptPassword(s) {
  arr = s.split("");

  for (let i = arr.length - 1; i >= 0; i--) {
    if (+arr[i] === 0) {
      arr.splice(i, 1, arr[0]);
      arr.shift();
    }

    if (/[A-Z]/g.test(arr[i]) && /[a-z]/g.test(arr[i + 1])) {
      let temp = arr[i + 1];
      arr[i + 1] = arr[i];
      arr[i] = temp;
      i += 2;
    }
  }

  return arr.filter((el) => el !== "*").join("");
}

const s = "51Pa*0Lp*0e";
let res = decryptPassword(s);
console.log(res);
