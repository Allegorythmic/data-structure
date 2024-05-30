from datastruct.linked_list.single import SinglyLinkedList


def test_append():
    sll = SinglyLinkedList()
    sll.append("A")
    sll.append("B")
    sll.append("C")
    assert sll.head.data == "A"
    assert sll.head.next.data == "B"
    assert sll.head.next.next.data == "C"


def test_prepend():
    sll = SinglyLinkedList()
    sll.append("A")
    sll.append("B")
    sll.prepend("C")
    assert sll.head.data == "C"
    assert sll.head.next.data == "A"
    assert sll.head.next.next.data == "B"


def test_delete_with_value():
    sll = SinglyLinkedList()
    sll.append("A")
    sll.append("B")
    sll.append("C")
    sll.delete_value("B")
    assert sll.head.data == "A"
    assert sll.head.next.data == "C"
    sll.delete_value("A")
    assert sll.head.data == "C"
    sll.delete_value("C")
    assert sll.head is None


def test_delete_non_existent_value():
    sll = SinglyLinkedList()
    sll.append("A")
    sll.delete_value("B")
    assert sll.head.data == "A"
