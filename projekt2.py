from typing import Any, Callable, List
from testing import Queue
import binarytree as bt


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
        def level_order(node: BinaryNode, visit: Callable[[Any], None]) -> None:
            if node is None:
                return
            visit(node)
            fifo = Queue()
            nc = 0 # number of nones in level
            level = 0
            fifo.enqueue(node.left_child)
            fifo.enqueue(node.right_child)
            if node.left_child is None:
                nc += 1
            if node.right_child is None:
                nc += 1
            while fifo:
                level += 1
                if nc == 2**(level): 
                    # if number of nones in level is equal to numbers of 
                    # nodes on this level in full binary tree then tree ends
                    break
                nc = 0 # reset number of nones on level
                levelcount = len(fifo) # count number of nodes on level
                while levelcount > 0:
                    i = fifo.dequeue()
                    visit(i)
                    levelcount -= 1
                    if i is not None:
                        fifo.enqueue(i.left_child)
                        fifo.enqueue(i.right_child)
                        if i.left_child is None:
                            nc += 1
                        if i.right_child is None:
                            nc += 1
                    if i is None:
                        fifo.enqueue(None)
                        fifo.enqueue(None)
                        nc += 2
        def help(node: BinaryNode) -> None:
            if node is None:
                nodes.append(None)
                return
            nodes.append(node.value)
        nodes = []
        level_order(self.root, help)
        # print(nodes)
        print(bt.build(nodes))   


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

# tree = BinaryTree(1)
# tree.root.add_left_child(2)
# tree.root.add_right_child(3)
# tree.root.left_child.add_left_child(4)
# tree.root.left_child.add_right_child(5)
# tree.root.left_child.left_child.add_left_child(8)
# tree.root.left_child.left_child.add_right_child(9)
# tree.root.right_child.add_right_child(7)
# tree.root.right_child.right_child.add_left_child(10)

# t1 = tree.root.left_child #2
# t2 = tree.root.right_child #3
# t3 = tree.root.left_child.left_child #4
# t4 = tree.root.left_child.right_child #5
# t5 = tree.root.left_child.left_child.left_child #8
# t6 = tree.root.left_child.left_child.right_child #9
# t7 = tree.root.right_child.right_child #7
# t8 = tree.root.right_child.right_child.left_child

# tree.show()


def check_level(tree: BinaryTree, first_node: BinaryNode, second_node: BinaryNode) -> bool:
    def level_order(node: BinaryNode) -> None:
        if node is None:
            return
        level = 0
        nodes(node) # append nodelist with tree.root
        levels(level) # append levellist with 0
        fifo = Queue()
        if node.left_child is not None:
            fifo.enqueue(node.left_child)
        if node.right_child is not None:
            fifo.enqueue(node.right_child)
        while fifo:
            level += 1
            levelcount = len(fifo) # number of nodes on the same level
            while levelcount > 0:
                i = fifo.dequeue()
                nodes(i) # append nodelist with node
                levels(level) # append levellist with current level
                # node and its level are on the same position in both lists
                levelcount -= 1 # decrease number of nodes on the same leevel
                if i.left_child is not None:
                    fifo.enqueue(i.left_child)
                if i.right_child is not None:
                    fifo.enqueue(i.right_child)
    def nodes(node: BinaryNode):
        nodelist.append(node)
    def levels(level: int):
        levellist.append(level)
    nodelist: List[BinaryNode] = []
    levellist: List[int] = []
    level_order(tree.root)
    if nodelist:
        for i in range(len(nodelist)):
            if nodelist[i] == first_node:
                fnl = levellist[i] # level of first_node
            if nodelist[i] == second_node:
                snl = levellist[i] # level of second_node
        if fnl == snl:
            return True
    return False


# print(check_level(tree, t3, t8))

tree = BinaryTree(100)
tree.root.add_left_child(10)
tree.root.left_child.add_left_child(20)
tree.root.left_child.add_right_child(8)
tree.root.left_child.left_child.add_left_child(25)
tree.root.left_child.left_child.add_right_child(15)
tree.root.left_child.left_child.left_child.add_left_child(16)
tree.root.left_child.left_child.left_child.add_right_child(31)
tree.root.left_child.left_child.right_child.add_left_child(17)
tree.root.left_child.left_child.right_child.add_right_child(21)
tree.root.add_right_child(45)
tree.root.right_child.add_left_child(53)
tree.root.right_child.add_right_child(70)
tree.root.right_child.right_child.add_left_child(81)
tree.root.right_child.right_child.add_right_child(24)

n1 = tree.root.left_child # 10
n2 = tree.root.right_child # 45
n3 = tree.root.left_child.left_child # 20
n4 = tree.root.left_child.right_child # 8
n5 = tree.root.right_child.left_child # 53
n6 = tree.root.right_child.right_child # 70
n7 = tree.root.left_child.left_child.left_child # 25
n8 = tree.root.left_child.left_child.right_child # 15
n9 = tree.root.right_child.right_child.left_child # 81
n10 = tree.root.right_child.right_child.right_child # 24
n11 = tree.root.left_child.left_child.left_child.left_child # 16
n12 = tree.root.left_child.left_child.left_child.right_child # 31
n13 = tree.root.left_child.left_child.right_child.left_child # 17
n14 = tree.root.left_child.left_child.right_child.right_child # 21

tree.show()

print(check_level(tree, n10, n8))
