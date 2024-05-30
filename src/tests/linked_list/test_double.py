from datastruct.linked_list.double import DoublyLinkedList


def test_append():
    dll = DoublyLinkedList()
    dll.append("A")
    dll.append("B")
    dll.append("C")
    assert dll.head.data == "A"
    assert dll.head.next.data == "B"
    assert dll.head.next.next.data == "C"
    assert dll.head.next.prev.data == "A"
    assert dll.head.next.next.prev.data == "B"


def test_prepend():
    dll = DoublyLinkedList()
    dll.append("A")
    dll.append("B")
    dll.prepend("C")
    assert dll.head.data == "C"
    assert dll.head.next.data == "A"
    assert dll.head.next.next.data == "B"
    assert dll.head.next.prev.data == "C"
    assert dll.head.next.next.prev.data == "A"


def test_delete_with_value():
    dll = DoublyLinkedList()
    dll.append("A")
    dll.append("B")
    dll.append("C")
    dll.delete_value("B")
    assert dll.head.data == "A"
    assert dll.head.next.data == "C"
    assert dll.head.next.prev.data == "A"
    dll.delete_value("A")
    assert dll.head.data == "C"
    dll.delete_value("C")
    assert dll.head is None


def test_delete_non_existent_value():
    dll = DoublyLinkedList()
    dll.append("A")
    dll.delete_value("B")
    assert dll.head.data == "A"
