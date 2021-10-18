from typing import Any


class Node:
    def __init__(self, value: Any =None):
        self.value: Any = value
        self.next: 'Node' = None


class LinkedList:
    def __init__(self):
        self.head: Node = None
        self.tail: Node = None

    def __str__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.value)
            node = node.next
        nodes = map(str, nodes)
        return " -> ".join(nodes)

    def push(self, value: Any) -> None:
        node = Node(value)
        node.next = self.head
        self.head = node
        if self.head.next is None:
            self.tail = self.head

    def append(self, value: Any) -> None:
        node = Node(value)
        if self.tail is not None:
            self.tail.next = node
            self.tail = self.tail.next
        else:
            self.head = node
            self.tail = node

    def node(self, at: int) -> None:
        current = self.head
        counter = 0
        while current is not None:
            if counter == at:
                return current
            counter += 1
            current = current.next

    def insert(self, value: Any, after: Node) -> None:
        node = Node(value)
        if after.next is not None:
            temp = after.next
            after.next = node
            node.next = temp
        else:
            after.next = node
            self.tail = node

    def pop(self) -> Any:
        if self.head is not None:
            temp = self.head
            self.head = self.head.next
            return temp.value

    def remove_last(self) -> Any:
        if self.head is not None:
            if self.head == self.tail:
                temp = self.head
                self.head = None
                self.tail = None
                return temp.value
            current = self.head
            while current.next is not self.tail:
                current = current.next
            temp = self.tail
            current.next = None
            self.tail = current
            return temp.value

    def remove(self, after: Node) -> Any:
        if after.next is None:
            return
        if after.next.next is not None:
            after.next = after.next.next
        else:
            after.next = None
            self.tail = after

    def print(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.value)
            node = node.next
        nodes = map(str, nodes)
        print(" -> ".join(nodes))

    def len(self):
        if self.head is not None:
            current = self.head
            counter = 1
            while current.next is not None:
                counter += 1
                current = current.next
            return counter
        else:
            return 0

list_ = LinkedList()

assert list_.head == None

list_.push(1)
list_.push(0)

assert str(list_) == '0 -> 1'

list_.append(9)
list_.append(10)

assert str(list_) == '0 -> 1 -> 9 -> 10'

middle_node = list_.node(at=1)
list_.insert(5, after=middle_node)

assert str(list_) == '0 -> 1 -> 5 -> 9 -> 10'

first_element = list_.node(at=0)
returned_first_element = list_.pop()

assert first_element.value == returned_first_element

last_element = list_.node(at=3)
returned_last_element = list_.remove_last()

assert last_element.value == returned_last_element
assert str(list_) == '1 -> 5 -> 9'

second_node = list_.node(at=1)
list_.remove(second_node)

assert str(list_) == '1 -> 5'
