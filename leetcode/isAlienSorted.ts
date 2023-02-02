// https://leetcode.com/problems/verifying-an-alien-dictionary/description/

function isAlienSorted(words: string[], order: string): boolean {
    let map = {}
    order.split("").map((el, i)=>map[el]=i)
    for(let i = 0; i < words.length - 1; i++){
        let curr = words[i], next = words[i + 1]
        let j = curr.length, count = 0
        while(j) {
            if(curr[count] && !next[count]) return false
            if(curr[count] !== next[count]){
                if(map[curr[count]] > map[next[count]]) return false
                else break  
            }
            j--; count++
        }
    }
    return true
};
