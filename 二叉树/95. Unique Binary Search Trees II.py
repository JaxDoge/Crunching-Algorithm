95. Unique Binary Search Trees II

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# 递归解法   注意 [] <> [None]
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
    	# Handle badcase
    	if not n: return []  # if n is zero, return empty list

    	def builder(low: int, high: int) -> List[TreeNode]:
    		res = []    # all the possible trees (root nodes)
    		# Handle boundary conditions, the last node has two None subtrees
    		if low > high:
    			res.append(None)
    			return res

    		for root in range(low, high+1):
    			# 递归计算左右子树的所有合法bst构型, 返回对应的根节点list
    			left_trees_list = builder(low, root-1)
    			right_trees_list = builder(root+1, high)
                
                #有了递归结果以后，直接构造树就完事了
                # 这就是笛卡尔积
    			for left_tree in left_trees_list:
    				for right_tree in right_trees_list:
    					root_node = TreeNode(val = root)
    					root_node.left = left_tree
    					root_node.right = right_tree 
                        
                        # record result
                        res.append(root_node)
            return res 
        return builder(1,n)


# 动态规划
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:

    	# 把一棵数每个节点的 val + offset，再返回这颗树
    	def isologueTree(node: TreeNode, offset: int):
    		if not node: return None
    		
    		# 为什么要创建一个新数？ 因为python里面的变量都是 reference，虚参指向的也是实参的内存地址, 
    		# 丫函数直接把原输入的树也给改了，就像 Morris 遍历完要断掉 dummy link 一样
    		new_node = TreeNode()
    		# 典型的前序遍历
    		new_node.val = node.val + offset
    		new_node.left = isologueTree(node.left, offset)
    		new_node.right = isologueTree(node.right, offset)
    		return new_node

    	
    	memo = []  # memo[len] 表示 1...len 的数列能构成的所有 BST 集合列表，一个简单的 int->List[TreeNode]映射
    	if not n: return memo # 写法不是很严谨，不过结果一样

    	memo.append([None])   # This is memo[0]

    	for len in range(1,n+1):
    		memo.append([])
    		for root in range(1,len+1):
    			left_sub_size = root - 1  # Classic!
    			right_sub_size = len - root
    			# 开始构造树，别被两个 for 吓到了, 其实顺序无所谓
    			for left_tree in memo[left_sub_size]:
    				for right_tree in memo[right_sub_size]:
    					newtree = TreeNode(val = root)

    					# 左子树直接使用备忘录里已有结果即可
    					# 右子树需要再备忘录的基础上调用 isologueTree 函数协助调整节点值
    					# 这样充分利用了已有计算结果，也省略了同构数的迭代构造用时
    					newtree.left = left_tree 
    					newtree.right = isologueTree(right_tree, root)
    					memo[len].append(newtree)
    	return memo[n]
        







public List<TreeNode> generateTrees(int n) {
	// dp[len] 表示 1...len 的数列能构成的所有 BST 集合列表
    ArrayList<TreeNode>[] dp = new ArrayList[n + 1];
    dp[0] = new ArrayList<TreeNode>();
    if (n == 0) {
        return dp[0];
    }


    dp[0].add(null);
    //长度为 1 到 n
    for (int len = 1; len <= n; len++) {
        dp[len] = new ArrayList<TreeNode>();
        //将不同的数字作为根节点，只需要考虑到 len
        for (int root = 1; root <= len; root++) {
            int left = root - 1;  //左子树的长度
            int right = len - root; //右子树的长度
            for (TreeNode leftTree : dp[left]) {
                for (TreeNode rightTree : dp[right]) {
                    TreeNode treeRoot = new TreeNode(root);
                    treeRoot.left = leftTree;
                    //克隆右子树并且加上偏差
                    treeRoot.right = clone(rightTree, root);
                    dp[len].add(treeRoot);
                }
            }
        }
    }
    return dp[n];
}

// 简单的前序遍历，把一棵数每个节点的 val + offset
private TreeNode clone(TreeNode n, int offset) {
    if (n == null) {
        return null;
    }
    TreeNode node = new TreeNode(n.val + offset);
    node.left = clone(n.left, offset);
    node.right = clone(n.right, offset);
    return node;
}

