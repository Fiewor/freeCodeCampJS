// https://leetcode.com/problems/minimum-speed-to-arrive-on-time/

/**
 * @param {number[]} dist
 * @param {number} hour
 * @return {number}
 */
var minSpeedOnTime = function(dist, hour) {
    let l = 1, r = 10**7, res = -1, time = 0

    while(l <= r){
        let mid = Math.floor((l + r) / 2) // mid is speed
        time = calcTime(dist, mid)
        if(time > hour) l = mid + 1 // not fast enough to meet up, increase speed!
        else { // good enough, find min speed
            res = mid
            r = mid - 1
        } 
    }
    return res
};

var calcTime = function(distance, speed) {
    let time = 0

    for(let i = 0; i < distance.length - 1; i++) {
        time += Math.ceil(distance[i] / speed) // train can only depart at integer hour, so round up to account for waiting time
    }   

    time += distance.at(-1) / speed // add last speed seperately cause no waiting time
    return time
}
