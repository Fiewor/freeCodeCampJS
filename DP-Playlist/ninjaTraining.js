const f = (day, lastDaysTask, points, dp = {}) => {
  if (day === 0) {
    let maxPoint = 0;
    for (let i = 0; i < 3; i++) {
      if (i !== lastDaysTask) maxPoint = Math.max(maxPoint, points[0][i]);
    }
    return maxPoint;
  }

  if (dp[day][lastDaysTask]) return dp[day][lastDaysTask];
  let maxPoint = 0;

  for (let i = 0; i < 3; i++) {
    if (i !== lastDaysTask) {
      maxPoint = Math.max(
        maxPoint,
        points[day][i] + f(day - 1, lastDaysTask, points, dp)
      );
    }
  }

  dp[day][lastDaysTask] = maxPoint;

  return dp[day][lastDaysTask];
};

const ninJaTraining = (n, points) => {
  return f(n - 1, 3, points, dp);
};

const ninJaTrainingTab = (n, points) => {
  const dp = Array(n)
    .fill(0)
    .map((el) => Array(4).fill(0));

  dp[0][0] = Math.max(points[0][1], points[0][2]);
  dp[0][1] = Math.max(points[0][0], points[0][2]);
  dp[0][2] = Math.max(points[0][0], points[0][1]);
  dp[0][3] = Math.max(points[0][0], points[0][1], points[0][2]);

  for (let day = 1; day < n; day++) {
    for (let last = 0; last <= 3; last++) {
      for (let task = 0; task <= 2; task++) {
        if (task !== last) {
          let point = points[day][task] + dp[day - 1][task];
          dp[day][last] = Math.max(dp[day][last], point);
        }
      }
    }
  }
  return dp[n - 1][3];
};

const ninJaTrainingSpaceOp = (n, points) => {
  const prev = Array(4).fill(0);
  prev[0] = Math.max(points[0][1], points[0][2]);
  prev[1] = Math.max(points[0][0], points[0][2]);
  prev[2] = Math.max(points[0][0], points[0][1]);
  prev[3] = Math.max(points[0][0], points[0][1], points[0][2]);

  for (let day = 0; day <= 3; day++) {
    let temp = Array(4).fill(0);
    for (let last = 0; last <= 3; last++) {
      temp[last] = 0;
      for (task = 0; task <= 4; task) {
        if (task != last) {
          temp[last] = Math.max(temp[last], points[day][task], prev[task]);
        }
      }
    }
    prev = temp;
  }
  return prev[3];
};

const points = [
  [1, 2, 5],
  [3, 1, 1],
  [3, 3, 3],
];

// console.log(ninJaTraining(3, points));
console.log(ninJaTrainingTab(3, points));
console.log(ninJaTrainingSpaceOp(3, points));
