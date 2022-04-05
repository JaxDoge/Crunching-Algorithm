AVL Tree - Insertion, Deletion and Rotation with Python Code

class treeNode(object):
    def __init__(self, value):
        self.value = value
        self.l = None
        self.r = None
        #  The height of this node
        self.h = 1

class AVLTree(object):
    # utilize recursion and hiden stack to backtrack the minimum unbalance tree
    def insert(self, root, key):
        #  Base case of recursion, construct a new node with key
        if not root:
            return treeNode(key)
        #  Insertation of BST
        elif key < root.value:
            root.l = self.insert(root.l, key)
        else:
            root.r = self.insert(root.r, key)

        #  After insterting, the height of current node need update
        root.h = 1 + max(self.getHeight(root.l),
                        self.getHeight(root.r))

        #  Get balance factor
        b = self.getBal(root)

        #  LL case, do right rotation
        if b > 1 and key < root.l.value:
            return self.rRotate(root)
        #  RR case, do left rotation
        if b < -1 and key > root.r.value:
            return self.lRotate(root)
        #  LR case, do left rotation on the left child node, then do right rotation on root
        if b > 1 and key > root.l.value:
            root.l = self.lRotate(root.l)
            return self.rRotate(root)
        #  RL case, do right rotation on the right child node, then do left rotation on root
        if b < -1 and key < root.r.value:
            root.r = self.rRotate(root.r)
            return self.lRotate(root)

        return root


    # Recursive function to delete a node with
    # given key from subtree with given root.
    # It returns root of the modified subtree.
    def delete(self, root, key):
 
        # Step 1 - Perform standard BST delete
        if not root:
            return root
 
        elif key < root.val:
            root.left = self.delete(root.left, key)
 
        elif key > root.val:
            root.right = self.delete(root.right, key)
 
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
 
            elif root.right is None:
                temp = root.left
                root = None
                return temp
 
            temp = self.getMinValueNode(root.right)
            root.val = temp.val
            root.right = self.delete(root.right,
                                      temp.val)
 
        # If the tree has only one node,
        # simply return it
        if root is None:
            return root
 
        # Step 2 - Update the height of the
        # ancestor node
        root.height = 1 + max(self.getHeight(root.left),
                            self.getHeight(root.right))
 
        # Step 3 - Get the balance factor
        balance = self.getBalance(root)
 
        # Step 4 - If the node is unbalanced,
        # then try out the 4 cases
        # Case 1 - Left Left
        if balance > 1 and self.getBalance(root.left) >= 0:
            return self.rightRotate(root)
 
        # Case 2 - Right Right
        if balance < -1 and self.getBalance(root.right) <= 0:
            return self.leftRotate(root)
 
        # Case 3 - Left Right
        if balance > 1 and self.getBalance(root.left) < 0:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
 
        # Case 4 - Right Left
        if balance < -1 and self.getBalance(root.right) > 0:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
 
        return root


    def lRotate(self, z):

        y = z.r
        T2 = y.l

        y.l = z
        z.r = T2

        z.h = 1 + max(self.getHeight(z.l),
                        self.getHeight(z.r))
        y.h = 1 + max(self.getHeight(y.l),
                        self.getHeight(y.r))

        return y

    def rRotate(self, z):

        y = z.l
        T3 = y.r

        y.r = z
        z.l = T3

        z.h = 1 + max(self.getHeight(z.l),
                        self.getHeight(z.r))
        y.h = 1 + max(self.getHeight(y.l),
                        self.getHeight(y.r))

        return y

    def getHeight(self, root):
        if not root:
            return 0

        return root.h

    def getBal(self, root):
        if not root:
            return 0

        return self.getHeight(root.l) - self.getHeight(root.r)

    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root
 
        return self.getMinValueNode(root.left)

    def preOrder(self, root):

        if not root:
            return

        print("{0} ".format(root.value), end="")
        self.preOrder(root.l)
        self.preOrder(root.r)