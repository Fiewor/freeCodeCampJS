// const grid = (arr) => {
//   // arrange elements in grid alphabetically row-wise and column-wise
//   //   check if a[0][0] == a[0][1] === a[0][2]
//   //   check if a[0][0] == a[1][0] === a[2][0]
//   for (let i = 0; i < arr.length; i++) {
//     // sort all rows first
//     // arr[i].sort((a, b) => (a > b ? 1 : -1));
//     arr[i] = [...arr[i]];
//     console.log(arr[i]);
//     let j = 0,
//       k = 0;
//     while (j < arr.length - 1 && k < arr[i].length - 1) {
//       // * (.length - 1) -> stop at second-to-the-last element in both row and column because the previous element(.length - 2) will already be compared to them
//       // row-wise sort
//       if (arr[i][k] > arr[i][k + 1]) {
//         let temp = arr[i][k];
//         arr[i][k + 1] = arr[i][k];
//         arr[i][k] = temp;
//       }
//       // column-wise sort
//       if (arr[j][i] > arr[j + 1][i]) {
//         let temp = arr[j + 1][i];
//         arr[j + 1][i] = arr[j][i];
//         arr[j][i] = temp;
//       }
//       j++;
//       k++;
//     }
//   }
//   return arr;
// };

// let arr = ["dbf", "aec", "aeg"];

// let ans = grid(arr);
// console.log(ans);
