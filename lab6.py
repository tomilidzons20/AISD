from typing import Any, Callable
import treelib as tr

class BinaryNode:
    def __init__(self, value: Any):
        self.value: Any = value
        self.left_child: 'BinaryNode' = None
        self.right_child: 'BinaryNode' = None

    def min(self) -> 'BinaryNode':
        if self.left_child is None:
            return self
        return self.left_child.min()

    def traverse_pre_order(self, visit: Callable[[Any], None]) -> None:
        visit(self)
        if self.left_child is not None:
            self.left_child.traverse_pre_order(visit)
        if self.right_child is not None:
            self.right_child.traverse_pre_order(visit)

    def __str__(self):
        return str(self.value)

class BinarySearchTree:
    def __init__(self, value: Any):
        self.root: 'BinaryNode' = BinaryNode(value)

    def insert(self, value: Any) -> None:
        self._insert(self.root, value)

    def _insert(self, node: BinaryNode, value: Any) -> BinaryNode:
        if value < node.value:
            if node.left_child is not None:
                node.left_child = self._insert(node.left_child, value)
            else:
                node.left_child = BinaryNode(value)
        if value > node.value:
            if node.right_child is not None:
                node.right_child = self._insert(node.right_child, value)
        return BinaryNode(value)

    def traverse_pre_order(self, visit: Callable[[Any], None]) -> None:
        self.root.traverse_pre_order(visit)

    def show(self) -> None:
        def edge(node: 'BinaryNode') -> None:
            if node.left_child is not None:
                tl.create_node(str(node.left_child) + "(L)", str(node.left_child), str(node))
            if node.right_child is not None:
                tl.create_node(str(node.right_child) + "(R)", str(node.right_child), str(node))

        tl = tr.Tree()
        tl.create_node(str(self.root), str(self.root))
        self.traverse_pre_order(edge)
        tl.show()


tree = BinarySearchTree(5)
tree.insert(4)
# tree.insert(7)
# tree.insert(3)
# tree.insert(6)
# tree.insert(8)
tree.show()
