// https://leetcode.com/problems/koko-eating-bananas/description/
var minEatingSpeed = function(piles, h) {
    let left = 1, right = Math.max(...piles)
    while(left < right){
        let mid = Math.floor((left+right)/2);
        let total = piles.map(pile => Math.ceil(pile/mid)).reduce((a,b)=>a+b)
        if(total<=h) right = mid
        else left = mid + 1
    }
    return left
};
