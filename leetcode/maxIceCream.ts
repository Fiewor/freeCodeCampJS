// https://leetcode.com/problems/maximum-ice-cream-bars/

function maxIceCream(costs: number[], coins: number): number {
  let count = 0;
  costs.sort((a, b) => a - b);
  while (
    count < costs.length && // haven't bought all the icecream
    costs[count] <= coins // iceream left can still be bought with available coins
  ) {
    coins -= costs[count];
    count++;
  }
  return count;
}

let // costs = [1, 6, 3, 1, 2, 5],
  //   coins = 20;
  costs = [1, 3, 2, 4, 1],
  coins = 7;
// costs = [10,6,8,7,7,8], coins = 5
let result = maxIceCream(costs, coins);
console.log(result);
