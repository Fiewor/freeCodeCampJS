const minMax = (arr) => {
  let totalSum = 0,
    min = Number.POSITIVE_INFINITY,
    max = Number.NEGATIVE_INFINITY;

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] < min) min = arr[i];
    if (arr[i] > max) max = arr[i];
    totalSum += arr[i];
  }

  console.log(totalSum - max); // minSum
  console.log(totalSum - min); // maxSum
};

let result = minMax([1, 3, 5, 7, 9]);
