from datastruct.linked_list.node import Node


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not data:
            return
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        new_node.prev = last_node

    def prepend(self, data):
        new_node = Node(data)
        if self.head:
            self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def delete_value(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            return
        current_node = self.head
        while current_node:
            if current_node.data == data:
                if current_node.next:
                    current_node.next.prev = current_node.prev
                if current_node.prev:
                    current_node.prev.next = current_node.next
                return
            current_node = current_node.next

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" <-> ")
            current_node = current_node.next
        print("None")
