from typing import Any, List, Callable, Union

class TreeNode:
    def __init__(self, value: Any =None):
        self.value: Any = value
        self.children: List['TreeNode'] = []
    
    def is_leaf(self) -> bool:
        if not self.children:
            return True
        return False

    def add(self, child: 'TreeNode') -> None:
        self.children.append(child)

    def visit(self, peak: 'TreeNode', child: 'TreeNode') -> None:
        return self.visit(peak, self.children[child+1])

    def for_each_deep_first(self, visit: Callable[['TreeNode'], None]) -> None:
        return self.for_each_deep_first(visit(self, self.children))

    def for_each_level_order(visit: Callable[['TreeNode'], None]) -> None:
        pass

    def search(value: Any) -> Union['TreeNode', None]:
        pass

    def print(self) -> None:
        print(self.value)


tree = TreeNode(4)
print(tree.is_leaf())
tree.add(TreeNode(3))
print(tree.is_leaf())
tree.print()

class Tree:
    def __init__(self, root: 'TreeNode'):
        root: TreeNode = root
    
    def add(value: Any, parent_name: Any) -> None:
        pass

    def for_each_level_order(visit: Callable[['TreeNode'], None]) -> None:
        pass

    def for_each_deep_first(visit: Callable[['TreeNode'], None]) -> None:
        pass

    def show():
        pass


dupa = [1,2,3,4]
print(dupa[2])
