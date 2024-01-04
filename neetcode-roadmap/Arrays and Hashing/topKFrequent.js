// https://leetcode.com/problems/top-k-frequent-elements/


/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
    let map = new Map()
    nums.map(num => {
        map.set(num, (map.get(num)??0) + 1)
    })
    return [...map.keys()].sort((a, b) => map.get(b) - map.get(a) ).slice(0, k)
};
