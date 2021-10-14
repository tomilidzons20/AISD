from typing import Any


class Node:
    def __init__(self, value = None, next = None):
        self.value: Any = value
        self.next: 'Node' = next


class LinkedList:
    def __init__(self):
        self.head: Node = None
        self.tail: Node = None

    def push(self, value: Any) -> None:
        newNode = Node(value)
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    def append(self, value: Any) -> None:
        pass

    def node(self, at: int) -> None:
        pass

    def insert(self, value: Any, after: Node) -> None:
        pass

    def pop(self) -> Any:
        pass

    def remove_last(self) -> Any:
        pass

    def remove(self, after: Node) -> Any:
        pass


list_ = LinkedList()
