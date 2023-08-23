const countDistinctWayToClimbStair = (n) => {
  if (n <= 1) return 1;
  else
    return (
      countDistinctWayToClimbStair(n - 2) + countDistinctWayToClimbStair(n - 1)
    );
};

let res = countDistinctWayToClimbStair(4);
