// https://leetcode.com/problems/binary-tree-preorder-traversal/description/

function preorderTraversal(root: TreeNode | null): number[] {
    let res = [], stack = []
    stack = [root]
    
    while(stack.length){
        let curr = stack.pop()
        if(curr){
            res.push(curr.val)
            if(curr.right) stack.push(curr.right)
            if(curr.left) stack.push(curr.left)
        }
    }
    return res
};
