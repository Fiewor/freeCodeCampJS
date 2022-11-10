// function longestCommonSubstring(input: string, string1: string): number {
//   let cell: any[] = new Array(input.length).fill(
//     new Array(string1.length).fill(0)
//   );

//   for (let i = 0; i < input.length; i++) {
//     for (let j = 0; j < string1.length; j++) {
//       if (input[i] === string1[j]) {
//         if (i === 0 && j === 0) cell[i][j] = 1; // for cell[0][0], set to 1
//         if (i === 0 && j !== 0) cell[i][j - 1] = 1; // for elements on cell 0 that also match, increment previous value by 1
//         // for elements on first column and not first row, increment by max from previous row
//         if (i !== 0 && j === 0) {
//           cell[i][j] = cell[i - 1].filter((el: number) => el != 0)[0] + 1;
//         } else {
//           cell[i][j] = cell[i - 1][j - 1] + 1;
//         }
//         console.log(cell[i][j]);
//       } else {
//         cell[i][j] = 0;
//       }
//     }
//   }
//   cell;
//   return Math.max(...cell[input.length - 1]);
// }

// let ans = longestCommonSubstring("fish", "hish");
// console.log(ans);
