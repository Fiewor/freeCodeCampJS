function caesarCipher(s: string, k: number): string {
  let str = s.split(""),
    map = new Map(),
    num: number;

  for (let i = 0; i < str.length; i++) {
    if (str[i].toUpperCase() === str[i]) {
      map.set(i, true);
      str[i] = str[i].toLowerCase();
    }
    num = str[i].charCodeAt(0);

    if (num < 97 || num > 122) continue;
    let sum = num + k;
    if (sum > 122) {
      while (sum > 122) {
        sum = 96 + (sum - 122);
      }
    }

    if (map.has(i)) {
      str[i] = String.fromCharCode(sum).toUpperCase();
    } else {
      str[i] = String.fromCharCode(sum);
    }
  }

  return str.join("");
}

let str = "www.abc.xy",
  // "middle-Outz",
  // "Abcdefghijklmnopqrstuvwxyz",
  key = 87;
console.log(caesarCipher(str, key));
