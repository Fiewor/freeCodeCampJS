function isPossible(a, b, c, d) {
  while (c >= a && d >= b) {
    if (c === d) {
      break;
    } else if (c > d) {
      if (d > b) {
        c %= d;
        console.log("c: ", c);
      } else {
        if ((c - a) % d === 0) {
          console.log("inside first yes");
          return "Yes";
        } else {
          console.log("inside first no");
          return "No";
        }
      }
    } else {
      if (c > a) {
        d %= c;
        console.log("d: ", d);
      } else {
        if ((d - b) % c === 0) {
          console.log("d", d);
          console.log("b", b);
          console.log("c", c);
          console.log("inside second yes");
          return "Yes";
        } else {
          console.log("inside second no");
          return "No";
        }
      }
    }
  }
  if (c === a && d === b) {
    return "Yes";
  } else {
    return "No";
  }
}

let result = isPossible(1, 1, 5, 2);
console.log("result: ", result);
