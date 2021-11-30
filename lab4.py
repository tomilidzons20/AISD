from collections import deque
from typing import Any, Callable, List, Union

import treelib as tr


class TreeNode:
    def __init__(self, value: Any):
        self.value: Any = value
        self.children: List['TreeNode'] = []
    
    def is_leaf(self) -> bool:
        if not self.children:
            return True
        return False

    def add(self, child: 'TreeNode') -> None:
        self.children.append(child)

    def for_each_deep_first(self, visit: Callable[['TreeNode'], None]) -> None:
        if not self:
            return
        visit(self)
        if not self.is_leaf():
            for child in self.children:
                child.for_each_deep_first(visit)

    def for_each_level_order(self, visit: Callable[['TreeNode'], None]) -> None:
        if not self:
            return
        visit(self)
        fifo = deque()
        for child in self.children:
            fifo.append(child)
        while fifo:
            i = fifo.popleft()
            visit(i)
            for child in i.children:
                fifo.append(child)

    def search(self, value: Any) -> Union['TreeNode', None]:
        def search_2(node: 'TreeNode') -> None:
            if node.value == value:
                res.append(node)
        res: List['TreeNode'] = []
        self.for_each_level_order(search_2)
        if res:
            return res[0]
        return None

    def __str__(self) -> str:
        return str(self.value)
    
    # def print_tree(self) -> None:
        # self.for_each_deep_first(self.__str__())
        # self.for_each_level_order(self.print(self))

        # deep first
        # self.print()
        # if not self.is_leaf():
        #     for child in self.children:
        #         child.print_tree()

        # level order
        # if not self:
        #     return
        # fifo = deque()
        # fifo.append(self)
        # while fifo:
        #     i = fifo.popleft()
        #     i.print()
        #     if i.children:
        #         for child in i.children:
        #             fifo.append(child)

class Tree:
    def __init__(self, root: 'TreeNode'):
        self.root: TreeNode = root
    
    def add(self, value: Any, parent_name: 'TreeNode') -> None:
        def search(node: 'TreeNode') -> None:
            if node == parent_name:
                res[0] = True
        res: List[bool] = [False]
        self.for_each_level_order(search)
        if res[0] == True:
            parent_name.add(TreeNode(value))  

    def for_each_level_order(self, visit: Callable[['TreeNode'], None]) -> None:
        self.root.for_each_level_order(visit)

    def for_each_deep_first(self, visit: Callable[['TreeNode'], None]) -> None:
        self.root.for_each_deep_first(visit)

    def show(self) -> None:
        tl = tr.Tree()
        tl.create_node(str(self.root), str(self.root))
        def edge(node: 'TreeNode') -> None:
            for child in node.children:
                tl.create_node(str(child), str(child), parent=str(node))
        self.for_each_deep_first(edge)
        tl.show()

tree = Tree(TreeNode(4))
c1 = TreeNode(3)
c11 = TreeNode(6)
c111 = TreeNode(0)
c12 = TreeNode(2)
c122 = TreeNode(10)
c11.add(c111)
c12.add(c122)
c1.add(c11)
c1.add(c12)

c2 = TreeNode(5)
c21 = TreeNode(7)
c211 = TreeNode(9)
c2.add(c21)
c21.add(c211)
c3 = TreeNode("osiem")

tree.root.add(c1)
tree.root.add(c2)
tree.root.add(c3)
tree.add(1, c2)
tree.add("siedem", c3)

tree.show()
