function truckTour(petrolpumps) {
  let graph = {};

  for (let i = 0; i < petrolpumps.length; i++) {
    let start = petrolpumps[i];
    console.log(i + 1)
    for (
      let j = (i === petrolpumps.length - 1) ? (petrolpumps.length - 3) : i + 1;
      j <= petrolpumps.length;
      j++
    ) {
      console.log(j);
    }
    start = {};
    if (petrolpumps[i] !== start) {
    }
    // start[]
  }
}
let pumps = [
  [1, 5], // a
  [10, 3], // b
  [3, 4], // c
];
let result = truckTour(pumps);
