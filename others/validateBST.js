/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isValidBST = function (root) {
  let q = [];
  q.push(root);
  while (q.length) {
    let stack = [],
      node = q.shift();
    let curr = node.val;
    stack.push(node.val);
    if (node.left && node.left > curr) return false;
    if (node.right && node.right < curr) return false;
  }
  return true;
};
