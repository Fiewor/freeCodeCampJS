// https://leetcode.com/problems/count-complete-tree-nodes/

/**
 * Definition for a binary tree node.
 */
class TreeNode {
  val: number;
  left: TreeNode | null;
  right: TreeNode | null;
  constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
    this.val = val === undefined ? 0 : val;
    this.left = left === undefined ? null : left;
    this.right = right === undefined ? null : right;
  }
}

function countNodes(root: TreeNode | null): number {
  if (!root) return 0;
  let q: TreeNode[] = [],
    count = 0;
  q.push(root);
  while (q.length) {
    let node = q.shift();
    count++;
    if (node && node.left) q.push(node.left);
    if (node && node.right) q.push(node.right);
  }
  return count;
}
