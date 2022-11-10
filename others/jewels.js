const numJewelsInStone = (jewels, stones) => {
  let map = new Map();

  [...stones].map((el) => {
    if (jewels.includes(el)) {
      map.set(el, (map.get(el) ?? 0) + 1);
    }
  });

  return [...map.values()]
    .reduce((a, b) => a + b, 0);
};

let result = numJewelsInStone("Af", "AaaddfFf");
console.log(result);
