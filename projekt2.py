from typing import Any, Callable, List
import treelib as tr


class BinaryNode:
    def __init__(self, value: Any):
        self.value: Any = value
        self.left_child: 'BinaryNode' = None
        self.right_child: 'BinaryNode' = None

    def is_leaf(self) -> bool:
        if self.left_child is None and self.right_child is None:
            return True
        else:
            return False

    def add_left_child(self, value: Any) -> None:
        self.left_child = BinaryNode(value)

    def add_right_child(self, value: Any) -> None:
        self.right_child = BinaryNode(value)

    def traverse_in_order(self, visit: Callable[[Any], None]) -> None:
        if self.left_child is not None:
            self.left_child.traverse_in_order(visit)
        visit(self)
        if self.right_child is not None:
            self.right_child.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]) -> None:
        if self.left_child is not None:
            self.left_child.traverse_post_order(visit)
        if self.right_child is not None:
            self.right_child.traverse_post_order(visit)
        visit(self)

    def traverse_pre_order(self, visit: Callable[[Any], None]) -> None:
        visit(self)
        if self.left_child is not None:
            self.left_child.traverse_pre_order(visit)
        if self.right_child is not None:
            self.right_child.traverse_pre_order(visit)

    def __str__(self) -> str:
        return str(self.value)


class BinaryTree:
    def __init__(self, value: Any):
        self.root: 'BinaryNode' = BinaryNode(value)

    def traverse_in_order(self, visit: Callable[[Any], None]) -> None:
        self.root.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]) -> None:
        self.root.traverse_post_order(visit)

    def traverse_pre_order(self, visit: Callable[[Any], None]) -> None:
        self.root.traverse_pre_order(visit)

    def show(self) -> None:
        def edge(node: 'BinaryNode') -> None:
            if node.left_child is not None:
                tl.create_node(str(node.left_child), str(node.left_child), str(node))
            if node.right_child is not None:
                tl.create_node(str(node.right_child), str(node.right_child), str(node))
        tl = tr.Tree()
        tl.create_node(str(self.root), str(self.root))
        self.traverse_pre_order(edge)
        tl.show()   
        

# tree = BinaryTree(10)
# tree.root.add_left_child(9)
# tree.root.add_right_child(2)
# tree.root.left_child.add_left_child(1)
# tree.root.left_child.add_right_child(3)
# tree.root.right_child.add_left_child(4)
# tree.root.right_child.add_right_child(6)

# assert tree.root.value == 10
# assert tree.root.right_child.value == 2
# assert tree.root.right_child.is_leaf() is False
# assert tree.root.left_child.left_child.value == 1
# assert tree.root.left_child.left_child.is_leaf() is True

tree = BinaryTree(1)
tree.root.add_left_child(2)
tree.root.add_right_child(3)
tree.root.left_child.add_left_child(4)
tree.root.left_child.add_right_child(5)
tree.root.left_child.left_child.add_left_child(8)
tree.root.left_child.left_child.add_right_child(9)
tree.root.right_child.add_right_child(7)

t1 = tree.root.left_child #2
t2 = tree.root.right_child #3
t3 = tree.root.left_child.left_child #4
t4 = tree.root.left_child.right_child #5
t5 = tree.root.left_child.left_child.left_child #8
t6 = tree.root.left_child.left_child.right_child #9
t7 = tree.root.right_child.right_child #7

tree.show()


def check_level(tree: BinaryTree, first_node: BinaryNode, second_node: BinaryNode) -> bool:
    def help(node: BinaryNode, value: int, level: int) -> int:
        if node.value == value:
            return level
        levelhelp = 0
        if node.left_child is not None:
            levelhelp = help(node.left_child, value, level + 1)
        if levelhelp != 0:
            return levelhelp
        if node.right_child is not None:
            levelhelp = help(node.right_child, value, level + 1)
        return levelhelp
    levelf = help(tree.root, first_node.value, 0)
    levels = help(tree.root, second_node.value, 0)
    if levelf == levels:
        return True
    else:
        return False


print(check_level(tree, t4, t7))