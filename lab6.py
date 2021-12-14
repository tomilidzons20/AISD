from typing import Any, Callable, List
import binarytree as bt
from testing import Queue

class BinaryNode:
    def __init__(self, value: Any) -> None:
        self.value: Any = value
        self.left_child: 'BinaryNode' = None
        self.right_child: 'BinaryNode' = None

    def min(self) -> 'BinaryNode':
        if self.left_child is None:
            return self
        return self.left_child.min()


class BinarySearchTree:
    def __init__(self, value: Any):
        self.root: 'BinaryNode' = BinaryNode(value)
    
    def insert(self, value: Any) -> None:
        self._insert(self.root, value)

    def _insert(self, node: BinaryNode, value: Any) -> BinaryNode:
        if node is None:
            return BinaryNode(value)
        if value < node.value:
            node.left_child = self._insert(node.left_child, value)
        if value > node.value:
            node.right_child = self._insert(node.right_child, value)
        return node

    def insertList(self, list: List[Any]) -> None:
        for el in list:
            self.insert(el)

    def contains(self, value: Any) -> bool:
        def help(node: BinaryNode, value: Any) -> bool:
            if node is None:
                return False
            if value == node.value:
                return True
            if value < node.value:
                return help(node.left_child, value)
            if value > node.value:
                return help(node.right_child, value)
        return help(self.root, value)

    def remove(self, value: Any) -> None:
        self._remove(self.root, value)

    def _remove(self, node: BinaryNode, value: Any) -> BinaryNode:
        if node is None:
            return
        if value == node.value:
            if node.left_child is None and node.right_child is None:
                return None
            if node.left_child is None:
                return node.right_child
            if node.right_child is None:
                return node.left_child
            node.value = node.right_child.min().value
            node.right_child = self._remove(node.right_child, node.value)
        if value < node.value:
            node.left_child = self._remove(node.left_child, value)
        if value > node.value:
            node.right_child = self._remove(node.right_child, value)
        return node

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

tree = BinarySearchTree(5)
tree.insertList([1,2,4,6,3,8,9,11,7,10])
tree.show()
tree.remove(5)
tree.show()
print(tree.contains(3))
