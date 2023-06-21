// https://leetcode.com/problems/product-of-array-except-self/description/

var productExceptSelf = function(nums) {
   let res = [], n = nums.length, right = 1, left = 1

   for(let i = 0; i < n; i++){
      if(i > 0) left *= nums[i - 1]
      res[i] = left
   }

   for(let i = n - 1; i >= 0; i--){
      if(i < n - 1) right *= nums[i + 1]
      res[i] *= right
   }

   return res;
};
