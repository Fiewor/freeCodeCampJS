const superDigit = (n, k) => {
  let p = n.repeat(k);
  if (p.length === 1) return p;
  else {
    return superDigit([...p].reduce((a, b) => +a + +b).toString(), (k = 1));
  }
};

let n = "9875";
let ans = superDigit(n, 4);
console.log(ans);
