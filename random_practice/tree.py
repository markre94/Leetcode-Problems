class Node:
    def __init__(self, data: int):
        self.left: Node = None
        self.right: Node = None
        self.data = data

    def __repr__(self):
        return f"Value = {self.data}, Right childer {self.right}, Left childern {self.left}"

    def print_children(self):
        # if not self.data:
        #     return
        # pass
        if self.left:
            self.left.print_children()
        print(f"Node: {self.data} Childern left {self.left}, childern right {self.right}")
        if self.right:
            self.right.print_children()


    def invert(self):
        # if not self.data:
        #     return
        if self.left:
            self.left.invert()
        if self.right:
            self.right.invert()

        self.left, self.right = self.right, self.left


if __name__ == '__main__':
    tree = Node(1)
    tree.left = Node(2)
    tree.right = Node(3)
    tree.left.left = Node(4)
    tree.left.right = Node(5)
    tree.left.right.left = Node(6)

    tree.print_children()

    tree.invert()
    print()
    tree.print_children()




