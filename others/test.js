// "rapidapi.terminalLink.enabled": false,
// "workbench.colorTheme": "Default Dark+",

// const { uptime } = require("process");

// function sumR(arr){
//     let sum = 0
//     if(arr.length === 0) return 0
//     else sum = arr[0] + sumR(arr.slice(1, arr.length))
//     return sum
// }
// let result = sumR([1, 2, 3, 4])
// console.log(result)

// function countR(arr){
//     let count = 0
//     if(arr.length === 0) return count
//     else {
//        count = 1 + countR(arr.slice(1, arr.length))
//     }
//     return count
// }
// let result = countR([1, 2, 3, 4])
// console.log(result)

// function maxR(arr) {
//   if (arr.length === 0) return 0;
//   if (arr.length === 1) return arr[0] > arr[1] ? arr[0] : arr[1];
//   else {
//     let subArray = maxR(arr.slice(1));
//     return arr[0] > subArray ? arr[0] : subArray;
//   }
// }
// let result = maxR([1, 2, 53, 4, 7, 10]);
// console.log(result);
// maxR([1, 2, 53, 4, 7, 10])
// maxR([2, 53, 4, 7, 10])
// maxR([53, 4, 7, 10])
// maxR([4, 7, 10])
// maxR([7, 10])
// maxR([10])

// 10, 5, 2, 3
// less + pivot + greater
// pivot -> 10
// [5, 2 , 3] + [10] + [] => [2, 3, 5, 10]
// pivot - 5
// [2, 3] + [5] + [] => [2, 3, 5]
// pivot - 2
// [] + 2 + [3] => [2, 3]

// Searching
// 1. Binary - O(log n)
// 1. Simple - O(n)

// Sorting
// 1. Selection Sort - O(n^2)
// 2. Quick Sort - Average = O(n log n), Worst = O(n^2)
// 3. Merge Sort - O(n log n)

// In practice, quick sort has a smaller constant (C*n) than merge sort
// and it hits the average case more often the the worse case,
// so it is more often faster than merge sort

// Hash Function + Array = Hash Table
// Hash Function -> takes in string and returns the index
// Array stores needed values in specific indexes
// A hash tables maps keys to values
// Examples: dictionaries in Python, Objects in JavaScript
// Hash tables are great for lookups
// Hash tables are used on a larger scale for DNS resolution
// i.e translating website names to IP addresses e.g. google.com -> 74.125.239.133
// also used for caching

// Queue - FIFO - Enqueue and Dequeue
// Stack - LIFO - Push and Pop

let graph = {};
graph["you"] = ["alice", "bob", "claire"];
graph["bob"] = ["anuj", "peggy"];
graph["alice"] = ["peggy"];
graph["claire"] = ["thom", "jonny"];
graph["anuj"] = [];
graph["peggy"] = [];
graph["thom"] = [];
graph["jonnym"] = [];
// console.log(graph);

// 1. Wake up
// 2. Exercise
// 3. Brush Teeth
// 4. Pack Lunch
// 5. Shower
// 6. Eat breakfast
// 7. Get dressed

// A tree is a special type of graph, where no edges ever point back up
function personIsSeller(name) {
  console.log("name", name);
  return name !== undefined && name.split("")[-1] === "m";
}

function search(name) {
  let search_queue = [];
  search_queue = search_queue.concat(graph[name]);
  let searched = [];

  while (search_queue) {
    person = search_queue.shift();
    if (person && !searched.includes(person)) {
      console.log("person", person);
      if (personIsSeller(person)) {
        console.log(`${person} is a mango seller`);
        return true;
      } else {
        search_queue = search_queue.concat(graph[person]);
        searched.push(person);
        console.log("searched", searched);
      }
    }
  }
  return false;
  console.log(search_queue);
}

let result = search("you");
console.log("result", result);
