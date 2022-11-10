function computeClosestToZero(ts) {
  if (ts.length === 0) return 0;
  let ans = 0;
  for (let i = 0; i < ts.length; i++) {
    if (
      Math.abs(ts[i]) < Math.abs(ts[ans]) ||
      (Math.abs(ts[i]) === Math.abs(ts[ans]) && ts[i] > 0)
    ) {
      ans = i;
    }
  }
  return ts[ans];
}

let arr = [-15, -7, -9, -14, -12];
// [7, 5, 9, 1, 4];
let result = computeClosestToZero(arr);

// let small = Number.POSITIVE_INFINITY, ans = -1
//     for(let i = 0; i < ts.length; i++){
//         let abs = Math.abs(ts[i])
//         if(abs < small){
//             ans = ts[i]
//             small = abs
//         }
//         if(abs === small){
//             abs = Math.max(ans, ts[i])
//         }
//     }
//     return ans;
