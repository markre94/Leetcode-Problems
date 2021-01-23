# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def branchSums(self, node):
        # Write your code here.
        branch_sums = []
        self.branch_add_sum(node, 0, branch_sums)
        return branch_sums

    def branch_add_sum(self, node, runnSum, sums):
        if node is None:
            return
        newRunSum = runnSum + node.value

        if node.left is None and node.right is None:
            sums.append(newRunSum)

        self.branch_add_sum(node.left, newRunSum, sums)
        self.branch_add_sum(node.right, newRunSum, sums)

    def invert_tree(self, node):
        if node is None:
            return
        self.invert_tree(node.left)
        self.invert_tree(node.right)

        node.left, node.right = node.right, node.left

    def printTree(self, node):

        if node.left:
            self.printTree(node.left)
        print(node.value)
        if node.right:
            self.printTree(node.right)

    def nodeDepths(self, node, depth=0):
        if node is None:
            return 0
        return depth + self.nodeDepths(node.left, depth + 1) + self.nodeDepths(node.right, depth + 1)

    def maximum_depth(self, node):
        if node is None:
            return 0

        left = self.maximum_depth(node.left)
        right = self.maximum_depth(node.right)

        if left > right:
            return left + 1
        else:
            return right + 1

    def nodeDepths(self, node, val=0):
        if node is None:
            return 0
        return 1 + self.nodeDepths(node.left, val+1) + self.nodeDepths(node.right, val+1)


tree = BinaryTree(10)
tree.left = BinaryTree(3)
tree.right = BinaryTree(4)
tree.right.right = BinaryTree(11)
tree.right.left = BinaryTree(9)

my_tree = Tree()

# print(my_tree.branchSums(tree))
# my_tree.invert_tree(tree)
# print()
# print()
#
# my_tree.printTree(tree)
# print(my_tree.branchSums(tree))

print(my_tree.nodeDepths(tree))


