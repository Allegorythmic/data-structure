from datastruct.linked_list.single import SinglyLinkedList
import io
import sys


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


def test_delete_value():
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


def test_delete_middle_value():
    sll = SinglyLinkedList()
    sll.append("A")
    sll.append("B")
    sll.append("C")
    sll.append("D")
    sll.delete_value("C")
    assert sll.head.data == "A"
    assert sll.head.next.data == "B"
    assert sll.head.next.next.data == "D"
    assert sll.head.next.next.next is None


def test_delete_non_existent_value():
    sll = SinglyLinkedList()
    sll.append("A")
    sll.delete_value("B")
    assert sll.head.data == "A"


def test_delete_empty_list():
    dll = SinglyLinkedList()
    dll.delete_value("A")
    assert dll.head == None


def test_print_list_with_value():
    sll = SinglyLinkedList()
    sll.append("A")
    sll.append("B")
    sll.append("C")

    captured_output = io.StringIO()
    sys.stdout = captured_output
    sll.print_list()
    sys.stdout = sys.__stdout__

    assert captured_output.getvalue().strip() == "A -> B -> C -> None"


def test_print_list_without_value():
    sll = SinglyLinkedList()
    sll.append(None)

    captured_output = io.StringIO()
    sys.stdout = captured_output
    sll.print_list()
    sys.stdout = sys.__stdout__

    assert captured_output.getvalue().strip() == "None"
