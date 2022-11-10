/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
class ListNode {
  constructor(val, next) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

var mergeTwoLists = function (list1, list2) {
  // If both lists are non-empty, I first make sure a starts smaller, use its head as result,
  // and merge the remainders behind it. Otherwise, i.e., if one or both are empty, I just return what's there.

  // if (list1 && list2) {
  //   if (list1.val > list2.val) {
  //     let temp = list1;
  //     temp;
  //     list1 = list2;
  //     list2 = temp;
  //   }
  //   console.log(list1.next);
  //   list1.next = mergeTwoLists(list1.next, list2);
  // }
  // return list1 || list2;

  // ! Second solution
  // ? First make sure that a is the "better" one
  // ? (meaning b is None or has larger/equal value). Then merge the remainders behind a.
  // if(!list1 || list2 && (list1.val > list2.val)){
  //   let temp = list1
  //   list1 = list2;
  //   list2 = temp;
  // }
  // if(list1){
  //   list1.next = mergeTwoLists(list1.next, list2)
  // }
  // return list1

  // ! Third solution - works
  if (!list1 || !list2) return list1 || list2;
  if (list1.val > list2.val) {
    list2.next = mergeTwoLists(list1, list2.next);
    return list2;
  }
  list1.next = mergeTwoLists(list2, list1.next);
  return list1;

  // ! Solution that didn't quite work
  // let currentNode = new ListNode(),
  //   head = currentNode;

  // head;
  // while (list1 != null && list2 != null) {
  //   if (list1.val < list2.val) {
  //     currentNode.next = new ListNode(list1.val);
  //     currentNode;
  //     list1 = list1.next;
  //   } else {
  //     currentNode.val = list1.val;
  //     currentNode.next = new ListNode(list2.val);
  //     currentNode;
  //     list2 = list2.next;
  //   }
  // }
  // currentNode.next = list1 || list2;
  // currentNode;
  // return head.next;
};

let list1 = [1, 2, 4],
  list2 = [1, 3, 4];
let result = mergeTwoLists(list1, list2);
console.log(result);
